# Agentic DevOps — Advanced Specialization

> Engagement toolkit for Microsoft partners pursuing the **Agentic DevOps Advanced Specialization** audit.

This repository combines the audit checklist with a full **engagement playbook** (discovery → hypercare) and **innersource** model so a consulting partner can stand up the offering from cold and ship to their first reference customer in 6–12 weeks.

> ⚠️ The Agentic DevOps specialization is newly framed by Microsoft + GitHub.
> Where official audit criteria are not yet public, this repo uses the closest
> published guidance as a placeholder (DevOps with GitHub on Azure specialization +
> GitHub Copilot / GHAS enablement). Confirm with your PDM before relying on
> specific thresholds, ACR pillars, or certifications. Pages marked with a
> `⚠️ Draft – confirm from official guide` callout are most affected.

---

## 🎯 Purpose

- **Pass the audit** — one page per Module A and Module B control, evidence checklist + guidance + common gaps.
- **Deliver to reference customers** — discovery workshop kit, WAF assessment, reference architectures, customer deliverable templates (HLD, LLD, runbook, KT plan, hypercare plan).
- **Productise the offering** — one-pager, qualification questionnaire, definition of done.
- **Innersource** — CONTRIBUTING, CODEOWNERS, content governance, roadmap.

---

## 🚀 Getting Started

This repo is a **GitHub Template**. Click **"Use this template"** (not Fork) to create your own copy.

### 1. Use this template

Click **Use this template → Create a new repository** and choose your GitHub organisation.

### 2. Set your site URL (optional)

The site URL is derived from `GITHUB_REPOSITORY` automatically. If you want to host on a custom domain or `<owner>.github.io` page, add a **repository variable** `ASTRO_SITE` under **Settings → Secrets and variables → Actions → Variables**.

### 3. Enable GitHub Pages

Go to **Settings → Pages → Source** → select **GitHub Actions**.

### 4. Create the engagement issues

Go to **Actions → Create Audit Engagement Issues → Run workflow**. This creates one issue per control plus a pre-qualification gate issue, labelled and grouped under an annual milestone.

### 5. Done

- Issues appear as your engagement task board 📋
- The documentation site deploys automatically on push to `main` 🌐
- Downloadable workfiles (Word, PowerPoint, Excel) live under `public/templates/` and are linked from each engagement playbook page
- Use the Engagement Agent for guided assistance 🤖

---

## 🤖 Engagement Agent

This repo ships with a **GitHub Custom Agent** purpose-built for the Agentic DevOps specialization. It knows every audit control, evidence requirement, engagement playbook page, reference architecture, and customer deliverable template.

Ask it things like:

> *"Which discovery question covers the customer's GHAS posture?"*
> *"Generate the HLD for an ARC runner pool on AKS with OIDC to Azure."*
> *"We have only 2 DPOR-linked customers — what are our options?"*
> *"What's the agent permission-scoping checklist before turning on Copilot coding agent in production?"*

The agent profile lives in [`.github/agents/engagement-agent.agent.md`](.github/agents/engagement-agent.agent.md).

---

## 📅 Annual Audit Cycle

The `Create Audit Engagement Issues` workflow runs automatically on a **schedule** (default: March 1st each year) to seed issues 9 months after the previous audit. Adjust the cron in `.github/workflows/create-issues.yml` to match your audit month + 9.

---

## 🖥️ Local Development

```bash
npm install
npm run dev
```

Build the static site with:

```bash
npm run build
```

---

## 📁 Structure

```
.
├── README.md
├── CONTRIBUTING.md
├── CODEOWNERS
├── astro.config.mjs
├── package.json
├── .github/
│   ├── agents/engagement-agent.agent.md
│   ├── memories/mdx-content.md
│   ├── ISSUE_TEMPLATE/{control-improvement,template-improvement,lesson-learned}.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── scripts/create-issues.sh
│   └── workflows/{deploy,create-issues,copilot-setup-steps}.yml
├── public/templates/
│   ├── engagement/                   # one-pager, questionnaire, deck, workbooks, DoD
│   ├── deliverables/                 # HLD, LLD, runbook, KT plan, hypercare plan
│   └── audit/                        # evidence tracker, pre-qual checklist
└── src/
    ├── content.config.ts
    └── content/docs/
        ├── index.mdx / overview.mdx / requirements.mdx / audit-process.mdx
        ├── evidence-tracker.mdx / faq.mdx
        ├── module-a/                # A.1.1 – A.3.3 (one MDX per control)
        ├── module-b/                # B.1.1 – B.4.2 (Agentic DevOps controls)
        ├── engagement/              # offering, qualification, discovery, WAF, MAP, reference architectures
        │   └── deliverables/        # HLD, LLD, runbook, KT plan, hypercare plan templates
        └── innersource/             # contributing, content governance, roadmap
```

---

## 📄 License

Content is provided for Microsoft partner enablement purposes. Refer to your Microsoft Partner Agreement for usage terms.
