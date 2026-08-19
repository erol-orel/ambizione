# Research plan — draft v0.2

Assemble in this order. The **2026 SNSF Ambizione guidelines (version 11.08.2026)** require a maximum of **15 A4 pages and 60,000 characters including spaces**; the mySNF character counter is binding. The bibliography is excluded. Minimum 10-point font and 1.5 line spacing apply, and the research plan must be one PDF without annexes. Tables, illustrations and formulae count toward the character limit.

| File | Section | Status |
| --- | --- | --- |
| `00-title-and-summary.md` | Title, summary | Revised |
| `01-state-of-the-art.md` | Current state of research in the field | Revised; citation verification still required |
| `02-own-work.md` | Current state of my own research | Revised |
| `03-objectives.md` | Objectives and hypotheses | Revised; H3a is the central hypothesis |
| `04-workplan.md` | Detailed research plan | Revised; PI-led, no doctoral/postdoctoral staffing |
| `05-impact-independence.md` | Relevance, impact, independence | Revised |
| `06-feasibility.md` | Feasibility, environment, resources | Revised; 2026 budget/staffing rules reflected |
| `99-bibliography.md` | Bibliography | Excluded from character/page maximum |
| `figures/` | Framework and Gantt | Regenerate from committed generator before submission |

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

1. Primary outcome series and forecast horizon for H3a.
2. Real-time onset rule and cold-start window `[[N]]`.
3. H3b non-inferiority margin `[[Δ]]`.
4. H1 benchmark sample size and variance-ratio threshold.
5. C2 recovery/calibration thresholds and H3c secondary criterion.
6. Host, data-access, mobility and computing confirmations.
7. Final eligible project budget.
8. Novelty and citation verification.

## Build

Regenerate both artefacts from their committed sources before submission:

```sh
python3 03-research-plan/draft/figures/make_figures.py
sh 03-research-plan/draft/assemble.sh
```

Then verify idempotence by running both commands a second time and confirming no tracked diff remains. The final character count must be checked in **mySNF**, because that counter is binding.
