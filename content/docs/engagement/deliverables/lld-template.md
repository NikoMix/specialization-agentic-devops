---
title: "Deliverable Template – Low-Level Design (LLD)"
description: "LLD template for an Agentic DevOps engagement covering repo bootstrap, branch protection, environments, OIDC role assignments, and MCP server manifests."
linkTitle: "LLD Template"
weight: 20
---

## When to use this

The LLD is the **per-repo / per-team configuration document** produced after the HLD is signed. It must be detailed enough that an engineer can implement it without further design decisions.

## Inputs you need

- Signed HLD
- Repo inventory (from discovery)
- Team / CODEOWNER mapping
- Azure subscription IDs and resource group naming convention

## Step-by-step

The following sequence drives the LLD from HLD to customer sign-off.

1. Download the DOCX template.
2. For each repo in scope, fill the per-repo configuration table.
3. For each environment, list OIDC federated credentials, Azure role assignments, and Key Vault scopes.
4. For each MCP server / GitHub App, fill the manifest (permissions, secrets, endpoints).
5. Review with the customer's lead engineer; iterate to sign-off.

## Section outline

| § | Section | Notes |
|---|---|---|
| 1 | Repo bootstrap | Default branch, protection rules, required workflows, CODEOWNERS, label set |
| 2 | Environments | Dev / Test / Prod; OIDC federated credential per env |
| 3 | Azure role assignments | Resource group, role, principal, justification |
| 4 | Key Vault scopes | Secret naming, access policies / RBAC, rotation cadence |
| 5 | GHAS configuration | Code scanning suite, secret scanning push protection, Dependabot grouping |
| 6 | Runner configuration | ARC namespace, runner image, scaling rules, allow-listed egress |
| 7 | MCP server manifests | Per-server: tools exposed, permissions, secrets, endpoint, audit |
| 8 | GitHub App manifests | Per-app: permissions, events, install scope, secret model |
| 9 | Pipeline catalog | Reusable workflows + custom actions in use |
| 10 | Validation plan | Smoke tests, security tests, rollback plan |

## Output: customer-ready deliverable

A signed LLD document (DOCX or PDF), 40–80 pages. Often delivered alongside the IaC / config-as-code repo that implements it.

{{< alert type="tip" title="Download the workfile" >}}
{{< button href="templates/deliverables/lld-template.docx" variant="outline" icon="document" >}}Download the LLD template (DOCX){{< /button >}}
{{< /alert >}}

## Reuse & contribute back

{{% alert type="tip" %}}
PR new sections (e.g., for a new MCP server pattern) via `template-improvement`.
{{% /alert %}}
