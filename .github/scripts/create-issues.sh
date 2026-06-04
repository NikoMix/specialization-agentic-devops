#!/usr/bin/env bash
# create-issues.sh — Agentic DevOps specialization audit issues.
# Skips any issue whose title already exists (open or closed) to avoid
# duplicates across re-runs.
#
# Environment variables expected:
#   GH_TOKEN     - GitHub token with issues:write permission
#   CYCLE_LABEL  - e.g. "audit-2026"
#   MILESTONE    - milestone title (e.g. "Audit 2026")
#   REPO         - owner/repo

set -euo pipefail

create_issue() {
  local title="$1"
  local labels="$2"
  local body="$3"

  local existing
  existing=$(gh issue list \
    --repo "$REPO" \
    --state all \
    --label "$CYCLE_LABEL" \
    --limit 200 \
    --json title \
    --jq "[.[] | select(.title == \"$title\")] | length")

  if [ "${existing:-0}" -gt 0 ]; then
    echo "⏭  Skipping (exists): $title"
    return
  fi

  gh issue create \
    --repo "$REPO" \
    --title "$title" \
    --label "$labels" \
    --milestone "$MILESTONE" \
    --body "$body"

  echo "✅ Created: $title"
}

# ─── Pre-Qualification Gate ───────────────────────────────────────────────────

create_issue \
  "🎯 Pre-Qualification Gate" \
  "pre-qualification,$CYCLE_LABEL" \
  "## Pre-Qualification Gate

Confirm pre-qualification requirements **before** requesting the Agentic DevOps audit from Partner Center.

> ⚠️ The Agentic DevOps specialization is newly framed by Microsoft + GitHub. The
> exact pre-qualification thresholds, ACR pillars, and certification list below
> are drafts based on the closest published guidance (DevOps with GitHub on Azure
> specialization + GitHub Copilot enablement). Confirm with your PDM before relying on them.

📖 [Full requirements guide](../../src/content/docs/requirements.mdx)

---

### 1 – Solutions Partner Designation

- [ ] Active **Solutions Partner for Digital & App Innovation (Azure)** confirmed in Partner Center
- [ ] Screenshot of active designation exported from Partner Center → Overview → Membership

### 2 – Azure Consumed Revenue (ACR) – draft thresholds

- [ ] ACR for GitHub + App Platform pillar confirmed ≥ \$15,000 (3-month trailing)
- [ ] ACR for Azure DevOps / Pipelines pillar confirmed ≥ \$15,000 (3-month trailing)
- [ ] ACR figures verified with PDM
- [ ] Partner Center ACR export saved for evidence

### 3 – Customer Diversity

- [ ] ≥ 3 unique customers contributing ACR via DPOR, PAL, or CSP
- [ ] Customer list exported with anonymisation key

### 4 – Certifications

- [ ] **AZ-400** Designing & Implementing Microsoft DevOps Solutions — held by ≥ 1 individual
- [ ] **GitHub Actions** certification — held by ≥ 1 individual
- [ ] **GitHub Advanced Security** certification — held by ≥ 1 individual
- [ ] **GitHub Copilot** certification (admin or developer) — held by ≥ 1 individual
- [ ] Total ≥ 5 unique certified individuals across the four certs above

---

When every box is ticked, close this issue and request the audit."

# ─── Module A — General Requirements (one issue per control) ─────────────────

declare -a MODULE_A=(
  "A.1.1|Organisational Data|articles of incorporation, organisation chart, list of key personnel"
  "A.1.2|Financial Documentation|annual financial statements, professional indemnity insurance certificate"
  "A.2.1|Service Delivery Methodology|delivery playbook, SOW template, kickoff & closure artefacts, RACI"
  "A.2.2|Quality Management|QMS policy, CSAT process, escalation procedure"
  "A.3.1|Customer Satisfaction|CSAT/NPS data, references, testimonials"
  "A.3.2|Complaint Handling|complaint register, resolved case, root cause analysis"
  "A.3.3|Security & Privacy|InfoSec policy, GDPR/data protection, breach procedure, staff training records"
)

for entry in "${MODULE_A[@]}"; do
  IFS='|' read -r ref title hints <<<"$entry"
  slug=$(echo "$ref" | tr 'A-Z.' 'a-z-')
  create_issue \
    "📋 Module A — $ref $title" \
    "module-a,$CYCLE_LABEL" \
    "## Module A — $ref $title

Collect and submit evidence for control **$ref**.

📖 [Full guidance](../../src/content/docs/module-a/${ref#A.}-${title// /-}.mdx) (see \`src/content/docs/module-a/\`)

### Evidence to collect

- [ ] $(echo "$hints" | sed 's/, /\n- [ ] /g')

### Submission

- [ ] Files named \`${ref}_<DocumentType>_v<N>.pdf\`
- [ ] Uploaded to the engagement evidence folder
- [ ] Evidence index updated"
done

# ─── Module B — Agentic DevOps (one issue per control) ───────────────────────

declare -a MODULE_B=(
  "B.1.1|Agentic DevOps Implementation Capability|case studies, reference architectures, capability statement, sample deliverables"
  "B.2.1|ACR Performance|Partner Center ACR exports, pillar breakdown, association evidence"
  "B.2.2|Customer Diversity|≥ 3 unique customers with DPOR/PAL/CSP association evidence"
  "B.3.1|Certifications Mapping|AZ-400, GitHub Actions, GHAS, Copilot cert holders mapping"
  "B.4.1|Audit Readiness|evidence index, internal pre-audit review, submission package"
  "B.4.2|Partner Onboarding Assets|customer onboarding pack, delivery templates, KT plan, runbook, hypercare plan"
)

for entry in "${MODULE_B[@]}"; do
  IFS='|' read -r ref title hints <<<"$entry"
  create_issue \
    "🤖 Module B — $ref $title" \
    "module-b,$CYCLE_LABEL" \
    "## Module B — $ref $title

Collect and submit evidence for control **$ref**.

📖 [Full guidance](../../src/content/docs/module-b/) (see \`src/content/docs/module-b/\`)

### Evidence to collect

- [ ] $(echo "$hints" | sed 's/, /\n- [ ] /g')

### Submission

- [ ] Files named \`${ref}_<DocumentType>_v<N>.pdf\`
- [ ] Uploaded to the engagement evidence folder
- [ ] Evidence index updated"
done

echo "✅ All audit engagement issues created (or skipped if already present)."
