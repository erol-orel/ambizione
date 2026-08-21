# SNSF Ambizione application workspace

Working repository for an application to the Swiss National Science Foundation
[Ambizione](https://www.snf.ch/en/N18L3oGWomTSSGkF/funding/careers/ambizione) scheme.

**Target deadline: 3 November 2026, 17:00 CET** — the final Ambizione call.

## How this repo is organised

| Folder | Contents |
| --- | --- |
| `00-source-documents/` | Official call documents (Guidelines, Regulations, confirmation template — read in full) and the applicant's own materials |
| `01-call/` | Current call requirements, evaluation criteria, documents and timeline |
| `02-profile/` | Applicant profile and career information |
| `03-research-plan/` | Research plan sources, drafts and generated artefacts |
| `04-other-documents/` | Mobility statement, CV narratives, host/data-access materials, correspondence and budget |
| `05-review/` | Hypothesis audit, self-assessment and reviewer-simulation notes |

## Where to start

| | |
| --- | --- |
| **What to do next** | `TODO.md` — ordered by dependencies and blocking decisions |
| **The research plan** | `03-research-plan/FINAL-research-plan.md` (assembled; edit `draft/`, then `sh draft/assemble.sh`) |
| **Scheme rules** | `01-call/scheme-facts.md` |
| **Applicant profile** | `02-profile/erol-orel-profile.md` |
| **CV narratives + output list** | `04-other-documents/cv-narratives/` |
| **Statement of mobility** | `04-other-documents/statement-of-mobility-draft.md` |
| **Emails to send** | `04-other-documents/emails/` |
| **Data access package** | `04-other-documents/data-access/` |
| **Budget** | `04-other-documents/budget.md` |
| **Pre-submission checks** | `05-review/snsf-compliance-audit.md` (vs the call documents), `05-review/hypothesis-audit.md`, `05-review/self-assessment.md` |

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

## Sourcing and verification

The 2026 Ambizione call is now open. The official SNSF call page and current regulations are the
primary sources for scheme facts. Repository notes may contain working interpretations or earlier
call information; where a repository note is marked `[VERIFY]`, check it against the current
official Call 2026 documents before relying on it.

The binding submission limits are those reported by the SNSF Portal: the research plan may not
exceed 15 pages or 60,000 characters with spaces, whichever limit is reached first. The SNSF
notes that the portal count is binding and may vary slightly with document/PDF encoding.
