# SNSF Ambizione application workspace

Working repository for an application to the Swiss National Science Foundation
[Ambizione](https://www.snf.ch/en/N18L3oGWomTSSGkF/funding/careers/ambizione) scheme.

**Target deadline: 3 November 2026** (the final Ambizione call — the scheme is being
discontinued and replaced from 2028).

## How this repo is organised

| Folder | Contents |
| --- | --- |
| `00-source-documents/` | Official call documents (to download) and the applicant's own materials |
| `01-call/` | What the call actually requires: facts, document list, evaluation criteria, timeline |
| `02-profile/` | Intake questionnaire — **fill this in first**, everything else is generated from it |
| `03-research-plan/` | The research plan: outline, page budget, and drafts |
| `04-other-documents/` | Statement of mobility, CV narratives, host-institution letter briefs, budget |
| `05-review/` | Self-assessment against the reviewers' scoring lens; reviewer-simulation notes |

## Order of work

0. Read `03-research-plan/candidate-projects.md` — the project-choice recommendation.
1. `02-profile/erol-orel-profile.md` is filled in from the CV; correct anything wrong.
2. Confirm eligibility against `01-call/eligibility-check.md` — do this before writing anything.
3. Lock the one-paragraph project pitch in `03-research-plan/00-core-idea.md`.
   Nothing else gets written until this is sharp.
4. Trigger the host-institution letters early (`04-other-documents/host-institution-letters.md`)
   — these have institutional lead times measured in weeks, not days.
5. Draft the research plan section by section against `03-research-plan/00-outline.md`.
6. Run `05-review/self-assessment.md` before submission.

## Important caveat on sourcing

This session could not reach `snf.ch` directly (blocked by the network egress policy),
so the facts in `01-call/` were reconstructed from search results and from Swiss university
grant-office pages. Every requirement is marked with a confidence level. **Anything marked
`[VERIFY]` must be checked against the official Call 2026 document and guidelines PDF before
you rely on it**, in particular page limits, character counts, and the exact document list,
which the SNSF changes between calls.
