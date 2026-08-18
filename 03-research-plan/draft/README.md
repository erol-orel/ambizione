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

## If you need to cut

The plan is **at 100% of the assumed 60,000-character limit**. If the real limit is lower, or the
SNSF counts differently, cut in this order — each item is genuinely severable:

1. **§4 T3.5 waterborne archetype** (~400 ch). Already scoped as an extension; the cleanest cut.
2. **§4 T4.3 value of information** (~350 ch). Elegant, but the least load-bearing task.
3. **§1.2 paragraph on partial existing responses** (~450 ch). Compress to one sentence.
4. **§6.4 preparatory work** (~700 ch). Move into the mobility statement or a cover note.
5. **§4 consolidated risk register** — keep the table, cut the R4 commentary (~400 ch).

Do **not** cut: the identifiability risk in T2.1, the WP3 data fallback, or the §5 delimitation
table. Each pre-empts a specific objection a referee will otherwise raise unanswered.

## Current length

**~60,600 characters against an assumed 60,000 limit — roughly 600 over**, and the counter here is
approximate (it strips markdown imperfectly). **Verify the real limit before cutting anything.**
If it is 60,000, one item from the cut list above clears it.
Run `sh wordcount.sh` after each edit. Both figures are drawn and linked from §3 and §4. They consume page budget rather than
characters, so check both limits when you typeset.

## Open decisions blocking completion

1. **Host unit** — §6 is drafted for Teodoro's group with an HUG collaboration. Confirm or
   overturn; if the institution changes, §5 and the mobility statement change too.
2. **Data agreements** — HUG ED, 144/CASU, ICU occupancy. §4 and §6 assume these; the fallback
   design is written into WP3 but the primary version needs them.
3. **Third archetype** — is Legionella in or out? Currently written as in, scoped as an extension.
4. **PhD student vs postdoc** — drives the budget and the WP staffing lines.
