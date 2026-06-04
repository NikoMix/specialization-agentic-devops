# MDX content authoring rules

**Scope:** `src/content/docs/**/*.mdx`

This repository's documentation pages follow a **strict template** for control pages so that the Engagement Agent and the auto-generated GitHub Issues stay synchronised. Follow these rules whenever editing or creating MDX files.

## ⚠️ MDX syntax gotchas

MDX 3 (Astro 6 / Starlight 0.39) parses `<` followed by a letter, digit, or space as the start of a JSX tag. This breaks the build with `Unexpected character '...' before name`.

**Always escape these patterns:**

| ❌ Wrong | ✅ Right |
|---|---|
| `target <2 business days` | `target &lt; 2 business days` |
| `latency <100ms` | `latency &lt; 100ms` |
| `<6 months coverage` | `&lt; 6 months coverage` |
| `if x < 5 then` (in prose) | `if x &lt; 5 then` |
| `&` standalone in prose | `&amp;` |

Inside fenced code blocks (` ``` `) characters are NOT parsed as MDX — so you don't need to escape there.

## Tables

- Add a blank line **before AND after** every table.
- Keep column counts consistent across rows.
- Escape literal `|` inside cells as `\|`.
- If a table needs more than 5 columns, restructure into multiple tables or use a definition list.
- Use `- [ ] Item` for checklists rather than tables with a checkbox column.

## Starlight components

- Always include a short prose sentence **before** any Starlight component block (`<Steps>`, `<Tabs>`, `<CardGrid>`, `<Aside>`). MDX 3 needs the surrounding context.
- Import components at the top of the file, immediately after frontmatter.

## Links

- Relative paths only — Astro doesn't auto-prefix `base` on absolute markdown links.
- Always include a trailing slash: `./overview/` not `./overview`.
- Filenames must NOT contain dots — Starlight strips them. Use `2-1-foo.mdx` (slug `/module-a/2-1-foo/`).

## Control numbers

Control numbers in prose always use dots: `A.2.1`, `B.3.1`. Never `A2.1` or just `2.1`.

## Control page template (Module A / Module B)

Every file in `src/content/docs/module-a/` and `src/content/docs/module-b/` must follow this exact structure:

```mdx
---
title: "<MODULE>.<SECTION>.<ITEM> – <Short Title>"
description: <One-sentence summary used by Starlight + search engines>
sidebar:
  label: "<SECTION>.<ITEM> <Short Title>"
  order: <integer>
---

import { Aside } from '@astrojs/starlight/components';

## What the Auditor Checks

<Short prose paragraph>

**Typical questions:**

- <Q1>
- <Q2>
- <Q3>

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **<Item name>** | PDF, Word, Excel | ⬜ |

---

## Evidence Guidance

### <Item 1 name>
<How to produce / collect it>

---

## Evidence Status

| Item | Owner | Status | Last Updated | Notes |
|---|---|---|---|---|
| <Item 1> | | ⬜ Not started | | |

---

## Common Gaps

- **<Gap>:** <Why it fails the audit and how to prevent it>
```

## Engagement playbook page template

Every file in `src/content/docs/engagement/**/*.mdx` follows this structure:

```mdx
---
title: "<Section> – <Title>"
description: <One-sentence summary>
sidebar:
  label: "<Short label>"
  order: <integer>
---

import { Aside, Steps, Tabs, TabItem } from '@astrojs/starlight/components';

## When to use this

<Short paragraph — which engagement phase, which customer signal>

## Inputs you need from the customer

| # | Input | Source | Format |
|---|---|---|---|

## Step-by-step

The following sequence walks the consultant through the activity.

<Steps>
1. ...
</Steps>

## Output: customer-ready deliverable

<What the consultant hands to the customer — link to a template in `public/templates/`>

## Reuse & contribute back

<Aside type="tip">
  Found a missing question, control, or template variant during your engagement?
  Open a PR against `src/content/docs/engagement/...` or raise an issue with the
  `innersource` label.
</Aside>
```

## Status icons (mandatory)

| Icon | Meaning |
|---|---|
| `⬜` | Not started |
| `🟡` | In progress |
| `✅` | Complete |

## Cross-references

- Cross-link controls with **relative** paths: from `src/content/docs/audit-process.mdx`, link to `../module-a/2-1-service-delivery-methodology/` (not `/module-a/...`).
- Filenames must NOT contain dots — Starlight strips them. Use `2-1-foo.mdx`.
- Never link to GitHub Issues by hard-coded number — they vary per fork.

## Downloadable workfiles

Bind documentation to downloadable templates in `public/templates/` using:

```mdx
<Aside type="tip" title="Download the workfile">
  [📄 Download the discovery workshop deck](${'$'}{import.meta.env.BASE_URL}templates/engagement/discovery-workshop-deck.pptx)
</Aside>
```

The `${'$'}{import.meta.env.BASE_URL}` prefix is required so that the link works under any `base` path (GitHub Pages project sites use `/<repo>/`).

## When evidence requirements change

If you add, remove, or reword an evidence item in a control page, you **must** make the matching edit to `.github/scripts/create-issues.sh` so the auto-created issue checkboxes stay aligned.

## Starlight components allowed

```mdx
import { Aside, Steps, Card, CardGrid, Tabs, TabItem } from '@astrojs/starlight/components';
```

Do not introduce React components, MDX expressions that fetch data at build time, or third-party widgets without explicit need — partners may build this on locked-down CI runners.
