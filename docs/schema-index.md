# Schema Index

## Common schema

`schemas/draft/2020-12/common.schema.json` contains shared definitions used by all other schemas:

- identifiers
- semantic versions
- scope objects
- metadata
- external references
- confidentiality levels
- participant types
- decision rights
- enforcement levels
- enforcement outcomes
- runtime enforcement modes
- risk levels
- conformance levels

## Top-level schemas

| Schema | Validates | Notes |
|---|---|---|
| `ralf-project.schema.json` | Complete RALF project files | Main import/export object for tools |
| `ralf-domain-pack.schema.json` | Reusable domain packs | Domain-specific lifecycles, roles, artifacts, policies, governance profiles, and knowledge |
| `ralf-context-packet.schema.json` | Task context packets | Portable task context for humans, systems, or AI assistance |
| `ralf-governance-profile.schema.json` | Governance profiles | Versioned policies, controls, approval rules, evidence requirements, and runtime enforcement expectations |
| `ralf-conformance-manifest.schema.json` | Compatibility claims | Used by tools, packs, adapters, Studio, and docs |

## Component schemas

| Schema | Validates |
|---|---|
| `ralf-lifecycle.schema.json` | lifecycle, phases, transitions, gates, feedback loops |
| `ralf-role.schema.json` | role definitions and decision rights |
| `ralf-artifact.schema.json` | artifact definitions and confidentiality |
| `ralf-policy.schema.json` | governance and policy rules |
| `ralf-control.schema.json` | governance controls mapped to phases, roles, actions, artifacts, or tools |
| `ralf-evidence-requirement.schema.json` | evidence objects required by policies, controls, gates, or approvals |
| `ralf-approval-rule.schema.json` | rules for human review, approval, rejection, or escalation |
| `ralf-runtime-enforcement.schema.json` | enforcement expectations for tool calls, artifact writes, memory access, external communication, and other runtime actions |

## Design rule

Reusable definitions belong in `common.schema.json` only when at least two schemas need them. Object-specific definitions should stay inside the object schema under `$defs`.

## Compliance note

Schema validation does not prove legal or regulatory compliance. It only confirms that a document follows the declared RALF structure.
