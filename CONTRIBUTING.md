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

```bash
npm install
npm run dev      # http://localhost:4321/<repo>/
npm run build    # validate before opening a PR
```

Every PR must pass `npm run build` locally **and** in CI. The MDX rules in `.github/memories/mdx-content.md` are not optional — they exist because Astro 6 / MDX 3 has strict parsing.

## Innersource lifecycle

Every page on the site is tagged with a lifecycle status:

| Status | Meaning | Who can endorse |
|---|---|---|
| Draft | First version, not yet validated on an engagement | Author |
| Reviewed | Reviewed by ≥ 1 peer consultant | CODEOWNER |
| Endorsed | Used on ≥ 1 paid engagement and updated with lessons learned | Practice lead |
| Deprecated | Superseded; kept for history | Practice lead |

See [`src/content/docs/innersource/content-governance.mdx`](src/content/docs/innersource/content-governance.mdx) for the full governance model.

---

Thank you for contributing. Every improvement compounds across the next engagement.
