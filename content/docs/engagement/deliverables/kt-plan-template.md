---
title: "Deliverable Template – Knowledge Transfer (KT) Plan"
description: "KT plan template for the customer platform team — RACI, shadow → reverse-shadow milestones, skills check rubric."
linkTitle: "KT Plan Template"
weight: 40
---

## When to use this

Start the KT plan **at design time**, not at engagement close. The customer platform team needs to be shadowing from day one if they are going to operate the platform without partner help.

## Inputs you need

- Customer platform team roster + skills baseline
- LLD section table of contents
- Engagement timeline

## Step-by-step

The following sequence drives the KT plan from kickoff to skills-check sign-off.

1. Download the DOCX template.
2. Map customer platform team members to RACI roles per module.
3. Schedule shadow → reverse-shadow milestones for each module.
4. Define skills-check rubric per module (1-hour practical test).
5. Run skills checks before engagement close; iterate until pass.

## KT modules

| # | Module | Skills checked |
|---|---|---|
| 1 | GitHub org administration | Create repo from template; configure branch protection; rotate org PAT |
| 2 | GHAS triage | Resolve a code scanning alert; address a secret scanning finding |
| 3 | Actions workflow authoring | Author a reusable workflow; configure OIDC federation |
| 4 | Self-hosted runner ops | Scale an ARC pool; patch a runner image; troubleshoot a stuck runner |
| 5 | Copilot administration | Add / remove seat; configure content exclusions; audit usage |
| 6 | Copilot coding agent ops | Enable agent on a repo; review agent PR; revert agent action |
| 7 | MCP server ops | Deploy a new MCP server; rotate its credentials |
| 8 | Audit log + SIEM integration | Query Sentinel for an audit event; configure a new detection |

## Shadow → reverse-shadow milestones

The same 4-stage progression applies per module.

| Stage | Who drives | Who observes | Duration |
|---|---|---|---|
| Stage 1 — Shadow | Partner | Customer | 1 sprint |
| Stage 2 — Co-pilot | Partner | Customer (asks questions) | 1 sprint |
| Stage 3 — Reverse-shadow | Customer | Partner (corrects only blockers) | 1 sprint |
| Stage 4 — Independent | Customer | Partner not present | 1 sprint |

## Output: customer-ready deliverable

A signed KT plan + skills-check results per module.

{{< alert type="tip" title="Download the workfile" >}}
{{< button href="templates/deliverables/kt-plan-template.docx" variant="outline" icon="document" >}}Download the KT Plan template (DOCX){{< /button >}}
{{< /alert >}}

## Reuse & contribute back

{{% alert type="tip" %}}
PR new modules (e.g., for newly-released GitHub features) via `template-improvement`.
{{% /alert %}}
