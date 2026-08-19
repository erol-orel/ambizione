# Research plan — draft v0.1

Assemble in this order. Page budget assumes **15 pages / 60,000 characters** excluding
bibliography — `[VERIFY]` against the Call 2026 guidelines before drafting to length.

| File | Section | Budget | Status |
| --- | --- | --- | --- |
| `00-title-and-summary.md` | Title, summary | 0.5 pp | Draft |
| `01-state-of-the-art.md` | Current state of research in the field | 2.5 pp | Draft — **references located and cross-checked, not yet verified against the articles** |
| `02-own-work.md` | Current state of my own research | 1.5 pp | Draft |
| `03-objectives.md` | Objectives and hypotheses | 1.0 pp | Draft |
| `04-workplan.md` | Detailed research plan | 7.5 pp | Draft — expanded; needs the Gantt figure |
| `05-impact-independence.md` | Relevance, impact, independence | 1.0 pp | Draft |
| `06-feasibility.md` | Feasibility, environment, resources | 0.5–1.0 pp | Draft — **written under an assumed host; confirm or overturn** |
| `99-bibliography.md` | Bibliography | excluded | Verified; **one author list outstanding** (the *Public Health* 2024 EMS/ILI paper) |
| `figures/` | Figure 1 (framework) and Figure 2 (Gantt) | — | Drawn; regenerate with `python3 figures/make_figures.py` |

## Conventions in the draft

- `[[…]]` marks something only you can supply — a name, a date, a number, a decision.
- `[VERIFY]` marks a factual claim I could not check from this environment.
- Citations are placeholders. **I have not invented references.** Where I cite, it is to
  well-established methodological work I am confident exists; every one still needs checking
  against the actual paper before submission, and the substantive epidemiological claims need
  references you supply from your own reading. See the warning in `99-bibliography.md`.

## Working title

> **COLDSTART — Evidence-informed forecasting of health-system crises when local data are scarce**

Alternatives if the acronym grates:
- *Forecasting health-system crises before the data arrive: evidence-derived priors, regime
  switching, and decision-relevant early warning*
- *From published evidence to actionable early warning: quantifying when synthesised literature
  improves crisis forecasting*

## Length

**51,569 characters against an assumed 60,000 — about 8,400 in reserve**, before figures. The
restructure in PR #1 replaced compression with subordination: one falsifiable question, with the
extreme-value, resilience and conformal components as supporting machinery rather than separate
claims. Verify the real limit against the call document; there is now room for the `[[…]]` content
you still have to supply.

Run `sh wordcount.sh` after edits, and rebuild both artefacts before submission:

```sh
python3 03-research-plan/draft/figures/make_figures.py   # figures
sh 03-research-plan/draft/assemble.sh                    # FINAL-research-plan.md
```

## Open decisions blocking completion

1. **Host unit** — §6 is drafted for Teodoro's group with an HUG collaboration. Confirm or
   overturn; if the institution changes, §5 and the mobility statement change too.
2. **Data agreements** — HUG ED, 144/CASU, ICU occupancy. §4 and §6 assume these; the fallback
   design is written into WP3 but the primary version needs them.
3. **Third archetype** — is Legionella in or out? Currently written as in, scoped as an extension.
4. **PhD student vs postdoc** — drives the budget and the WP staffing lines.
