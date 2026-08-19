# Applicant decisions — recommended answers

My position on each open decision, with reasoning. Where I differ from the review that produced
this list, it is marked **DIFFER**. Where something is missing, **ADDED**.

---

## The ordering problem

The list presents Steps 1–3 (primary outcome, horizon, cold-start window) as free scientific
choices and puts data access at Step 15. **That order cannot work.** You cannot choose "ED
presentations" as the primary outcome before knowing whether daily ED presentations are
obtainable at usable resolution and history. And N, the horizon and Δ are not three independent
intuitions — they are three outputs of one power calculation.

**Revised order:**

| | |
| --- | --- |
| **0** | **Data reality check.** What exists, at what resolution, over how many years, and — the missing decision — **how many historical episodes** the evaluation can include |
| **1** | Primary outcome, plus a **pre-declared substitute primary** if the first is refused |
| **2** | One simulation that jointly fixes horizon, N and Δ |
| **3** | Everything else in the original order |

**ADDED — the missing decision: how many episodes?** Power in this design comes from the number
of crisis episodes, not from the length of the cold-start window. It is not on the list and it
determines whether the whole confirmatory test is viable. Count them explicitly: influenza seasons
`[[~10 if data goes back to 2015]]`, COVID waves `[[4–6]]`, heat events `[[2015, 2018, 2019, 2022,
2023…]]`. If the total is under about ten, the design needs rethinking before anything else.

---

## Step 1 — Primary outcome: **A, ED presentations**

Agreed, for a reason the list does not state: **the primary outcome should be the one the decision
layer acts on.** Capacity escalation responds to presentations and occupancy, not to call volume.
If the primary outcome is not decision-relevant, the H4 link becomes an argument rather than a
measurement.

**ADDED — name the substitute primary now.** If ED data is refused, **144/CASU call volume**
becomes primary. Declare that in the proposal. Choosing the outcome after seeing which data
arrived is exactly the flexibility that destroys a confirmatory design, and pre-declaring the
substitute costs nothing.

ICU occupancy should not be primary: counts are small, events are rare, and it is the weakest
series for detecting a skill difference.

## Step 2 — Primary horizon: **14 days for the respiratory archetype — but not for heat**

**DIFFER.** 14 days is right for a respiratory epidemic and the reasoning holds. But **14-day
heat forecasts are beyond meteorological predictability**, so the same primary horizon cannot
serve both archetypes. A referee in environmental epidemiology will catch that immediately.

- Respiratory archetype: **14 days** primary; 7 and 28 secondary.
- Heat archetype: **`[[3–5 days]]`** primary, matching operational heat-warning lead times.

Two archetype-specific primary horizons, each declared in advance. This is not a loosening of the
design — it is the correct specification.

## Step 3 — Cold-start window: **provisionally 4 weeks, confirmed by simulation**

Agreed in value, but not as an intuition. **N = 4 weeks with a 14-day horizon yields roughly two
non-overlapping forecast origins per episode.** That is thin. It is defensible only if the episode
count from Step 0 is healthy.

Fix N in the same simulation that fixes Δ, and report the sensitivity analysis (1–2, 1–4, 1–6
weeks) as pre-planned rather than exploratory.

## Step 4 — Onset rule: **B, deviation from a prospectively estimated baseline**

Agreed, with a caveat the list misses. **A seasonal baseline requires history that a novel
pathogen does not have.** The retrospective evaluation includes COVID waves, which were novel at
the time, so the rule must degrade gracefully.

Use deviation from a **rolling baseline estimated only on data preceding the candidate onset**,
with a pre-specified exceedance duration (for example two consecutive days). This works for
recurrent hazards and for novel ones, and applies identically across archetypes — which matters,
because an onset rule that differs by archetype makes the generalisation claim untestable.

Not change-point detection: an optimised detector is itself a model fitted to the episode, and
defending it costs more than it earns.

## Step 5 — Δ: **derive from simulation. No number in the proposal.**

Fully agreed. The plan already says it will be fixed before evaluation; keep it that way.

## Step 6 — H1: **keep directional. Decided.**

Agreed without reservation. The directional claim is supported by the extraction evidence, has a
falsifiable remedy, and a retreat to "extraction may introduce errors" would be unfalsifiable.

## Step 7 — Benchmark size: **300, with a pre-specified extension rule**

Agreed. **ADDED:** write "300" rather than "300–500". A range reads as indecision; a number with a
stated rule for extension reads as design.

## Step 8 — Geneva data central: **yes, with the fallback cost stated**

Agreed. The open-data-only version is not an Ambizione-scale contribution, and the plan already
states plainly what the fallback would cost the primary outcome claim. Ambition plus a declared
floor is the right structure.

## Step 9 — Collaborator: **the arithmetic decides this**

At Swiss employer cost of roughly `[[CHF 100–120k]]` per FTE-year, **CHF 250,000 buys about two
FTE-years in total** — and that is the entire project budget, before computing, data, travel and
the mobility stay.

Realistic shapes:

| Option | Cost | Leaves for everything else |
| --- | --- | --- |
| 50% for 4 years | ~CHF 200–240k | almost nothing |
| **40–50% for 3–4 years** | **~CHF 150–190k** | **~CHF 60–100k** ← recommended |
| 100% for 2 years, concentrated M3–M30 | ~CHF 200–240k | almost nothing |

Recommend **~40–50% FTE across M3–M36**, spanning the WP1 extraction and WP3 pipeline work.
Profile: data scientist or research software engineer — Python/R, reproducible pipelines, health
data handling, ideally some NLP. Explicitly **not** a second scientific lead.

Confirm rates with the grants office before fixing the FTE; the arithmetic above is indicative.

## Step 10 — Independence sentence

> This project establishes my independent research programme at the intersection of **automated
> evidence synthesis**, **econometric modelling of rare transitions**, and **emergency public
> health** — a combination that follows from my own trajectory rather than from any group I have
> worked in.

The final clause is the one doing the work.

## Step 11 — What to be known for

Agreed, sharpened: **the person who established when published evidence can — and cannot —
substitute for missing local data in crisis forecasting.** The boundary condition is as much the
contribution as the positive result, and saying so protects against a null result reading as
failure.

`[[Steps 10 and 11 are one decision. Answer them together.]]`

## Step 12 — Two domains: **keep. No change.**

## Step 13 — WP4 scope

**DIFFER slightly.** Core: T4.1 elicitation and T4.2 decision-analytic evaluation **including the
equity audit** — it is cheap, it is folded into T4.2 already, and the SNSF assesses that
dimension. Conditional: T4.3 counterfactuals and T4.4 shadow mode.

## Step 14 — SHELF panel: **15–20, at least three operational roles**

Agreed. **ADDED:** name the units, if not the individuals, before submission. "n ≈ 15–20" with no
identified participants is a soft commitment a referee will discount.

## Steps 15–17 — data, CCER, budget

Agreed on substance; move to the front (see the ordering problem above). Every budget line should
name the work package it serves.

## Step 18 — Mobility: state the capability, not the institution

The answer to "what capability becomes available" is concrete: **extreme-value methodology for the
tail of the critical regime**, from the group that published the closest precedent on Swiss
hospital congestion. That capability is not present in the host environment. Say that.

## Steps 19–21 — host relationship, CV last, final hostile review

Agreed, no changes.

---

## What to do first

1. Count the episodes (Step 0). Everything downstream depends on it.
2. Send the data requests — already drafted in `04-other-documents/data-access/`.
3. Answer Steps 10/11 in your own words. They are yours and nobody can draft them for you.

Steps 2, 3 and 5 wait for the simulation. Do not guess them.
