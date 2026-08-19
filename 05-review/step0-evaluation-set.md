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

## What the updated GESICA inventory settles

The revised report and table (RSV added; twenty respiratory diseases in five priority tiers)
answer several open cells and change one recommendation.

**144/CASU is the best-characterised candidate outcome — by some distance.**

- Geneva's CASU-144 is operated by **HUG**: **>165,000 calls/year, ~71,000 of them emergency
  calls** — roughly **195 emergency calls per day**. That is ample volume for daily count
  modelling, and it is a documented figure rather than an assumption.
- Records carry date and time, age, sex, intervention type, unit engaged, **call reason**,
  medical history, **EST urgency level** and destination facility. The urgency scale allows
  severity stratification; the call reason carries the syndromic signal.
- Single institutional interlocutor (HUG for Geneva), which the report notes simplifies access.
- Your report's stated limitation — *"probablement plus adaptées à la prédiction de la demande
  ambulancière qu'à l'incidence globale de la maladie"* — **is not a limitation for this project.**
  The outcome here is demand, not incidence. The report is saying 144 data are well suited to
  exactly what COLDSTART forecasts.

**ED presentations, by contrast, appear nowhere in the inventory as a source.** Hospital
statistics (D06) are annual with >1 year lag via the OFS. That is not proof that daily ED data
cannot be obtained from HUG — only that it is undocumented, while 144 is documented and
quantified.

### Recommendation changed: make 144 emergency call volume the primary outcome

I previously recommended ED presentations. The evidence in your own inventory reverses that:

| | 144 calls | ED presentations |
| --- | --- | --- |
| Daily granularity | **Documented** | Undocumented `[[verify with HUG]]` |
| Volume | ~195 emergency calls/day | `[[unknown]]` |
| History | From centre commissioning `[[verify]]` | `[[unknown]]` |
| Suited to demand forecasting | **Stated in your report** | Yes |
| Decision relevance | Ambulance staffing and dispatch — a decision WP4 already covers | Bed capacity |
| Interlocutor | HUG (single) | HUG |

My earlier argument — that the primary outcome should be the one the decision layer acts on —
still holds, but it does not select ED over 144: **T4.1 elicits from dispatch supervisors as well
as capacity managers**, and ambulance redistribution is explicitly among the decisions the plan
addresses.

So: **144/CASU emergency call volume primary; ED presentations as the pre-declared substitute.**
Revisit only if HUG confirms daily ED data with long history, since ED sits one step closer to
bed capacity.

### One outcome series can serve both archetypes

Section 1.2 of the revised report is more useful than it looks. Non-infectious respiratory
conditions — asthma and COPD exacerbations driven by pollution peaks and heat — do not transmit
and fit no epidemic model, **but they contribute to the same respiratory care demand the model
predicts**.

That means a single outcome — respiratory-related emergency demand — carries **both** the
respiratory-epidemic and the heatwave archetype, with different drivers acting on the same series.
The generalisation test becomes cleaner: same outcome, same metric, different mechanism. Say this
explicitly in §3; it removes the objection that the two archetypes are being compared on
incommensurable outcomes.

### Episode counting depends on how the outcome is defined

Priority 1 groups **COVID-19, influenza and RSV** as the only three diseases with simultaneous
weekly sentinel surveillance, wastewater monitoring and near-real-time emergency signals.

If the outcome is **all-cause respiratory demand**, co-circulating pathogens collapse into one
episode: a winter with both influenza and RSV is one demand surge, not two. Episodes are then
roughly *distinct demand surges*, not *pathogen-seasons* — which lowers the count relative to my
earlier estimate but keeps each episode genuinely independent.

If the outcome were **pathogen-specific confirmed cases**, the count would rise but the outcome
would stop being the decision-relevant demand measure.

**Choose demand, accept the lower count, and say why.** A referee who spots pathogen-seasons being
counted as independent episodes when they overlap in time will not be gentle.

## A. Data access status

| Dataset | Status | Historical coverage | Granularity | Source of truth |
| --- | --- | --- | --- | --- |
| HUG ED presentations | `[[requested]]` | `[[ask: from when?]]` | `[[daily?]]` | HUG |
| **144 / CASU calls** | `[[requested]]` | From centre commissioning — *dates to verify with HUG* | **Daily; ~195 emergency calls/day** | HUG (GE) — single interlocutor |
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

1. The 144/CASU **commissioning date and the start of usable electronic records** — this now sets
   the length of the primary series and therefore the episode count.
2. Whether HUG can also provide **daily** ED presentations, and from what year — needed for the
   substitute outcome, and to decide whether the primary should be revisited.
3. Whether ICU occupancy exists at daily resolution and is a demand signal rather than a
   reflection of capacity policy.
4. Whether case and presentation definitions are stable across the candidate period.

Everything else above is either already answered in your GESICA inventory or estimable from the
public record.
