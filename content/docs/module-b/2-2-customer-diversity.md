---
title: "B.2.2 – Customer Diversity"
description: "Evidence requirements for control B.2.2 – at least three unique customers contributing Azure Consumed Revenue via DPOR, PAL, or CSP."
linkTitle: "2.2 Customer Diversity"
weight: 30
---

{{% alert type="caution" title="⚠️ Draft – confirm from official guide" %}}
The ≥ 3 customer threshold and the eligible association types are drafts based
on the closest published guidance. Confirm with your PDM.
{{% /alert %}}

## What the Auditor Checks

The auditor verifies that your ACR comes from **at least three unique customers**, each associated via DPOR, PAL, or CSP. Concentration risk on a single customer is a fail condition.

**Typical questions:**

- Which customers contributed ACR in the qualifying pillars over the last 3 months?
- For each customer, what is the association type (DPOR / PAL / CSP)?
- Can you produce evidence of the association link?

---

## Required Evidence Checklist

The four items below cover the customer list, the per-customer proof, and the per-pillar mapping.

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **Customer list** with ACR contribution and association type | Excel, PDF | ⬜ |
| 2 | **DPOR / PAL / CSP association proof** per customer | PDF, Screenshot | ⬜ |
| 3 | **Mapping of customer → ACR pillar** | Excel, PDF | ⬜ |
| 4 | **Anonymisation key** linking display name to real customer (for internal use only) | Excel | ⬜ |

---

## Evidence Guidance

### Customer List

A simple table is sufficient.

| Display Name | Industry | Country | 3-Month ACR | Association Type | Pillar(s) |
|---|---|---|---|---|---|
| Customer A | Financial Services | UK | $25,000 | PAL | App Platform + GitHub |
| Customer B | Manufacturing | DE | $18,000 | DPOR | Azure DevOps + Pipelines |
| Customer C | Public Sector | NL | $16,000 | CSP | App Platform + GitHub |

### Association Proof

For each customer, capture one screenshot or export:

- **DPOR:** Partner Center → Customers → \<customer\> → Associations
- **PAL:** Partner Center → Customers → \<customer\> → PAL associations, or `Get-AzContext` output showing the PAL service principal
- **CSP:** Partner Center → CSP tenant → Subscriptions

### Anonymisation

The auditor sees display names (Customer A / B / C). Keep the real-name mapping in a separate file shared only with the engagement lead and the auditor on request.

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Customer list | | | ⬜ | |
| Association proof — Customer A | | | ⬜ | |
| Association proof — Customer B | | | ⬜ | |
| Association proof — Customer C | | | ⬜ | |
| Anonymisation key | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Only 2 customers contribute material ACR | Establish a PAL link with one additional customer immediately (PAL can be set up same day) |
| Customer is associated but pillar mapping is unclear | Annotate the ACR export per customer with the qualifying pillar |
| Concentration risk: 1 customer drives &gt; 80% of ACR | Surface to PDM early — some auditors flag concentration even when the count of 3 is met |
