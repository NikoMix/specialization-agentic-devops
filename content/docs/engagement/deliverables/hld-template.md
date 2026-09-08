---
title: "Deliverable Template – High-Level Design (HLD)"
description: "HLD template for an Agentic DevOps engagement covering platform topology, identity, runners, agents, and policies."
linkTitle: "HLD Template"
weight: 10
---

## When to use this

The HLD is the **first** customer-facing technical document, produced at the end of discovery and refined during design. It is signed by the customer's architect and forms the basis for the LLD.

## Inputs you need

- Discovery report
- Reference architecture pick(s)
- WAF assessment scorecard
- Customer non-functional requirements

## Step-by-step

The following sequence drives the HLD from blank document to customer sign-off.

1. Download the DOCX template.
2. Replace the cover page metadata (customer, version, authors, reviewers).
3. For each reference architecture in scope (see [Reference Architectures](/docs/engagement/reference-architectures/)), copy the relevant section into the HLD body.
4. Customise diagrams in your preferred tool (Visio, Excalidraw, Mermaid) and embed.
5. Walk through the HLD with the customer's architect; iterate to sign-off.

## Section outline

| § | Section | Notes |
|---|---|---|
| 1 | Executive summary | One page; outcomes, scope, key decisions |
| 2 | Business context | From the discovery report |
| 3 | Current state | Topology + pain points |
| 4 | Target state — platform topology | RA-1 (control plane) + chosen runner / agent topologies |
| 5 | Identity & access | Entra ID, SSO, EMU decision, audit log streaming |
| 6 | Security architecture | GHAS posture, supply chain, agent permission model |
| 7 | Operational model | RACI, on-call, change management |
| 8 | Non-functional requirements | Performance, reliability, cost envelope |
| 9 | Open questions & risks | Tracked to LLD |

## Output: customer-ready deliverable

A signed HLD document (DOCX or PDF), 30–60 pages.

{{< alert type="tip" title="Download the workfile" >}}
{{< button href="templates/deliverables/hld-template.docx" variant="outline" icon="document" >}}Download the HLD template (DOCX){{< /button >}}
{{< /alert >}}

## Reuse & contribute back

{{% alert type="tip" %}}
PR new sections or pruned sections via `template-improvement`.
{{% /alert %}}
