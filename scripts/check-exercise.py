#!/usr/bin/env python3
"""Check exercise records and concept evidence without certifying human input."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from collections import defaultdict

ROOT=Path(__file__).resolve().parent.parent
PURPOSES={'diagnostic','practice','verify','review'}
TYPES={'recall','condition','error-spot','fill-step','choice','numeric','skeleton',
       'derivation','proof','coding','transfer'}
HIGH_TYPES={'transfer','derivation','proof','coding'}
RESULTS={'pending','pass','partial','fail'}


def load(path):
    path=path.resolve()
    if ROOT/'exercises' not in path.parents:
        raise ValueError('exercise must be inside this workspace exercises/')
    text=path.read_text()
    fm=re.match(r'\A---\n(.*?)\n---(?:\n|$)',text,re.S)
    if not fm:raise ValueError('frontmatter missing')
    fields={}
    for line in fm[1].splitlines():
        if ':' in line:
            k,v=line.split(':',1)
            if k.strip() in fields:raise ValueError('duplicate frontmatter key')
            fields[k.strip()]=v.strip().strip('"\'')
    sections={}
    chunks=re.split(r'^## ([^\n]+)\n',text[fm.end():],flags=re.M)
    for i in range(1,len(chunks),2):
        if chunks[i] in sections:raise ValueError('duplicate section '+chunks[i])
        sections[chunks[i]]=chunks[i+1]
    return path,fields,sections


def body(sections,key):
    return re.sub(r'<!--.*?-->','',sections.get(key,''),flags=re.S).strip()


def protected(sections):
    return {k:hashlib.sha256(sections.get(k,'').encode()).hexdigest() for k in ('Problem','Rubric','Attempt')}


def snapshot(path):
    key=hashlib.sha256(path.relative_to(ROOT).as_posix().encode()).hexdigest()
    return ROOT/'.ai/grading'/f'{key}.json'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def field(path,key):
    match=re.search(r'^- '+re.escape(key)+r':\s*(.*)$',path.read_text(),re.M)
    return match[1].strip() if match else ''


def references(value):
    return [v.strip().strip('`"\'') for v in value.strip('[]').split(',') if v.strip()]


def run_record(path,fields,sections,stamp):
    content=body(sections,'Grader Run')
    links=re.findall(r'\[[^]]+\]\(([^)]+)\)',content)
    if len(links)!=1:raise ValueError('exactly one Grader Run link required')
    run=(path.parent/links[0]).resolve()
    runs=(ROOT/'.ai/grading/runs').resolve()
    if run.parent!=runs or not run.is_file():raise ValueError('Grader Run link must name an existing runs/ file')
    required=('Exercise','Input snapshot','Snapshot SHA-256','Tutor','Grader',
              'Invocation','Runtime reference','Completed','Exit status','Raw output','Result')
    record={key:field(run,key) for key in required}
    if not all(record.values()) or any('{' in value or '<' in value for value in record.values()):
        raise ValueError('Grader Run record incomplete')
    if record['Exercise'].strip('`')!=path.relative_to(ROOT).as_posix():
        raise ValueError('Grader Run exercise mismatch')
    if record['Input snapshot'].strip('`')!=stamp.relative_to(ROOT).as_posix():
        raise ValueError('Grader Run snapshot path mismatch')
    if record['Snapshot SHA-256'].strip('`')!=sha256(stamp):
        raise ValueError('Grader Run snapshot hash mismatch')
    if (record['Grader'].strip('`')!=fields['grader'] or
            record['Tutor'].strip('`')==record['Grader'].strip('`')):
        raise ValueError('Grader Run grader mismatch or not independent')
    if record['Result'].strip('`')!=fields['result'] or record['Exit status'].strip('`') not in ('0','success'):
        raise ValueError('Grader Run result or exit status mismatch')
    try:
        completed=datetime.datetime.fromisoformat(record['Completed'].strip('`'))
        if completed.tzinfo is None:raise ValueError('timezone missing')
    except ValueError as exc:raise ValueError('Grader Run completed time invalid') from exc
    output_links=re.findall(r'\[[^]]+\]\(([^)]+)\)',record['Raw output'])
    if len(output_links)!=1 or (run.parent/output_links[0]).resolve().parent!=runs:
        raise ValueError('Grader Run output link invalid')
    if not (run.parent/output_links[0]).is_file():raise ValueError('Grader Run raw output missing')
    return run


def ready(sections):
    for key in ('Problem','Rubric','Attempt'):
        if not body(sections,key):raise ValueError(key+' missing')
    attempt=body(sections,'Attempt')
    if not re.search(r'^전사 확인: OK\s*$',attempt,re.M):raise ValueError('전사 확인: OK missing')
    answer=re.sub(r'^전사 확인:.*$','',attempt,flags=re.M).strip()
    if not answer or re.fullmatch(r'<[^>]+>',answer):raise ValueError('Attempt answer missing')
    rubric={}
    for rid,text in re.findall(r'^\s*-\s*(R\d+)\.\s*(.+)$',body(sections,'Rubric'),re.M):
        if rid in rubric:raise ValueError('duplicate Rubric '+rid)
        if re.search(r'<[^>]+>',text):raise ValueError('Rubric placeholder: '+rid)
        rubric[rid]='필수' in text
    if not rubric or not any(rubric.values()):raise ValueError('numbered Rubric with required items missing')
    return rubric,answer


def check(path,prepare=False):
    path,f,s=load(path)
    result=f.get('result')
    if result not in RESULTS:raise ValueError('invalid result')
    datetime.date.fromisoformat(f.get('date',''))
    if f.get('purpose') not in PURPOSES:raise ValueError('invalid purpose')
    if f.get('type') not in TYPES:raise ValueError('invalid type')
    if not f.get('concept'):raise ValueError('concept missing')
    order=f.get('review_order','')
    if f['purpose']=='review':
        if result=='pending' and order:raise ValueError('pending review_order must be blank')
        if result!='pending' and (not order.isdecimal() or int(order)<1):
            raise ValueError('graded review requires positive review_order')
    elif order:raise ValueError('review_order only belongs to review')
    if f.get('legacy_unverified')=='true':
        if prepare or f['purpose']!='diagnostic' or result=='pending':
            raise ValueError('legacy_unverified only for historical graded diagnostic')
        return 'legacy diagnostic: retained as history, never state evidence'
    if not prepare and result=='pending':return 'pending: no grading required'
    rubric,answer=ready(s)
    stamp=snapshot(path)
    digest=protected(s)
    if prepare:
        subprocess.run([sys.executable, str(ROOT/'scripts/check-workspace.py'), '--allow-no-git'], cwd=ROOT, check=True)
        if result!='pending':raise ValueError('prepare requires pending result; never retroactively certify an existing grade')
        stamp.parent.mkdir(parents=True,exist_ok=True)
        content={'exercise':path.relative_to(ROOT).as_posix(),'protected_sha256':digest}
        if stamp.exists():
            if json.loads(stamp.read_text())!=content:raise ValueError('protected input changed; create a new attempt file')
        else:
            with stamp.open('x') as out:json.dump(content,out,ensure_ascii=False,indent=2)
        return 'ready: protected input snapshot saved; this does not prove human consent'
    if not stamp.is_file():raise ValueError('pre-grading snapshot missing; run prepare before grading')
    saved=json.loads(stamp.read_text())
    if not isinstance(saved, dict):raise ValueError('invalid pre-grading snapshot')
    if saved.get('exercise')!=path.relative_to(ROOT).as_posix() or saved.get('protected_sha256')!=digest:
        raise ValueError('Problem/Rubric/Attempt changed after prepare')
    if not f.get('grader') or re.search(r'<[^>]+>',f['grader']):raise ValueError('grader missing')
    grade=body(s,'Grading');rows={}
    for line in grade.splitlines():
        cells=[x.strip() for x in re.split(r'(?<!\\)\|',line)]
        if len(cells)<5 or not re.fullmatch(r'R\d+',cells[1]):continue
        rid,verdict,evidence=cells[1:4]
        if rid in rows:raise ValueError('duplicate grading row '+rid)
        if verdict not in ('✓','✗'):raise ValueError('invalid verdict '+rid)
        quotes=re.findall(r'"([^"\n]+)"|“([^”\n]+)”',evidence.replace(r'\|','|'))
        snippets=[a or b for a,b in quotes]
        if not snippets or not any(q in answer for q in snippets):raise ValueError('no exact Attempt quote for '+rid)
        rows[rid]=verdict
    if set(rows)!=set(rubric):raise ValueError('grading rows must cover exactly all Rubric items')
    results=re.findall(r'^- Result:\s*(pass|partial|fail)\s*$',grade,re.M)
    if results!=[result]:raise ValueError('Grading Result/frontmatter mismatch')
    all_required=all(rows[rid]=='✓' for rid,required in rubric.items() if required)
    if (result=='pass')!=all_required:raise ValueError('pass must match all required items passing')
    if not body(s,'Next'):raise ValueError('Next section missing')
    run_record(path,f,s,stamp)
    return 'graded: structure, quotations and protected inputs valid; semantic correctness not certified'


def frontmatter(path):
    text=path.read_text()
    match=re.match(r'\A---\n(.*?)\n---(?:\n|$)',text,re.S)
    if not match:raise ValueError(f'{path}: frontmatter missing')
    return {key:value.strip().strip('"\'') for key,value in
            (line.split(':',1) for line in match[1].splitlines() if ':' in line)}


def concept_files():
    return sorted(path for path in (ROOT/'concepts').glob('*.md')
                  if path.name not in ('_template.md','CONCEPT_MAP.md','MISCONCEPTIONS.md'))


def ledger():
    records=defaultdict(list)
    warnings=[]
    problems=defaultdict(dict)
    for path in sorted((ROOT/'exercises').glob('*.md')):
        if path.name in ('_template.md','README.md'):continue
        message=check(path)
        resolved,fields,sections=load(path)
        if message.startswith('legacy diagnostic:'):
            warnings.append(f'{path.relative_to(ROOT)}: legacy diagnostic has no new snapshot or run proof')
            continue
        if fields['result']=='pending':continue
        slug=fields['concept']
        records[slug].append((resolved,fields,sections))
        digest=hashlib.sha256(body(sections,'Problem').encode()).hexdigest()
        if digest in problems[slug]:
            warnings.append(f'{path.relative_to(ROOT)}: same Problem as {problems[slug][digest]}')
        else:problems[slug][digest]=path.relative_to(ROOT)
    passes=int(next((line.split(':',1)[1].strip() for line in
                     (ROOT/'LEARNER.md').read_text().splitlines()
                     if line.startswith('- verified_passes:')), '2'))
    if passes<1:raise ValueError('verified_passes must be positive')
    errors=[]
    known=set()
    for path in concept_files():
        concept=frontmatter(path)
        slug=concept.get('name') or path.stem
        known.add(slug)
        state=concept.get('state')
        if state not in ('unseen','introduced','practiced','verified','stale'):
            errors.append(f'{path.relative_to(ROOT)}: invalid state {state}')
            continue
        items=records.get(slug,[])
        by_path={str(p.relative_to(ROOT)):f for p,f,_ in items}
        cited=references(concept.get('verified_by',''))
        eligible=[]
        for ref in cited:
            f=by_path.get(ref)
            if not f or f['purpose'] not in ('practice','verify') or f['result'] not in ('pass','partial'):
                errors.append(f'{path.relative_to(ROOT)}: ineligible verified_by {ref}')
            else:eligible.append(f)
        concept_text=path.read_text()
        reviewed=state!='unseen' and not re.search(r'<!--\s*/?ai:draft\s*-->',concept_text) and all(
            re.search(r'^## '+name+r'\n\s*\S',concept_text,re.M)
            for name in ('Definition','Claims','Verification Criteria'))
        if state!='unseen' and not reviewed:
            errors.append(f'{path.relative_to(ROOT)}: concept draft has not been reviewed')
        distinct={f['date'] for f in eligible if f['result']=='pass'}
        high=any(f['result']=='pass' and f['type'] in HIGH_TYPES for f in eligible)
        base='verified' if len(distinct)>=passes and high else ('practiced' if eligible else ('introduced' if reviewed else 'unseen'))
        reviews=sorted(((int(f['review_order']),p,f) for p,f,_ in items if f['purpose']=='review'),key=lambda x:x[0])
        orders=[number for number,_,_ in reviews]
        if orders!=list(range(1,len(orders)+1)):
            errors.append(f'{path.relative_to(ROOT)}: review_order must be unique and consecutive from 1')
        history=path.read_text().split('## Review History\n',1)
        if reviews:
            if len(history)!=2:
                errors.append(f'{path.relative_to(ROOT)}: Review History missing')
            else:
                for number,exercise,f in reviews:
                    link=f'../exercises/{exercise.name}'
                    row=next((line for line in history[1].splitlines() if line.startswith(f'- {number}. ')), '')
                    if (not row or f']({link})' not in row or f['result'] not in row or
                            '근거:' not in row or '상태:' not in row):
                        errors.append(f'{path.relative_to(ROOT)}: Review History entry {number} missing evidence link')
        latest=reviews[-1][2] if reviews else None
        expected=('stale' if latest and latest['result']!='pass' and base=='verified'
                  else 'verified' if latest and latest['result']=='pass' and base=='verified'
                  else base)
        if reviews and base!='verified':
            errors.append(f'{path.relative_to(ROOT)}: review without verified base')
        if latest and concept.get('last_reviewed')!=latest['date']:
            errors.append(f'{path.relative_to(ROOT)}: last_reviewed does not match latest review')
        if state in ('verified','stale'):
            for key in ('verified_on','review_due'):
                try:datetime.date.fromisoformat(concept.get(key,''))
                except ValueError:errors.append(f'{path.relative_to(ROOT)}: {key} date missing or invalid')
        rank={'unseen':0,'introduced':1,'practiced':2,'verified':3,'stale':3}
        if rank[state]>rank[expected] or (state in ('verified','stale') and state!=expected):
            errors.append(f'{path.relative_to(ROOT)}: state {state} unsupported; expected {expected}')
        elif rank[state]<rank[expected]:
            warnings.append(f'{path.relative_to(ROOT)}: state {state}; evidence suggests {expected}')
    for slug in records.keys()-known:
        warnings.append(f'exercises for unknown concept {slug} are not state evidence')
    return warnings,errors


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=['prepare','check','ledger'])
    p.add_argument('paths',nargs='*',type=Path)
    a=p.parse_args();failed=False
    if a.mode=='ledger':
        if a.paths:p.error('ledger takes no paths')
        try:
            warnings,errors=ledger()
            for warning in warnings:print('WARN: '+warning)
            for error in errors:print('FAIL: '+error)
            print(f'ledger: {len(warnings)} warnings, {len(errors)} errors')
            return int(bool(errors))
        except (OSError,ValueError,KeyError) as exc:
            print('FAIL: ledger: '+str(exc));return 1
    if not a.paths:p.error('prepare/check requires exercise paths')
    for path in a.paths:
        try:print(str(path)+': '+check(path,a.mode=='prepare'))
        except (OSError,ValueError,KeyError,subprocess.CalledProcessError) as exc:
            print('FAIL: '+str(path)+': '+str(exc));failed=True
    return int(failed)

if __name__=='__main__':raise SystemExit(main())
