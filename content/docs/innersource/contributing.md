---
title: "Innersource – Contributing"
description: "How to contribute to the Agentic DevOps specialization repo — branch policy, commit conventions, PR review SLA, evidence handling."
linkTitle: "Contributing"
weight: 10
---

This page is the site-rendered version of [`CONTRIBUTING.md`](https://github.com/NikoMix/specialization-agentic-devops/blob/main/CONTRIBUTING.md). When the two disagree, the markdown file in the repo root wins.

## Who can contribute

Anyone in the practice. The audience is partner consultants delivering Agentic DevOps engagements — not customers. Engagement artefacts (customer names, secrets, customer IP) must **never** be checked in. See "Evidence handling" below.

## Branch policy

This repo commits **directly to `main`**. There is no `develop` branch and no long-lived feature branches. For larger changes, use a short-lived topic branch and PR back into `main`.

## Commit conventions

Conventional Commits — `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`. Include the Copilot co-author trailer:

```
Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

## PR review SLA

| PR type | First review |
|---|---|
| Typo / link fix | Next business day |
| Content improvement | 3 business days |
| New page / template | 5 business days |
| Architectural change | 10 business days |

CODEOWNERS auto-assigns reviewers. See [`CODEOWNERS`](https://github.com/NikoMix/specialization-agentic-devops/blob/main/CODEOWNERS).

## Evidence handling

When porting a lesson learned, anonymise:

- Replace customer name with `Customer A`, `Customer B`, etc.
- Strip URLs, account IDs, subscription IDs, tenant IDs.
- Remove screenshots that contain identifying chrome.
- Never check in customer source code, customer telemetry, or secrets.

If in doubt, **don't** check it in — open an issue describing the lesson abstractly and discuss in the issue thread.

## Local development

The site is built with [Hugo](https://gohugo.io/) **extended** v0.165.0 or newer, using the [`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme) theme, which is pinned as a git submodule under `themes/`.

Clone with the submodule, or initialise it afterwards:

```powershell
git clone --recurse-submodules https://github.com/NikoMix/specialization-agentic-devops.git
# or, in an existing clone
git submodule update --init --recursive
```

Serve the site locally:

```powershell
hugo server
```

Then open <http://localhost:1313/specialization-agentic-devops/>.

Build locally before opening a PR — this is the same command CI runs:

```powershell
hugo --minify --gc
python .github/scripts/verify_tables.py
```

{{% alert type="caution" title="Authoring gotchas" %}}
Read `.github/memories/hugo-content.md` before authoring new pages. It captures
the table formatting rules, the shortcodes this theme provides, and the download
link pattern.

The single most important rule: **never indent a Markdown table.** A table
indented by four or more spaces becomes a code block, and one indented inside a
shortcode stops being a table at all. Tables always start at column 0.
{{% /alert %}}
