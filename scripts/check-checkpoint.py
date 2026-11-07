#!/usr/bin/env python3
"""Validate a closed workspace without changing its checkpoint or files."""
import argparse
from pathlib import Path
import subprocess
p=argparse.ArgumentParser()
p.add_argument('checkpoint')
p.add_argument('--allow', action='append', default=[])
a=p.parse_args()
workspace=Path(__file__).resolve().parent.parent

def git(*args):
    return subprocess.check_output(['git', '-C', str(workspace), *args], stderr=subprocess.STDOUT)
try:
    root=Path(git('rev-parse','--show-toplevel').decode().strip()).resolve()
    prefix=workspace.relative_to(root).as_posix()
    prefix='' if prefix=='.' else prefix+'/'
    git('merge-base','--is-ancestor',a.checkpoint,'HEAD')
    if git('status','--porcelain','--untracked-files=all','--','.').strip():
        raise ValueError('post-close workspace must be clean')
    # Inspect each commit, not just the final diff: change-then-revert must fail.
    for sha in git('rev-list',a.checkpoint+'..HEAD','--','.').decode().split():
        paths=git('diff-tree','--root','--no-commit-id','--name-only','--no-renames','-r','-m','-z',sha).split(b'\0')
        for raw in paths:
            if not raw: continue
            path=raw.decode('utf-8','surrogateescape')
            if prefix and not path.startswith(prefix): continue
            local=path[len(prefix):]
            if not any(local==x.rstrip('/') or local.startswith(x.rstrip('/')+'/') for x in a.allow):
                raise ValueError('non-bookkeeping change after checkpoint: '+sha[:8]+' '+local)
    print('post-close: clean; checkpoint ancestor; only allowed bookkeeping changes')
except (OSError, ValueError, subprocess.CalledProcessError) as exc:
    p.exit(1,'FAIL: post-close check: '+str(exc)+'\n')
