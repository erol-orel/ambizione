# Research plan — draft v0.2

Assemble in this order. The **2026 SNSF Ambizione guidelines (version 11.08.2026)** require a maximum of **15 A4 pages and 60,000 characters including spaces**; the mySNF character counter is binding. The bibliography is excluded. Minimum 10-point font and 1.5 line spacing apply, and the research plan must be one PDF without annexes. Tables, illustrations and formulae count toward the character limit.

The files follow the **structure prescribed by Guidelines 4.3** — the section numbers are the
SNSF's, not ours:

| File | SNSF section | Status |
| --- | --- | --- |
| `00-title-and-summary.md` | Title + **1. Summary** (max 1 page — check in the rendered PDF, the cap is a page, not a character count) | Revised |
| `01-state-of-the-art.md` | **2.1** Current state of research in the field | Revised; citation verification still required |
| `02-own-work.md` | **2.2** Current state of personal research and required competences | Revised |
| `03-objectives.md` | **2.3.1** Objectives and hypotheses | Revised; H3a central |
| `04-workplan.md` | **2.3.2** Work packages and methods | Revised; PI-led, no doctoral/postdoctoral staffing |
| `05-environment-team-resources.md` | **2.3.3** Research environment, team and resources | Revised |
| `06-schedule-milestones.md` | **2.4** Schedule and milestones | Split out as required |
| `07-relevance-impact-career.md` | **2.5** Relevance and impact + **2.6** Personal career development | Revised |
| `99-bibliography.md` | **3.** Bibliography | Excluded from the character/page maximum; no "et al.", DOIs, no links |
| `figures/` | Figures 1–2 | Regenerate from the committed generator before submission |

## Conventions

- `[[…]]` marks something only the applicant can supply — a name, date, number, decision or confirmation.
- `[VERIFY]` marks a factual claim requiring final external verification.
- Bibliographic references must be checked against the publisher record before submission.

## Current scientific architecture

The proposal has one central scientific question: **can published quantitative evidence provide useful information when local outcome data are insufficient at crisis onset, and can harmful borrowing be detected early?**

H1 is methodological validation; C2 is a model-adequacy criterion; **H3a is the central hypothesis**; H3b is robustness; H3c is a secondary information channel; H4 concerns decision value. Exactly one comparison is confirmatory: rung 4 versus rung 3 on CRPS skill score over the pre-specified cold-start window, **on respiratory episodes**; the heat domain repeats it as a sequential generalisation test, run only if the respiratory test is met.

EVT, resilience indicators and conformal calibration are supporting machinery, not separate headline contributions.

## Budget constraint

The 2026 Ambizione regulations cap project funds at **CHF 250,000 over four years** and do **not** permit doctoral students or postdocs to be employed through Ambizione. The plan therefore requests no doctoral/postdoctoral position; any personnel support must be eligible other-employee support and must be bounded and justified.

## Remaining load-bearing decisions

1. Real-time onset rule; cold-start window `[[N]]`, horizons and `[[Δ]]` follow the **episode
   inventory** (build it first — template in `05-review/applicant-facts.md`).
2. H1 benchmark sample size and variance-ratio threshold.
3. C2 recovery/calibration thresholds and H3c secondary criterion.
4. Host confirmation (two signatures: contact person + head of institute — see
   `04-other-documents/host-institution-letters.md`), data-access agreements, computing.
5. Final eligible project budget (`04-other-documents/budget.md` carries the verified rules).
6. Novelty audit and citation verification (full author lists, DOIs).
7. Fill the `[[…]]` placeholders — the counter excludes them, so **every fill needs an offsetting
   cut**; reserve is ~0. Cut candidates: §2.1.3, §2.3.2 T4.2, the §2.6 Institute paragraph.

## Build

Regenerate both artefacts from their committed sources before submission:

```sh
python3 03-research-plan/draft/figures/make_figures.py
sh 03-research-plan/draft/assemble.sh
```

Then verify idempotence by running both commands a second time and confirming no tracked diff remains. The final character count must be checked in **mySNF**, because that counter is binding.
