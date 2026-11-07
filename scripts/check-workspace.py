#!/usr/bin/env python3
"""Verify the owning Git repository before project mutations. No writes."""
import argparse
import os
from pathlib import Path
import subprocess

p = argparse.ArgumentParser()
p.add_argument('--workspace', type=Path, default=Path(__file__).resolve().parent.parent)
p.add_argument('--git-root', default=os.environ.get('AI_EXPECTED_GIT_ROOT'))
p.add_argument('--allow-no-git', action='store_true')
a = p.parse_args()
workspace = a.workspace.expanduser().resolve()
expected = Path(a.git_root).expanduser().resolve() if a.git_root else workspace
if workspace != expected and expected not in workspace.parents:
    p.exit(1, 'FAIL: expected Git root must contain the workspace\n')
r = subprocess.run(['git', '-C', str(workspace), 'rev-parse', '--show-toplevel'], text=True, capture_output=True)
if r.returncode:
    if a.allow_no_git:
        print('No Git repository: initialize this workspace before committing.')
        raise SystemExit(0)
    p.exit(1, 'FAIL: initialize an independent Git repository first\n')
actual = Path(r.stdout.strip()).resolve()
if actual != expected:
    p.exit(1, 'FAIL: Git root mismatch: expected %s, actual %s. Initialize the project or explicitly set AI_EXPECTED_GIT_ROOT.\n' % (expected, actual))
