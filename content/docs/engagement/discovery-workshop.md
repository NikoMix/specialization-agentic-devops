---
title: "Engagement Playbook – Discovery Workshop Kit"
description: "2-day discovery workshop agenda, stakeholder map, current vs. target SDLC, Copilot guardrails, GHAS baseline, success metrics."
linkTitle: "Discovery Workshop Kit"
weight: 30
---

## When to use this

Run the discovery workshop once the qualification questionnaire scores **Go**. It is a 2-day workshop with the customer's platform team, a security rep, and an engineering manager. The output is a baseline + target-state document plus a draft engagement plan.

## Inputs you need from the customer

| # | Input | Source | Format |
|---|---|---|---|
| 1 | Completed qualification questionnaire | Customer | DOCX |
| 2 | Read-only admin access to GHEC / ADO org | Customer | Invite |
| 3 | Pipeline metrics export (cycle time, green-build rate) | Customer | CSV / XLSX |
| 4 | Stakeholder list with roles | Customer | XLSX |

## Step-by-step

The following sequence covers the 2-day workshop end-to-end.

1. Day 0 — send the deck, agenda, and pre-read; confirm attendees and any environment access.
2. Day 1 morning — stakeholder map, business outcomes, current-state SDLC walkthrough.
3. Day 1 afternoon — pipeline + GHAS baseline tour, identity and access review, Copilot adoption signals.
4. Day 2 morning — target state design (reference architecture pick), agent permission model.
5. Day 2 afternoon — engagement plan draft, RACI, definition of done, next steps.
6. Day 3+ — write up the discovery report and share within 5 business days.

## Agenda — Day 1

| Time | Topic | Output |
|---|---|---|
| 09:00 | Welcome + outcomes | Shared outcomes statement |
| 09:30 | Stakeholder map | RACI draft |
| 10:30 | Current-state SDLC walkthrough | Process flow diagram |
| 13:30 | Pipeline + GHAS baseline tour | Baseline metrics scorecard |
| 15:00 | Identity & access review | Access map + gaps |
| 16:00 | Copilot adoption signals | Adoption baseline + guardrail list |

## Agenda — Day 2

| Time | Topic | Output |
|---|---|---|
| 09:00 | Target state — reference architecture | Architecture pick |
| 10:30 | Agent permission scoping | Agent + MCP scope matrix |
| 13:30 | Engagement plan draft | Plan v0.1 |
| 15:00 | Definition of done | DoD draft |
| 16:00 | Next steps + open actions | Action register |

## WAF + MAP touchpoints

The workshop deliberately surfaces the inputs you'll need for the next two artifacts in this playbook.

{{< tabs >}}
{{% tab title="WAF" %}}
Capture answers for the [WAF Assessment](/docs/engagement/waf-assessment/) on Operational Excellence + Security pillars during the current-state walkthrough.
{{% /tab %}}
{{% tab title="MAP / readiness" %}}
Capture answers for the [Assessment Platform Inputs](/docs/engagement/assessment-platform-inputs/) (DevOps maturity, Copilot readiness, GHAS posture) during the baseline tour.
{{% /tab %}}
{{< /tabs >}}

## Output: customer-ready deliverable

A discovery report (15–25 pages) + a baseline scorecard (XLSX) + the engagement plan v0.1.

{{< alert type="tip" title="Download the workfiles" >}}
{{< button href="templates/engagement/discovery-workshop-deck.pptx" variant="outline" icon="collections" >}}Discovery Workshop Deck (PPTX){{< /button >}} · {{< button href="templates/engagement/discovery-workshop-workbook.xlsx" variant="outline" icon="grid" >}}Discovery Workshop Workbook (XLSX){{< /button >}}
{{< /alert >}}

## Reuse & contribute back

{{% alert type="tip" %}}
Found an agenda item you always cut, or one that always overruns? PR the deck
and the page. Use the `lesson-learned` issue template to capture the rationale.
{{% /alert %}}
