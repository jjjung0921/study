#!/usr/bin/env python3
"""Read-only Claude hook adapter. Repository checkers own validation."""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
def run(args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
def report(result, blocking=False):
    if result.returncode:
        print((result.stdout + result.stderr)[-12000:], file=sys.stderr)
        return 2 if blocking else 1
    return 0

def main():
    try:
        event = json.load(sys.stdin)
        if not isinstance(event, dict): raise ValueError('object required')
    except (ValueError, OSError) as exc:
        print('Invalid hook input: '+str(exc), file=sys.stderr)
        return 1
    kind = event.get('hook_event_name')
    if kind in ('Stop','SubagentStop') and event.get('stop_hook_active') is True:
        print('Repeated stop: automatic retry skipped; resolve the previous checker failure before claiming completion.', file=sys.stderr)
        return 0
    study = (ROOT/'scripts/study-end.sh').exists()
    guard = [sys.executable, str(ROOT/'scripts/check-workspace.py')]
    if study: guard.append('--allow-no-git')
    result = run(guard)
    if result.returncode: return report(result, kind in ('Stop','SubagentStop'))
    if kind == 'SessionStart':
        if (ROOT/'pyproject.toml').exists():
            print('Research runs: use the Python required by pyproject.toml and scripts/run-experiment.py; the runner validates the interpreter.')
        return 0
    if kind not in ('Stop','SubagentStop'): return 0
    if kind == 'SubagentStop':
        if not study or event.get('agent_type') != 'study-grader': return 0
        for path in sorted((ROOT/'exercises').rglob('*.md')):
            if path.name.startswith('_') or path.name == 'README.md': continue
            result = run([sys.executable, 'scripts/check-exercise.py','check',str(path)])
            if result.returncode: return report(result,True)
        return 0
    current = ROOT/'.ai/CURRENT.md'
    if not current.exists(): return 0
    text = current.read_text()
    status = re.search(r'^## Status\s*\n\s*(\w+)',text,re.M)
    # Stop fires at every assistant turn, not just session closure.
    if not status or status[1] not in ('DONE','REVIEW','BLOCKED'): return 0
    script = 'scripts/study-end.sh' if study else 'scripts/ai-end.sh'
    args = ['bash',script]
    # Dirty bookkeeping means pre-close; clean history means post-close.
    head = run(['git','rev-parse','--verify','HEAD'])
    if head.returncode == 0 and not run(['git','status','--porcelain','--','.']).stdout.strip():
        args.append('--post-close')
    return report(run(args),True)

if __name__ == '__main__':
    raise SystemExit(main())
