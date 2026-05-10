# YAML Usage

RALF examples may be written in YAML for human authoring. Validation still uses JSON Schema after parsing YAML into JSON-compatible values.

Guidelines:

- use YAML 1.2-compatible syntax;
- avoid implicit booleans such as `yes` and `no`;
- quote strings that look like dates when they are not timestamps;
- avoid anchors and aliases in published examples unless necessary;
- keep examples deterministic and easy to diff.
