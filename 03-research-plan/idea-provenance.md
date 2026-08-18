# Where the additions came from, and what I left out

## From AURORA (Wellcome Discovery draft)

Three ideas transferred. One of them materially upgrades the project.

**1. Early-warning signals from ecosystem regime shifts → critical slowing down (AURORA Obj. 4).**
This is the significant one. AURORA asks whether changes in ecosystem stability provide
early-warning signals before conventional surveillance detects emergence. The underlying theory —
**critical slowing down** — is about systems approaching a critical transition losing resilience,
so variance and lag-1 autocorrelation of their fluctuations rise *beforehand* [Scheffer 2009], and
it has been developed specifically for epidemic transitions [O'Regan 2013; Brett 2018;
Southall 2021].

Applied here it does something the original framing did not: **resilience indicators are computed
from short windows of recent data**, so they carry information at crisis onset by a route entirely
independent of the literature priors. The project now has *two* answers to the cold-start problem —
one evidence-derived, one theory-derived — and a new hypothesis (H3c) asking whether they are
complementary or redundant. Structurally, the indicators enter as theoretically motivated
covariates on the regime-transition intensities, which also makes the state model mechanistically
grounded rather than purely statistical. Added as T2.5.

**2. Counterfactual intelligence (AURORA Obj. 7).** "Can predictive and causal inference be
combined to generate counterfactual scenarios?" Became **T4.6**: had escalation been triggered
when the model signalled rather than when it actually occurred, what would have changed? This is
stress testing in the sense used in quantitative finance, and it converts an abstract skill
improvement into bed-days and diverted transports — a quantity a hospital director recognises.

**3. Equity and bias.** AURORA's structural-determinants framing, reinforced by the systematic
review, became **T4.5**: an equity audit of forecast skill and elicited thresholds across strata.
The SNSF assesses this dimension, and it is substantively right — a system well calibrated on
average and poorly calibrated for one group is not deployable.

## From your own systematic review (Edjinedja, Larribau, Orel et al. 2026)

I had only read its first two pages. Reading it properly yielded four things, and it is now cited
three times in the plan — self-citation doing real work rather than decoration.

**1. A measured gap.** §7.3 reports that across 138 studies, explicit treatment of uncertainty,
transparency and explainability remains infrequent, though the field regards these as
preconditions for adoption. **This is published evidence, from your own review, for the gap this
proposal fills** — much stronger than asserting it. Now in §1.5.

**2. Hard numbers on data incompleteness.** §7.2: completeness averaging 52.3% for triage records,
70.3% for care reports, 57.3% for emergency forms, with some variables missing in >90% of records.
This changed the work plan rather than decorating it. T3.1 now treats missingness as a modelled
quantity, and it is a second independent justification for requesting **daily aggregates** rather
than record-level data — which also makes the data request easier to grant.

**3. Support for the decision framing.** §7.5 finds forecasting the most prevalent AI task in
prehospital knowledge acquisition, driven by "What will happen next?" and *"What actions are
needed to achieve a desired outcome?"* — the second is a counterfactual question, and it is
evidence that T4.6 answers something practitioners actually ask.

**4. Algorithmic bias** (§7.2) — fed into T4.5 as above.

## What I deliberately did not take

**Agentic AI and Model Context Protocol orchestration (review §7.6).** Genuinely interesting, and
you will be tempted, so here is the argument against putting it in this proposal:

- It is **engineering, not a scientific question.** A multi-agent architecture is a way of
  building something, not a claim that can be falsified.
- It pulls hard toward **the tool framing** this whole application was restructured to avoid. You
  have already built the platform; proposing to re-architect it is proposing your own past work
  plus fashion.
- It **dates badly**. A four-year plan whose distinctiveness rests on a 2026 orchestration
  protocol will read as naive by the mid-term review, and referees know it.
- It **overlaps** with the Horizon consortium's conversational-assistant work, which is exactly
  the overlap §5 argues does not exist.

If it turns out to matter, it belongs in the implementation of T2.7, unremarked.

**Adversarial robustness (review §7.7)** — real, but a different project.

**Global South / multi-country scope (AURORA).** Right for a Wellcome Discovery consortium,
wrong for CHF 250k and one doctoral researcher. The archetype-contrast design already delivers a
generalisability claim at a scale you can actually deliver.

## The tension you should be aware of

You asked for the most complete and ambitious version. The plan is now at **~60,000 characters —
100% of the assumed limit** — and carries four work packages with 20 tasks.

That is a real risk, and I want it on the record: **over-ambition is the most common reason
Ambizione applications fail on feasibility.** What protects this version is that every addition is
an *analysis of data already being collected*, not new data, new people or new fieldwork:
resilience indicators are statistics on existing series; conformal calibration is a wrapper;
the equity audit and counterfactuals are analyses of results WP3 already produces. Nothing added
here increases the budget.

Say that explicitly in §4 if you have room, because a referee counting tasks will wonder.
