# Step 0 — the evaluation set

Pre-filled from your own GESICA data inventory (`00-source-documents/my-materials/
gesica-disease-model-source-table.xlsx`, sheet `Sources_donnees_GE_VD`). Much of questions A and B
was already answered there. Only the cells marked `[[…]]` genuinely need someone else to tell you.

---

## The finding that changes the design

**At daily resolution, every candidate primary outcome requires HUG. Every open source is weekly.**

| Source | Granularity | Access |
| --- | --- | --- |
| 144/CASU calls (D03) | **daily**, continuous, near real-time | Formal convention with HUG |
| ED presentations | **daily** `[[confirm]]` | HUG only — hospital statistics (D06) are **annual** and lag >1 year via OFS |
| ICU occupancy | `[[daily, confirm]]` | HUG only |
| Sentinella (D05) | **weekly** | Public |
| Mandatory notification (D04) | **weekly** | Public dashboard; individual data on request |
| Wastewater (D08) | weekly–daily, but **10 national stations since 2023** | Portal / request |
| MeteoSwiss (D10, D11) | **10 min – daily**, long history | Open |

This means the WP3 fallback is not merely "a narrower outcome claim" — it is **a coarser time
resolution**, and that interacts with every other design parameter. At weekly resolution, a 4-week
cold-start window is **four observations**, not twenty-eight, and a 14-day horizon is two steps.

**Consequence:** the fallback needs its own pre-specified horizon and window
(`[[weekly resolution; horizon 2–4 weeks; window 6–8 weeks]]`), declared alongside the primary
design rather than improvised if it triggers. Add this to the protocol.

It also sharpens the data request: **the daily granularity is the thing to secure**, and it has no
open substitute. Say so in the letters — it is a more precise ask than "retrospective extract".

---

## A. Data access status

| Dataset | Status | Historical coverage | Granularity | Source of truth |
| --- | --- | --- | --- | --- |
| HUG ED presentations | `[[requested]]` | `[[ask: from when?]]` | `[[daily?]]` | HUG |
| 144 / CASU calls | `[[requested]]` | From each centre's commissioning — *exact dates to verify with HUG* (per your D03 note) | Daily | HUG (GE) |
| ICU occupancy | `[[requested]]` | `[[ask]]` | `[[ask]]` | HUG |
| Mandatory notification | **Public** (aggregate) | Decades | Weekly | OFSP / cantonal doctor |
| Sentinella | **Public** | 1986; SARS-CoV-2/flu/RSV since week 40 of 2020 | Weekly | OFSP |
| Wastewater | Portal / request | Summer 2020; national programme reduced from 2023 | Weekly–daily | Eawag / OFSP |
| MeteoSwiss | **Open** | Long | 10 min – daily | MeteoSwiss |
| Legionellosis | **Granted** | Notifiable since 1998 | Case-level | BASEC 2026-00324 |

## B–C. Candidate episodes — provisional, for you to confirm

Not a blank table: this is my estimate from the record, to be corrected rather than composed.

**Respiratory — approximately 13–14 candidate episodes**

| Episode | Notes |
| --- | --- |
| COVID waves ×5 | spring 2020; autumn–winter 2020–21; Delta autumn 2021; Omicron winter 2021–22; 2022–23 |
| Influenza seasons ×8–9 | 2015–16 through 2019–20, then 2022–23 onward |
| 2020–21 and 2021–22 influenza | **Suppressed by NPIs — not usable as ordinary seasons.** Potentially valuable as negative controls: does the method correctly *not* raise an alarm? |

**Heat — approximately 6–9 candidate episodes**
2015, 2018, 2019 (two distinct events), 2022, 2023, plus `[[2017, 2024, 2025 — confirm against
MeteoSwiss heat-warning records]]`.

**Legionellosis — extension.** Annual notified cases since 1998, plus the 2017 Geneva outbreak.

**Provisional verdict:** respiratory clears the warning threshold comfortably; **heat is the
marginal archetype** and may drive the power calculation. Worth knowing before the simulation.

## D. Episode qualification criteria — fix these before counting

An episode qualifies only if it has:

- [ ] the primary outcome series available **before, during and after** onset;
- [ ] enough pre-onset history for the rolling baseline that defines onset;
- [ ] a consistent case/presentation definition across the period `[[coding changes? triage system changes?]]`;
- [ ] no overlap with an adjacent episode that would break the block structure;
- [ ] documented completeness through the window.

---

## Two statistical points for the simulation

**1. Episodes are less independent than they look — and the design already partly fixes it.**
If the same evidence-derived prior is applied to every episode, the episodes share a common error
source: prior misspecification. Testing across ten episodes then partly means testing one prior ten
times, and the effective sample size for H3a is smaller than the episode count suggests.

The rolling-origin rule that admits **only literature published before each origin** is not merely
realism — it is what makes the priors genuinely differ across episodes and moves them closer to
independence. Worth stating in the plan as a design property rather than only as a fidelity
constraint, because a statistical referee will otherwise raise the correlation and not see the
answer.

**2. Count the two archetypes separately.** They now have separate primary horizons, so they are
separate confirmatory analyses with separate power. Pooling them into one episode count would
hide that heat is the weaker arm.

---

## What only you can supply

1. Whether HUG can provide **daily** ED presentations, and from what year.
2. The 144/CASU commissioning dates — your own inventory flags these as to be verified.
3. Whether ICU occupancy exists at daily resolution and is a demand signal rather than a
   reflection of capacity policy.
4. Whether case and presentation definitions are stable across the candidate period.

Everything else above is either already answered in your GESICA inventory or estimable from the
public record.
