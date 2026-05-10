#!/usr/bin/env python3
"""Validate RALF JSON/YAML files against local JSON Schemas."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource


def load_document(path: Path):
    if path.suffix.lower() in {'.yaml', '.yml'}:
        return yaml.safe_load(path.read_text(encoding='utf-8'))
    return json.loads(path.read_text(encoding='utf-8'))


def build_registry(schema_dir: Path) -> Registry:
    registry = Registry()
    for schema_file in schema_dir.glob('*.schema.json'):
        schema = json.loads(schema_file.read_text(encoding='utf-8'))
        registry = registry.with_resource(schema['$id'], Resource.from_contents(schema))
    return registry


def validate(document_path: Path, schema_path: Path, schema_dir: Path) -> int:
    instance = load_document(document_path)
    schema = json.loads(schema_path.read_text(encoding='utf-8'))
    registry = build_registry(schema_dir)
    validator = Draft202012Validator(
        schema,
        registry=registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if not errors:
        print(f'PASS {document_path} -> {schema_path.name}')
        return 0
    print(f'FAIL {document_path} -> {schema_path.name}')
    for error in errors:
        path = '/'.join(str(part) for part in error.path) or '<root>'
        print(f'  - {path}: {error.message}')
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate a RALF JSON/YAML document.')
    parser.add_argument('document', type=Path)
    parser.add_argument('--schema', type=Path, required=True)
    parser.add_argument('--schema-dir', type=Path, default=Path('schemas/draft/2020-12'))
    args = parser.parse_args()
    return validate(args.document, args.schema, args.schema_dir)


if __name__ == '__main__':
    raise SystemExit(main())
