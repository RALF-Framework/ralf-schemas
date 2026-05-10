#!/usr/bin/env python3
"""Run the repository validation manifest."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'tests' / 'validation-manifest.yaml'


def run_case(file_path: Path, schema_path: Path, should_pass: bool) -> bool:
    cmd = [sys.executable, str(ROOT / 'tools' / 'validate.py'), str(file_path), '--schema', str(schema_path), '--schema-dir', str(ROOT / 'schemas' / 'draft' / '2020-12')]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    passed = result.returncode == 0
    print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, end='', file=sys.stderr)
    if passed != should_pass:
        print(f'UNEXPECTED RESULT: {file_path} expected {"pass" if should_pass else "fail"}')
        return False
    return True


def main() -> int:
    manifest = yaml.safe_load(MANIFEST.read_text(encoding='utf-8'))
    ok = True
    for item in manifest.get('valid', []):
        ok &= run_case(ROOT / item['file'], ROOT / item['schema'], True)
    for item in manifest.get('invalid', []):
        ok &= run_case(ROOT / item['file'], ROOT / item['schema'], False)
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
