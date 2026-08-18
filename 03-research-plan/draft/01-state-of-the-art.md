# 1. Current state of research in the field

## 1.1 Forecasting health-system crises: strong in steady state, weak at onset

Anticipating surges in demand for emergency care is an established field with a mature toolkit.
Syndromic surveillance methods detect departures from an expected baseline — the Serfling
seasonal regression and the Farrington family of algorithms remain the operational standard in
European surveillance systems, valued for interpretability and specificity rather than for
forecasting skill. For quantitative prediction, seasonal ARIMA variants, Prophet-style
decomposition models and, where sufficient history exists, recurrent neural architectures are
routinely compared; ensembles of structurally different models consistently outperform their
best member, a finding robust enough that it now organises the field institutionally through
collaborative forecast hubs.

Two features of this literature matter here.

First, **prehospital data are a leading indicator**. Emergency call volumes and dispatch records
carry syndromic signal days ahead of laboratory-confirmed surveillance, because they capture
care-seeking before it is formalised into a notified case. `[[Add your specific references —
the AI-in-EMS systematic review you co-authored is the natural anchor, plus the SAMU/144 lead-time
literature.]]`

Second, and decisively for this proposal, **the performance of these methods is conditional on
history**. Data-adaptive models need years of observations to learn seasonality, weekday
structure and weather response. The published performance figures that motivate their operational
adoption are almost invariably obtained in that regime.

## 1.2 The cold-start problem

The regime in which forecasts matter most is the opposite one. At the onset of a novel or
displaced crisis — a new pathogen, an unprecedented heat event, a contamination incident — the
relevant local time series is short, unstable and possibly unrepresentative of what follows.
Decisions taken in those first weeks are consequential, expensive and difficult to reverse:
opening surge capacity, cancelling elective activity, redistributing ambulances, triggering
cantonal or national escalation.

The early COVID-19 period demonstrated this at scale. Forecasts produced in the first months
were poor, widely divergent, and nonetheless used, because nothing better was available.
`[[Cite the retrospective forecast-skill evaluations here — several groups have published
systematic assessments of early-pandemic forecast performance.]]` The subsequent improvement in
forecast quality tracked the accumulation of local data more closely than it tracked
methodological innovation, which is precisely the point: the field solved the easy regime.

Existing responses to data scarcity are partial. Transfer learning and multi-region pooling
borrow strength from other locations, but require those locations to be observed contemporaneously
and comparably. Mechanistic compartmental models function with little data but demand parameter
values that must come from somewhere — and in practice are set by hand, from a small number of
familiar papers, with uncertainty asserted rather than derived. Scenario projection sidesteps
prediction altogether, which is defensible but leaves the operational question unanswered.

## 1.3 The unused resource: published evidence as quantitative prior information

What does exist at the onset of a crisis is the published record of analogous events. Effect
sizes for weather–demand associations, surge multipliers, transmission parameters, intervention
effects and length-of-stay distributions have been estimated many times, in many settings, and
reported in a literature that is large, indexed and machine-readable.

The statistical machinery for using such information is well developed. Informative priors
derived from previous studies are standard in Bayesian evidence synthesis; power priors,
commensurate priors and hierarchical borrowing formalise partial discounting of historical
information; meta-analytic-predictive approaches derive a prior for a new setting from a
random-effects synthesis of previous ones. Structured expert elicitation offers an alternative
route to the same object.

What is missing is the link between this machinery and the operational forecasting problem, and
it is missing for two substantive reasons rather than by oversight.

**Extraction.** Converting a corpus of publications into a set of quantitative estimates with
usable uncertainty is hard. Effect measures are reported inconsistently, populations and
exposure definitions differ, and reporting is selective. Automated extraction — increasingly
feasible with large language models, and central to the living systematic review movement — makes
the operation tractable at scale but introduces its own error, whose structure is not
characterised. The reliability of automated extraction has been studied for screening and for
categorical data items; for **quantitative parameters intended to serve as priors**, it has not.

**Transportability.** Even a perfectly extracted estimate may not transfer. The formal literature
on transportability and external validity establishes conditions under which an effect estimated
in one population identifies a quantity in another, and those conditions are demanding. A prior
built from studies conducted under different health systems, case definitions and policy regimes
may be not merely uninformative but actively misleading — and a confidently wrong prior in the
cold-start regime is worse than no prior at all, because it is most influential precisely when
local data cannot correct it.

**These two problems are the scientific content of this proposal.** They are usually treated as
implementation obstacles. They are better understood as the empirical question of whether
published evidence can be made to earn its place in operational forecasting.

## 1.4 Representing escalation: an inherited answer from another field

A second gap concerns what is being forecast. Operational early warning is not a point prediction
of a count; it is a judgement about **state** — whether the system is functioning normally, under
strain, or heading for failure. Practice typically produces this by thresholding a point forecast,
which discards the structure of the problem: escalation is persistent, transitions are abrupt,
and the same observed value carries different meaning depending on the trajectory it sits on.

**Markov regime-switching models** represent exactly this structure — a latent state process with
persistent regimes, state-dependent dynamics and estimable transition probabilities — and have
been the standard instrument for anticipating rare, costly transitions in econometrics and
quantitative finance since Hamilton's work in the late 1980s. **Extreme value theory** provides
the complementary apparatus for the tail: peaks-over-threshold and generalised Pareto methods
estimate the probability of exceedances beyond the observed range, which is what an "alarming"
state actually is.

Both are largely absent from health-system surge forecasting, despite the problem structure being
close to identical: rare, expensive, persistent adverse regimes, with severe asymmetry between the
cost of a missed escalation and the cost of a false alarm. Hidden Markov models appear
occasionally in disease-mapping and syndromic-surveillance work, and extreme value methods appear
in heat–mortality studies, but a regime-switching representation of health-system state, with an
extreme-value tail and evidence-derived priors, has not to my knowledge been developed or
evaluated. `[[Confirm this claim with a systematic search before submission — it is a strong claim
and a referee will test it. LiteRev is the obvious instrument.]]`

## 1.5 Evaluation: the gap between prediction and decision

Finally, the field evaluates itself against the wrong target. Forecasting studies overwhelmingly
report discrimination and error metrics — AUC, RMSE, MAE — which measure whether a model ranks or
approximates well, not whether acting on it produces better outcomes. Proper scoring rules
address part of this by rewarding calibrated probabilistic forecasts rather than accurate point
predictions. Decision-analytic evaluation addresses the rest: net benefit and decision-curve
methods weight errors by their actual consequences, and value-of-information analysis asks what
better prediction would be worth.

For rare adverse states this is not a refinement but a necessity. An alarming regime is by
construction infrequent; an accuracy-based criterion rewards a model that never raises the alarm,
and a threshold chosen to optimise AUC has no relationship to the point at which an emergency
service can and should act differently. That most operational forecasting tools are never adopted
is usually attributed to implementation barriers. A more parsimonious explanation is that they
were optimised for a quantity nobody needed.

## 1.6 The gap this project addresses

Bringing these threads together:

- Forecasting methods perform well where history is long and poorly where decisions are urgent.
- A large body of relevant quantitative evidence exists but is not used as prior information,
  because extraction is unreliable in uncharacterised ways and transportability is unestablished.
- The operational target — escalation state — has a natural representation, developed in another
  field, that has not been applied here.
- Evaluation conventions measure something other than usefulness.

**No study has tested whether evidence derived systematically from the published literature
improves health-crisis forecasting in the cold-start regime, using proper scoring rules and
decision-analytic evaluation, in a real health system.** That is the question this project
answers, and it is answerable now because the extraction infrastructure exists — I built it.
