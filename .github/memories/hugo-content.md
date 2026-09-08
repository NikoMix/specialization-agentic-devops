# Content authoring rules — Hugo

**Scope:** `content/**/*.md`
**Applies to:** every page on the documentation site.

The site is built with Hugo (extended) and the [`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme)
theme, pinned as a git submodule under `themes/`. Pages are plain CommonMark +
GitHub-flavoured Markdown with Hugo shortcodes — there is no JSX, and no MDX.

---

## Tables — the rule that matters most

Tables are the primary content type in this toolkit: evidence checklists, status
trackers, gap analyses, timelines. They are also the easiest thing to break.

**A Markdown table must start at column 0.** Always.

```markdown
| Control | Evidence |
|---|---|
| B.1.1 | Case studies |
```

Indenting a table breaks it in two different ways, neither of which produces an
error — the page just silently renders wrong:

| Indentation | Result |
|---|---|
| 1–3 spaces | Usually still a table, but fragile |
| 4+ spaces | Becomes an indented **code block** |
| Any indentation inside a shortcode | Stops being a table at all |

This is precisely what went wrong in the previous Astro/MDX version of this site:
tables nested inside `<TabItem>` were indented by seven spaces and rendered as
raw text. Do not reintroduce it.

Inside `{{%/* tabs */%}}` and `{{%/* alert */%}}`, keep the table hard against the
left margin:

```markdown
{{%/* tab title="Module A" */%}}
| Control | Evidence |
|---|---|
| A.1.1 | Org chart |
{{%/* /tab */%}}
```

`.github/scripts/verify_tables.py` counts the delimiter rows in every page and the
`<table>` elements in the built HTML, and fails the build if they disagree. Run it
before opening a PR:

```bash
hugo --minify --gc
python .github/scripts/verify_tables.py
```

---

## Front matter

Every page uses YAML front matter:

```yaml
---
title: "B.1.1 – Agentic DevOps Implementation Capability"
description: "One sentence, used by search engines and the theme's card summaries."
linkTitle: "1.1 Agentic DevOps Capability"
weight: 10
---
```

| Key | Purpose |
|---|---|
| `title` | Page `<h1>` and browser title |
| `description` | Meta description and list-card summary |
| `linkTitle` | Shorter label used in the docs navigation rail |
| `weight` | Ordering within the section; lower sorts first |

For **control pages** the `title` must keep the exact `X.N.M – Name` shape.
`.github/scripts/create_audit_issues.py` parses it to build the audit issue set,
and the workflow fails loudly if the pattern stops matching.

---

## Shortcodes

The theme provides `alert`, `cards`, `card`, `tabs`, `tab`, `accordion`, `badge`,
`button`, `columns`, `icon`, `figure` and `video`.

Use `{{%/* ... */%}}` (percent) when the body is Markdown, and `{{</* ... */>}}`
(angle) when it is not.

### Callouts

```markdown
{{%/* alert type="caution" title="Draft – confirm from official guide" */%}}
Markdown **content** here.
{{%/* /alert */%}}
```

`type` is one of `note`, `tip`, `important`, `warning`, `caution`.

GitHub-style alerts also work through a render hook and need no shortcode:

```markdown
> [!NOTE]
> Rendered as a callout.
```

### Tabs

```markdown
{{</* tabs */>}}
{{%/* tab title="Module A" */%}}
Markdown, unindented.
{{%/* /tab */%}}
{{%/* tab title="Module B" */%}}
Markdown, unindented.
{{%/* /tab */%}}
{{</* /tabs */>}}
```

### Download links

Workfiles live in `static/templates/`. Link them with the `button` shortcode, never
a bare Markdown link — the shortcode runs the path through `relURL`, so it keeps
working under the `/specialization-agentic-devops/` base path that GitHub Pages
serves from.

```markdown
{{</* button href="/templates/audit/evidence-tracker.xlsx" variant="outline" icon="grid" */>}}Download the Evidence Tracker (XLSX){{</* /button */>}}
```

Icons: `grid` for XLSX, `document` for DOCX, `collections` for PPTX.

---

## Links

Use **absolute, site-rooted** paths for internal links:

```markdown
[Evidence Tracker](/docs/evidence-tracker/)
[Control B.1.1](/docs/module-b/1-1-agentic-devops-capability/)
```

The theme's link render hook resolves these through `.Page.GetPage`, rewrites them
to the correct `RelPermalink` including the base path, and **warns on a broken
link**. The deploy workflow turns that warning into a build failure, so a dead
internal link cannot ship.

External links get `rel="noopener noreferrer"` and open in a new tab automatically.

---

## Page structure — control pages

Every file in `content/docs/module-a/` and `content/docs/module-b/`:

1. `## What the Auditor Checks` — what the control is really testing
2. `## Required Evidence Checklist` — a `| # | Evidence Item | Accepted Formats | Status |` table
3. `## Evidence Guidance` — how to produce each item
4. `## Evidence Status` — an owner/due-date/status tracking table
5. `## Common Gaps` — a `| Gap | Remediation |` table

The evidence checklist table is **machine-read** by the issue generator. Keep the
header row exactly as above; the generator fails the workflow rather than opening
a partial issue set if it stops parsing.

---

## Filenames

- Lower-case kebab-case, no dots: `2-1-acr-performance.md`
- Section landing pages are `_index.md`
- The URL follows the path: `content/docs/module-b/2-1-acr-performance.md` → `/docs/module-b/2-1-acr-performance/`

---

## Escaping

Unlike MDX, Hugo needs almost no escaping.

| Character | In Hugo |
|---|---|
| `<` before a letter | Fine in prose; use `&lt;` only inside raw HTML |
| `$` | Literal. Do **not** write `\$` — the backslash renders |
| `{` `}` | Literal, unless it forms `{{` |
| `|` inside a table cell | Escape as `\|` |
