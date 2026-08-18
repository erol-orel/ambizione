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

## You need to cut ~1,500 characters

The plan is **~61,500 against an assumed 60,000**. I stopped compressing rather than keep
degrading the prose — the document now contains more good material than the format allows, and
choosing what leaves is the remaining editorial act. **Verify the real limit first**; if it is
genuinely 60,000, the three cuts marked ★ clear it with the least loss.

| Cut | Saves | Damage |
| --- | --- | --- |
| ★ §1.1 — compress the forecast-hub detail to two sentences | ~500 | Low. The hubs matter as context, not as argument |
| ★ §6.2 — turn the commitments table into prose | ~500 | Low. The content survives; only the layout goes |
| ★ §2.3 — compress the Swiss outbreak-modelling paragraph | ~400 | Low. The *F1000Research* point is what carries it |
| §4 T2.6 — fold the conformal layer into T2.2 as one sentence | ~450 | Moderate. It is the safety net for H3b |
| §4 T4.3 — drop the equity audit | ~700 | Moderate. The SNSF assesses this dimension explicitly |
| §3 — drop the heatwave archetype to extension status | ~600 | High. Weakens the generalisability claim to a single core archetype |

Do **not** cut: the T2.1 identifiability risk, the WP3 data fallback, the §5 delimitation table,
or the simulation-as-prior paragraph in WP2. Each pre-empts a specific objection that would
otherwise arrive unanswered.

## Open decisions blocking completion

1. **Host unit** — §6 is drafted for Teodoro's group with an HUG collaboration. Confirm or
   overturn; if the institution changes, §5 and the mobility statement change too.
2. **Data agreements** — HUG ED, 144/CASU, ICU occupancy. §4 and §6 assume these; the fallback
   design is written into WP3 but the primary version needs them.
3. **Third archetype** — is Legionella in or out? Currently written as in, scoped as an extension.
4. **PhD student vs postdoc** — drives the budget and the WP staffing lines.
