---
title: "Innersource – Content Governance"
description: "Content lifecycle (Draft → Reviewed → Endorsed → Deprecated), endorsement criteria, review cadence."
linkTitle: "Content Governance"
weight: 20
---

The repo grows fast when engagements are running. Governance keeps quality high without slowing contribution.

## Lifecycle

Every page and downloadable template flows through this four-stage lifecycle.

| Stage | What it means | Visible signal |
|---|---|---|
| **Draft** | Author has shipped a first cut; not yet reviewed | Front-matter `status: draft`; `🟡` icon in sidebar |
| **Reviewed** | One CODEOWNER + one peer have reviewed | Front-matter `status: reviewed`; no icon |
| **Endorsed** | Used in at least two completed engagements without major rework | Front-matter `status: endorsed`; `✅` icon |
| **Deprecated** | Superseded or no longer recommended | Front-matter `status: deprecated`; `⬜` icon; deprecation banner |

## Endorsement criteria

A page or template is endorsed when **all** of the following are true.

- Used in two or more completed engagements
- No customer-reported defects
- CODEOWNER + one independent reviewer have signed off
- Lessons-learned issues from the two engagements have been resolved or absorbed into the page

## Review cadence

| Cadence | Activity |
|---|---|
| Per PR | CODEOWNER review per `CODEOWNERS` |
| Monthly | Content council triage — promote Draft → Reviewed; flag stale content |
| Quarterly | Endorsement review — promote Reviewed → Endorsed; deprecate where superseded |
| Annually | Full audit refresh ahead of Module A / Module B re-issue |

## Stale content policy

Pages with `status: draft` or `status: reviewed` that haven't been touched in 12 months are auto-flagged via an issue created by the annual `create-issues` workflow. CODEOWNER decides: refresh, endorse, or deprecate.

## Roles

| Role | Responsibility |
|---|---|
| **Practice lead** | Final endorser; deprecation sign-off |
| **Content area owner** (audit / engagement / innersource) | Day-to-day CODEOWNER reviews |
| **Contributor** | Any practice member raising a PR |

{{% alert type="tip" %}}
Roles map to the placeholders in [`CODEOWNERS`](https://github.com/NikoMix/specialization-agentic-devops/blob/main/CODEOWNERS). Replace `@NikoMix` with the real GitHub team or user once the practice is staffed.
{{% /alert %}}
