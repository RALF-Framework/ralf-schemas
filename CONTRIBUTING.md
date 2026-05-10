# Contributing

RALF schemas should follow the RALF specification. If a proposed change alters the meaning of a RALF concept, update or discuss the specification first.

## Local checks

```bash
python tools/validate-all.py
```

or:

```bash
npm install
npm run validate
```

## Compatibility

Schema changes must describe compatibility impact:

- non-breaking;
- breaking;
- documentation/example only.

Breaking changes during the draft period are allowed but must be recorded in `CHANGELOG.md`.
