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
  ralf-governance-profile.schema.json
  ralf-control.schema.json
  ralf-evidence-requirement.schema.json
  ralf-approval-rule.schema.json
  ralf-runtime-enforcement.schema.json
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

## Governance validation

The schemas now include first-class validation objects for dynamic governance:

- `ralf-governance-profile.schema.json`
- `ralf-control.schema.json`
- `ralf-evidence-requirement.schema.json`
- `ralf-approval-rule.schema.json`
- `ralf-runtime-enforcement.schema.json`

These schemas validate the structure of governance information. They do **not** prove legal or regulatory compliance.

A valid governance profile only means the file follows RALF structure. It does not mean that a system satisfies the EU AI Act, ISO/IEC 42001, NIST AI RMF, or any internal compliance program.

## Supported dialect

The current schemas use JSON Schema Draft 2020-12.

YAML examples are validated by parsing YAML into JSON-compatible data structures and then applying the JSON Schemas. The schema language is still JSON Schema; there is no separate YAML schema dialect.

## Quick validation

Python:

```bash
python tools/validate.py examples/valid/project.ralf.yaml --schema schemas/draft/2020-12/ralf-project.schema.json
python tools/validate.py examples/valid/governance-profile.ralf.yaml --schema schemas/draft/2020-12/ralf-governance-profile.schema.json
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

Draft. These schemas are intended to validate early RALF examples and guide SDK/CLI/Studio development. They should be treated as unstable until the corresponding specification reaches `1.0.0`.
