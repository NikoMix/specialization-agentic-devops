---
title: "Engagement Playbook – Reference Architectures"
description: "Six reference architectures covering GitHub + Azure control plane, runners, agents, ADO migration, secure SDLC, and agentic release pipelines."
linkTitle: "Reference Architectures"
weight: 60
---

## When to use this

Pick a reference architecture during the discovery workshop's Day 2 morning ("target state"). One engagement typically adopts 2–4 of the architectures below — the GitHub control plane is always in scope; runner, agent, and migration topologies depend on the customer's starting point.

The numbering is for reference only — the architectures are not sequential dependencies.

## Published Microsoft guidance behind each architecture

Control [B.1.1](/docs/module-b/1-1-agentic-devops-capability/) asks for architecture diagrams from delivered engagements. Basing yours on published Microsoft guidance — and citing it — is stronger evidence than an undocumented drawing, and it is faster.

The table below maps each in-repo architecture to the closest **currently published** Microsoft article. Every URL was verified to return HTTP 200 without redirecting on 8 September 2026.

| # | Architecture | Closest published Microsoft guidance | Source |
|---|---|---|---|
| RA-1 | GHEC + Entra ID + landing zone | [Deploy Azure Landing Zones](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/landing-zone-deploy) + [GHEC SSO with Entra ID](https://learn.microsoft.com/en-us/entra/identity/saas-apps/github-tutorial) + [EMU provisioning with Entra ID](https://learn.microsoft.com/en-us/entra/identity/saas-apps/github-enterprise-managed-user-provisioning-tutorial) | Architecture Center + Entra docs |
| RA-2 | Self-hosted Actions runners on Azure | [Highly available GitHub Actions on AKS](https://learn.microsoft.com/en-us/azure/aks/github-actions-azure-files-overview) + [Authenticate to Azure from GitHub Actions by OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect) | AKS + Azure Developer docs |
| RA-3 | Copilot coding agent + custom MCP servers | [Baseline Microsoft Foundry Chat in an Azure Landing Zone](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone) + [MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) + [Host MCP servers on Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/mcp-overview) | Architecture Center + product docs |
| RA-4 | Azure DevOps → GitHub migration | [Azure Boards integration with GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/?view=azure-devops) | Azure DevOps docs (weak — see gaps) |
| RA-5 | Secure SDLC (GHAS + Defender + Key Vault + signed artifacts) | [DevSecOps for Infrastructure as Code](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/devsecops-infrastructure-as-code) + [DevSecOps on AKS](https://learn.microsoft.com/en-us/azure/architecture/guide/devsecops/devsecops-on-aks) + [Quarantine pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/quarantine) | Architecture Center |
| RA-6 | Agentic release pipeline | [Azure SRE Agent](https://learn.microsoft.com/en-us/azure/sre-agent/overview) + [AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | SRE Agent docs + Architecture Center |

### Supporting platform guidance

Applies across every architecture above.

| Topic | Article |
|---|---|
| Hub-spoke topology | [Hub-spoke network topology in Azure](https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke) |
| Private Link placement and DNS | [Azure Private Link in a hub-and-spoke network](https://learn.microsoft.com/en-us/azure/architecture/networking/guide/private-link-hub-spoke-network) |
| Governed subscription provisioning | [Subscription vending implementation guidance](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) |
| DevOps architecture hub | [Get started with DevOps architecture design](https://learn.microsoft.com/en-us/azure/architecture/guide/devops/devops-get-started) |
| Repo posture in Defender for Cloud | [Defender for Cloud DevOps security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction) |

### Deployment targets for the CI/CD path

Pick whichever matches the customer's compute, and cite it as the "deploy to" half of the pipeline diagram.

| Target | Article |
|---|---|
| AKS | [Baseline architecture for an AKS cluster](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks) |
| AKS via GitOps | [GitOps for Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks) |
| App Service | [Baseline zone-redundant App Service web application](https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/baseline-zone-redundant) |
| API Management | [Automate API deployments by using APIOps](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/devops/automated-api-deployments-apiops) |

{{% alert type="caution" title="Where Microsoft has no published architecture" %}}
The Azure Architecture Center catalogue was enumerated in full (206 curated
architectures and solution ideas, plus the 524-entry table of contents). Five
areas central to this specialization have **no Architecture Center coverage at
all**, so a diagram for them has to be partner-produced:

1. **GitHub Enterprise Cloud topology** — EMU, SSO, audit log streaming. Only the
   two Entra tutorials above exist, and neither is an architecture.
2. **Actions Runner Controller and VMSS runner pools** — ARC is never named in the
   Architecture Center. The AKS article above is the nearest first-party content.
3. **GitHub Actions OIDC federation** — documented, but not as an architecture.
4. **GitHub Copilot** — does not appear anywhere in the Architecture Center catalogue.
5. **Azure DevOps → GitHub migration** — no Microsoft article covers Boards, Repos,
   Pipelines and Artifacts migration end to end; that guidance lives in GitHub's own
   GitHub Enterprise Importer documentation, outside Microsoft Learn.

Treat this as an **opportunity**, not a blocker. A partner-produced diagram in an
area Microsoft has not documented is exactly the differentiated evidence control
B.1.1 rewards.
{{% /alert %}}

{{% alert type="warning" title="Retired URLs — do not cite these" %}}
Several widely-shared Architecture Center URLs still return HTTP 200 but now
redirect to a *different* article. Citing them in an evidence pack sends the
auditor somewhere unexpected.

| Retired URL | Now lands on |
|---|---|
| `/azure/architecture/guide/aks/aks-cicd-github-actions-and-gitops` | An Azure **Pipelines** baseline article — the GitHub Actions and GitOps content is gone |
| `/azure/architecture/solution-ideas/articles/devsecops-in-github` | A 2022 DevOps how-to, outside the Architecture Center |
| `/azure/architecture/solution-ideas/articles/devsecops-in-azure` | DevSecOps on AKS |
| `/azure/architecture/example-scenario/apps/devops-dotnet-baseline` | An Azure Pipelines baseline article |
{{% /alert %}}

## RA-1 — GitHub Enterprise Cloud + Entra ID + Azure landing zone

**Published guidance:** [Deploy Azure Landing Zones](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/landing-zone-deploy) · [GHEC SSO with Entra ID](https://learn.microsoft.com/en-us/entra/identity/saas-apps/github-tutorial) · [EMU provisioning](https://learn.microsoft.com/en-us/entra/identity/saas-apps/github-enterprise-managed-user-provisioning-tutorial). No Microsoft architecture joins GHEC to a landing zone — the GHEC half of this diagram is partner-produced.

The control-plane architecture. Every Agentic DevOps engagement adopts a variant of this.

**Components**

- GHEC organisation (Standard or Enterprise Managed Users)
- Entra ID with SAML SSO + SCIM provisioning
- Audit log streaming → Event Hubs → Log Analytics → Sentinel
- Azure landing zone hub-spoke (or starter landing zone) hosting downstream Azure resources
- Conditional Access policy gating GitHub access

**When to pick**

- Always — this is the foundation.

**Common variants**

- EMU vs. non-EMU (regulated customers usually pick EMU)
- Sentinel vs. third-party SIEM destination

---

## RA-2 — Self-hosted Actions runners on Azure

**Published guidance:** [Highly available GitHub Actions on AKS](https://learn.microsoft.com/en-us/azure/aks/github-actions-azure-files-overview) · [OIDC from GitHub Actions to Azure](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect) · [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation). Actions Runner Controller itself is not documented by Microsoft.

Runner topology for security / network-isolated builds and Azure-resident workloads.

**Components**

- Actions Runner Controller (ARC) on AKS, or VMSS-backed runner pool
- OIDC trust between GitHub and Azure (workload identity federation, no long-lived secrets)
- Private endpoint to GitHub.com from runner subnet (where required)
- Key Vault for build-time secrets, pulled via workload identity

**When to pick**

- Customer has strict network egress rules
- Builds need Azure-resident network access (private endpoints, internal APIs)
- Compliance requires runner residency in a specific region

**Common variants**

- AKS + ARC (preferred for elasticity)
- VMSS (preferred when the team doesn't operate Kubernetes)

---

## RA-3 — Copilot coding agent + custom MCP servers

**Published guidance:** [Baseline Microsoft Foundry Chat in an Azure Landing Zone](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone) for the egress and secret model · [MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) for governing agent tool access · [Host MCP servers on Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/mcp-overview) for the hosting topology.

Agent topology with network egress and secret model.

**Components**

- Copilot coding agent enabled on selected repos
- Agent identity = dedicated GitHub App (not user PAT)
- Custom MCP servers hosted on Container Apps with private endpoint
- Secrets pulled from Key Vault via workload identity
- Allow-listed network egress (e.g., GitHub.com, customer internal APIs)
- Audit trail of agent actions → Sentinel

**When to pick**

- Customer wants Copilot coding agent in production beyond proof-of-concept
- Custom MCP servers needed for proprietary tools (internal docs, ticketing, deployment)

**Permission scoping checklist:** see `.github/agents/engagement-agent.agent.md` for the full list.

---

## RA-4 — Azure DevOps → GitHub migration topology

**Published guidance:** [Azure Boards integration with GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/?view=azure-devops) covers coexistence only. Microsoft publishes no end-to-end ADO-to-GitHub migration architecture; use GitHub's GitHub Enterprise Importer documentation for the mechanics and produce the topology diagram yourself.

Migration pattern for partners moving from ADO to GitHub.

**Components**

- GitHub Enterprise Importer (GEI) for repos
- Manual or template-based pipeline translation (Classic / YAML → Actions)
- Identity migration: ADO orgs / AAD → GHEC EMU
- Boards → GitHub Issues + Projects v2
- Artifacts → GitHub Packages
- Service connections → OIDC federation

**When to pick**

- Customer is currently on Azure DevOps
- Customer wants Copilot + GHAS (which favour GitHub-native repos)

**Sizing inputs** (see Engagement Agent for the full sizing matrix):

- Number of orgs / projects / repos / pipelines / agent pools / Boards work items / service connections

---

## RA-5 — Secure SDLC reference (GHAS + Defender for Cloud + Key Vault + signed artifacts)

**Published guidance:** [DevSecOps for Infrastructure as Code](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/devsecops-infrastructure-as-code) · [DevSecOps on AKS](https://learn.microsoft.com/en-us/azure/architecture/guide/devsecops/devsecops-on-aks) · [Quarantine pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/quarantine) for artifact attestation gates · [Defender for Cloud DevOps security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction).

End-to-end secure SDLC.

**Components**

- GHAS code scanning, secret scanning, Dependabot enabled at org level
- Defender for Cloud DevOps Security connector
- Branch protection + required reviews on default branches
- `actions/attest-build-provenance` for supply chain attestations
- Key Vault for all build / deploy secrets (no long-lived PATs)
- Required workflows for security gates

**When to pick**

- Always for regulated industries (financial services, healthcare, public sector)
- Customer mentions Sigstore, SLSA, or supply chain risk

---

## RA-6 — Agentic release pipeline

**Published guidance:** [Azure SRE Agent](https://learn.microsoft.com/en-us/azure/sre-agent/overview) for the on-call assistant · [AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) for the multi-agent handoff model. PR triage and release-note agents are undocumented by Microsoft.

Pattern for adding AI agents to the release path.

**Components**

- **PR triage agent** — labels, assigns reviewers, runs first-pass review
- **Release-notes agent** — drafts notes from merged PRs and Issues
- **On-call assistant agent** — triages production alerts, links to runbooks
- Agents implemented as GitHub Apps or MCP servers; backed by Azure AI Foundry agents
- Human-in-the-loop approval for all write operations (first 30 days)

**When to pick**

- Customer has already passed the Copilot coding agent pilot phase
- Customer's release process is documented and stable

---

## Reuse & contribute back

{{% alert type="tip" %}}
Add a new reference architecture (e.g., a hybrid runner pool spanning two
clouds) via a PR against this page. Use the `template-improvement` issue
template. Add the architecture diagram as a PNG or SVG under
`static/templates/architectures/`.
{{% /alert %}}
