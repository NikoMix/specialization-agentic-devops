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

### 2. Set your site URL

Set `baseURL` in [`hugo.toml`](hugo.toml) to your published address. The deploy workflow overrides it at build time with the URL that GitHub Pages reports, so this only matters for local builds and for a custom domain.

### 3. Enable GitHub Pages

Go to **Settings → Pages → Source** → select **GitHub Actions**.

### 4. Create the engagement issues

Go to **Actions → Create Audit Engagement Issues → Run workflow**. It opens **43 issues** for the cycle:

| Issues | Scope |
|---:|---|
| 1 | Pre-qualification gate, built from the Quick Readiness Checklist |
| 7 | One per Module A control (A.1.1 – A.3.3) |
| 6 | One per Module B control (B.1.1 – B.4.2) |
| 29 | One per **Module B evidence item**, linked back to its control issue |

All of them are labelled, grouped under an annual milestone, and derived from the pages in `content/docs/` — so they cannot drift from the guide. Re-running skips anything that already exists. Use the `scope` and `dry_run` inputs to preview or to open just one module.

### 5. Done

- Issues appear as your engagement task board 📋
- The documentation site deploys automatically on push to `main` 🌐
- Downloadable workfiles (Word, PowerPoint, Excel) live under `static/templates/` and are linked from each engagement playbook page
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

The site is built with **[Hugo](https://gohugo.io/) extended v0.165.0 or newer** and the [`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme) theme, which is pinned as a git submodule under `themes/`.

```bash
git clone --recurse-submodules https://github.com/NikoMix/specialization-agentic-devops.git
cd specialization-agentic-devops

hugo server        # http://localhost:1313/specialization-agentic-devops/
```

In an existing clone that predates the submodule:

```bash
git submodule update --init --recursive
```

Validate before opening a PR — the same two commands CI runs:

```bash
hugo --minify --gc
python .github/scripts/verify_tables.py
```

> [!NOTE]
> The theme is consumed as a **git submodule**, not a Hugo Module, even though its
> README recommends the latter. Go's module packaging strips every directory named
> `vendor`, and the theme keeps its Chroma syntax-highlighting partial at
> `assets/scss/vendor/_chroma.scss`. Imported as a Hugo Module that file is absent
> from the module zip, and the theme's `@import "vendor/chroma"` fails the build.
> Once the directory is renamed upstream, `hugo.toml` can move to `[module.imports]`.

---

## 📁 Structure

```
.
├── README.md
├── CONTRIBUTING.md
├── CODEOWNERS
├── hugo.toml                         # site config, menus, theme params
├── .github/
│   ├── agents/engagement-agent.agent.md
│   ├── memories/hugo-content.md      # content authoring rules
│   ├── ISSUE_TEMPLATE/{control-improvement,template-improvement,lesson-learned}.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── scripts/create_audit_issues.py
│   ├── scripts/verify_tables.py
│   └── workflows/{deploy,create-issues,copilot-setup-steps}.yml
├── themes/ms-hugo-theme/             # submodule: NikoMix/ms-hugo-theme
├── static/templates/
│   ├── engagement/                   # one-pager, questionnaire, deck, workbooks, DoD
│   ├── deliverables/                 # HLD, LLD, runbook, KT plan, hypercare plan
│   └── audit/                        # evidence tracker, pre-qual checklist
└── content/
    ├── _index.md                     # home page
    └── docs/
        ├── overview.md / requirements.md / audit-process.md
        ├── evidence-tracker.md / faq.md
        ├── module-a/                 # A.1.1 – A.3.3 (one page per control)
        ├── module-b/                 # B.1.1 – B.4.2 (Agentic DevOps controls)
        ├── engagement/               # offering, qualification, discovery, WAF, MAP, reference architectures
        │   └── deliverables/         # HLD, LLD, runbook, KT plan, hypercare plan templates
        └── innersource/              # contributing, content governance, roadmap
```

---

## 📄 License

Content is provided for Microsoft partner enablement purposes. Refer to your Microsoft Partner Agreement for usage terms.
