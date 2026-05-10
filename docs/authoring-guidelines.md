# Schema Authoring Guidelines

## Normative source

Do not add a schema field just because it is convenient for one implementation. First decide whether the field belongs in the RALF specification.

## Naming

Use lowercase `snake_case` for field names.

Use lowercase `kebab-case` for RALF identifiers.

Good:

```yaml
responsible_role: release-manager
```

Avoid:

```yaml
responsibleRole: ReleaseManager
```

## Required fields

Only make a field required when a RALF object cannot preserve its intended meaning without it.

## References

Use `$ref` for shared definitions and for reusable RALF object types. Keep `$id` stable once published.

## Extensions

Custom or experimental fields should live under `extensions`.

Extension keys should be prefixed by project, vendor, or domain, for example:

```yaml
extensions:
  acme.priority_score: 0.8
```

Extensions must not change the meaning of normative RALF fields.

## Validation is not semantic reasoning

JSON Schema validates structure, types, required fields, enums, and formats. It does not prove that a model is semantically complete. A separate CLI or SDK layer should perform cross-reference checks such as:

- every `responsible_role` exists;
- every artifact reference exists;
- every transition points to existing phases;
- every blocking policy has an owner;
- AI execution has explicit decision rights.
