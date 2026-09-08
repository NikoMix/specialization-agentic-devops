## Summary

<!-- One or two sentences describing the change. -->

## Engagement phase

- [ ] Qualify (offering one-pager, questionnaire)
- [ ] Discover (workshop, WAF assessment, MAP inputs)
- [ ] Design (reference architectures, HLD, LLD)
- [ ] Deliver (runbook, KT plan)
- [ ] Hypercare (hypercare plan, retro)
- [ ] Innersource / governance only

## Audit control(s) touched

<!-- List A.x.y and/or B.x.y; "none" if this PR does not touch audit content. -->

## Innersource lifecycle

- [ ] Draft (new content, not yet engagement-validated)
- [ ] Reviewed (peer-reviewed, ready for first engagement)
- [ ] Endorsed (used on ≥ 1 paid engagement, lessons learned applied)
- [ ] Deprecated

## Checklist

- [ ] `hugo --minify --gc` passes locally with no broken-link warnings
- [ ] `python .github/scripts/verify_tables.py` passes
- [ ] No real customer names, contract values, or identifiable engagement detail in this PR
- [ ] If evidence requirements changed, `.github/scripts/create-issues.sh` updated to match
- [ ] If a Module A/B control page changed, the matching entry in `content/docs/evidence-tracker.md` still aligns
- [ ] Linked issue: closes #
