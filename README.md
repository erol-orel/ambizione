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

## Where to start

| | |
| --- | --- |
| **What to do next** | `TODO.md` — ordered by what blocks what |
| **The research plan** | `03-research-plan/FINAL-research-plan.md` (assembled; edit `draft/`, then `sh draft/assemble.sh`) |
| **Scheme rules** | `01-call/scheme-facts.md` |
| **Applicant profile** | `02-profile/erol-orel-profile.md` |
| **CV narratives + output list** | `04-other-documents/cv-narratives/` |
| **Statement of mobility** | `04-other-documents/statement-of-mobility-draft.md` |
| **Emails to send** | `04-other-documents/emails/` |
| **Data access package** | `04-other-documents/data-access/` |
| **Budget** | `04-other-documents/budget.md` |
| **Pre-submission checks** | `05-review/hypothesis-audit.md`, `05-review/self-assessment.md` |

Working notes kept for reference — the reasoning behind decisions already taken, useful if a
choice is revisited or at interview: `03-research-plan/why-cold-start.md`,
`idea-provenance.md`, `literature-to-strengthen.md`, `literev-evidence-assessment.md`.

## Rebuilding the generated artefacts

```sh
python3 03-research-plan/draft/figures/make_figures.py
sh 03-research-plan/draft/assemble.sh
```

Run both after editing any section file. `FINAL-research-plan.md` and the figures are generated —
never edit them directly.

## Important caveat on sourcing

This session could not reach `snf.ch` directly (blocked by the network egress policy),
so the facts in `01-call/` were reconstructed from search results and from Swiss university
grant-office pages. Every requirement is marked with a confidence level. **Anything marked
`[VERIFY]` must be checked against the official Call 2026 document and guidelines PDF before
you rely on it**, in particular page limits, character counts, and the exact document list,
which the SNSF changes between calls.
