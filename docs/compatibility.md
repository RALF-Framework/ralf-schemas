# Compatibility Policy

## Schema compatibility

A schema version is compatible with a prior version when documents valid under the prior version remain valid and preserve the same meaning.

## Breaking changes

Breaking changes include:

- removing a field;
- renaming a field;
- changing a field type;
- adding a required field to an existing object;
- narrowing an enum;
- changing the meaning of an existing field.

## Non-breaking changes

Non-breaking changes usually include:

- adding optional fields;
- adding descriptions;
- relaxing constraints;
- adding examples;
- adding new schemas that do not alter existing ones.

## Draft period

Until `1.0.0`, breaking changes are allowed, but every change should be listed in `CHANGELOG.md`.

## Tooling rule

Tools should pin to an explicit schema version. Do not assume that `latest` is safe for production validation.
