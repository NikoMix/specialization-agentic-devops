# Contributing

This is an **innersource** repository for consultants pursuing or delivering the Agentic DevOps Advanced Specialization. Every engagement is an opportunity to improve the toolkit — please contribute back.

## How to contribute

1. **Open an issue first** using one of the templates in `.github/ISSUE_TEMPLATE/`:
   - `control-improvement` — refine an audit control's evidence list or guidance
   - `template-improvement` — improve a customer deliverable template (HLD, LLD, runbook, KT plan, hypercare plan)
   - `lesson-learned` — capture a finding from a delivered engagement
2. **Branch** from `main` using `feat/<short-slug>`, `fix/<short-slug>`, or `docs/<short-slug>`.
3. **Commit** with conventional messages: `feat(module-b): add agent permission scoping checklist`.
4. **Open a PR** using the `.github/PULL_REQUEST_TEMPLATE.md`. Map the PR to:
   - The engagement phase (qualify, discover, design, deliver, hypercare)
   - The audit control(s) it touches (A.x.y or B.x.y)
   - The innersource lifecycle stage (Draft / Reviewed / Endorsed / Deprecated)

## Review SLA

| Change type | Reviewer | Target SLA |
|---|---|---|
| Typo / link fix | Any CODEOWNER | 1 business day |
| Content update to existing page | CODEOWNER for that area | 3 business days |
| New control page / template | Practice lead + 1 peer | 5 business days |
| Breaking change to workflow / build | Practice lead + repo admin | 5 business days |

## Code of conduct

Be specific, evidence-based, and respectful. Anonymise customer data before sharing.

- Never commit a real customer name, contract value, or identifiable engagement detail.
- Use "Customer A", "Customer B", or a sector descriptor ("a large UK retailer") instead.
- Treat the repo as if a Microsoft auditor and a competitor partner could read every commit.

## Local development

The site is built with [Hugo](https://gohugo.io/) **extended** v0.165.0 or newer and the [`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme) theme, pinned as a git submodule under `themes/`.

```bash
git clone --recurse-submodules https://github.com/NikoMix/specialization-agentic-devops.git
hugo server      # http://localhost:1313/<repo>/
```

In an existing clone: `git submodule update --init --recursive`.

Every PR must pass both of these locally **and** in CI:

```bash
hugo --minify --gc                        # fails on a broken internal link
python .github/scripts/verify_tables.py   # every Markdown table reached the HTML
```

The content rules in `.github/memories/hugo-content.md` are not optional. The most important one: **a Markdown table must start at column 0.** Indented four spaces it becomes a code block; indented inside a shortcode it stops being a table at all. `verify_tables.py` exists to catch exactly this.

## Innersource lifecycle

Every page on the site is tagged with a lifecycle status:

| Status | Meaning | Who can endorse |
|---|---|---|
| Draft | First version, not yet validated on an engagement | Author |
| Reviewed | Reviewed by ≥ 1 peer consultant | CODEOWNER |
| Endorsed | Used on ≥ 1 paid engagement and updated with lessons learned | Practice lead |
| Deprecated | Superseded; kept for history | Practice lead |

See [`content/docs/innersource/content-governance.md`](content/docs/innersource/content-governance.md) for the full governance model.

---

Thank you for contributing. Every improvement compounds across the next engagement.
