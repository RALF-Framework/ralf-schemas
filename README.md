# RALF Schemas

Machine-readable schemas for the RALF Framework.

This repository is the validation companion to `ralf-spec`. The specification defines the meaning of RALF concepts. This repository defines the JSON Schemas used by tools to validate RALF documents.

## What this repo contains

```text
schemas/draft/2020-12/
  common.schema.json
  ralf-project.schema.json
  ralf-lifecycle.schema.json
  ralf-role.schema.json
  ralf-artifact.schema.json
  ralf-policy.schema.json
  ralf-domain-pack.schema.json
  ralf-context-packet.schema.json
  ralf-conformance-manifest.schema.json
examples/
  valid/
  invalid/
tools/
  validate.py
  validate.mjs
tests/
  validation-manifest.yaml
```

## Relationship to `ralf-spec`

`ralf-spec` is normative for semantics. `ralf-schemas` is normative for machine validation.

If a schema and the specification conflict, treat that as a bug and open a schema-change issue. Until RALF reaches `1.0.0`, schemas may change as the specification stabilizes.

## Supported dialect

The current schemas use JSON Schema Draft 2020-12.

YAML examples are validated by parsing YAML into JSON-compatible data structures and then applying the JSON Schemas. The schema language is still JSON Schema; there is no separate YAML schema dialect.

## Quick validation

Python:

```bash
python tools/validate.py examples/valid/project.ralf.yaml --schema schemas/draft/2020-12/ralf-project.schema.json
```

Node.js:

```bash
npm install
npm run validate
```

## Versioning

Schema releases follow semantic versioning after the first stable release.

- Patch: documentation fixes, clearer descriptions, non-breaking metadata changes.
- Minor: additive fields or relaxed validation.
- Major: removed fields, renamed fields, stricter required fields, or changed meaning.

During `0.x`, compatibility is best-effort and should be pinned explicitly by tooling.

## Current status

Draft. These schemas are intended to validate early RALF examples and guide SDK/CLI development. They should be treated as unstable until the corresponding specification reaches `1.0.0`.
