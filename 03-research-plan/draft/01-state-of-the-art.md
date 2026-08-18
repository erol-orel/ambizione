# 1. Current state of research in the field

## 1.1 Forecasting health-system crises: strong in steady state, weak at onset

Anticipating surges in demand for emergency care is an established field with a mature toolkit.
Syndromic surveillance methods detect departures from an expected baseline: the Farrington
quasi-Poisson framework [Farrington 1996] and its reweighted "Flexible" extension
[Noufaily 2013] remain the operational standard across European public health institutions,
valued for interpretability and specificity across heterogeneous series without per-series
tuning. For quantitative prediction, seasonal ARIMA variants, decomposition models and — where
sufficient history exists — recurrent architectures are routinely compared, and ensembles of
structurally different models consistently outperform their best member. That finding is robust
enough to have organised the field institutionally: the US COVID-19 Forecast Hub aggregated
submissions from more than 90 groups, and its ensemble was the most consistently accurate
probabilistic forecaster of incident deaths over eighteen months [Cramer 2022], with the European
hub reproducing the pattern across 32 countries [Sherratt 2023].

Two features of this literature matter here.

First, **prehospital data are a leading indicator**. Emergency medical dispatch and ambulance
records carry syndromic signal ahead of laboratory-confirmed surveillance, because they capture
care-seeking before it is formalised into a notified case. A three-region European comparison of
dispatch, ambulance and emergency department data identified the onset of the 2009 A(H1N1)
autumn/winter wave eight days in advance [Rosenkötter 2013], and a ten-year series of emergency
telephone calls has been shown to track influenza-like illness incidence [Bonora 2024]. Our own
systematic review of artificial intelligence in emergency medical services for disasters and
health emergencies maps this literature and its methodological limits [Edjinedja 2026].

Second, and decisively for this proposal, **the performance of these methods is conditional on
history**. Data-adaptive models require years of observations to learn seasonality, weekday
structure and weather response. Even the Farrington family — deliberately robust — is known to
degrade when historical baselines are short, which is the recognised difficulty in applying it to
emerging diseases. The published performance figures that motivate operational adoption are
almost invariably obtained in the data-rich regime.

## 1.2 The cold-start problem

The regime in which forecasts matter most is the opposite one. At the onset of a novel or
displaced crisis — a new pathogen, an unprecedented heat event, a contamination incident — the
relevant local series is short, unstable and possibly unrepresentative of what follows. Decisions
taken in those first weeks are consequential, expensive and hard to reverse: opening surge
capacity, cancelling elective activity, redistributing ambulances, triggering cantonal escalation.

The early COVID-19 period demonstrated this at scale. Forecast quality improved through the
pandemic [Cramer 2022], and that improvement tracked the accumulation of local data at least as
closely as it tracked methodological innovation. The field, in effect, solved the easy regime.

Existing responses to data scarcity are partial. Transfer learning and multi-region pooling borrow
strength from other locations, but require those locations to be observed contemporaneously and
comparably. Mechanistic compartmental models function with little data but demand parameter
values that must come from somewhere — and in practice are set by hand, from a small number of
familiar papers, with uncertainty asserted rather than derived. Scenario projection sidesteps
prediction altogether, which is defensible but leaves the operational question unanswered.

## 1.3 The unused resource: published evidence as quantitative prior information

What does exist at the onset of a crisis is the published record of analogous events. Weather–
demand associations, surge multipliers, transmission parameters, intervention effects and
length-of-stay distributions have been estimated many times, in many settings, and reported in a
literature that is large, indexed and machine-readable.

The statistical machinery for using such information is well developed. Power priors discount
historical data by an explicit weight [Ibrahim 2000]; commensurate priors tie the discount to
agreement between sources [Hobbs 2011]; meta-analytic-predictive priors derive a prior for a new
setting from a random-effects synthesis of previous ones, with robust mixture variants that
protect against prior–data conflict [Schmidli 2014].

What is missing is the link between this machinery and operational forecasting, and it is missing
for two substantive reasons rather than by oversight.

**Extraction.** Converting a corpus into quantitative estimates with usable uncertainty is hard.
Effect measures are reported inconsistently, populations and exposure definitions differ, and
reporting is selective. Automated extraction with large language models makes the operation
tractable at scale, and a recent systematic review of this literature is directly informative
about its limits: accuracy ranges from 47% to 99.9% and is markedly worse for **numerical** items
(47–88%) than for categorical or string items (74–96%), with **omission** rather than fabrication
the dominant error mode (60–74% of errors, against hallucination rates of 0.08–6%)
[Ghersi 2026 — verify authorship]. This is the clearest available evidence that automated
extraction is weakest precisely on the quantities a prior needs. What has not been established is
the *structure* of that error when the extracted quantities are pooled: whether the resulting
distributions are merely noisy, or systematically too narrow.

**Transportability.** Even a perfectly extracted estimate may not transfer. The formal literature
establishes when an effect estimated in one population identifies a quantity in another, via
selection diagrams and do-calculus [Bareinboim 2016], via sampling-score reweighting in the
potential-outcomes tradition [Dahabreh 2019], and as reviewed comparatively by [Degtiar 2023].
The conditions are demanding. A prior built from studies conducted under different health systems,
case definitions and policy regimes may be not merely uninformative but actively misleading — and
a confidently wrong prior in the cold-start regime is worse than no prior, because it is most
influential exactly when local data cannot correct it.

**These two problems are the scientific content of this proposal.** They are usually treated as
implementation obstacles. They are better understood as the empirical question of whether
published evidence can be made to earn its place in operational forecasting.

## 1.4 Representing escalation: latent regimes and tails

A second gap concerns what is being forecast. Operational early warning is not a point prediction
of a count; it is a judgement about **state** — whether the system is functioning normally, under
strain, or heading for failure. Practice typically produces this by thresholding a point forecast,
which discards the structure of the problem: escalation is persistent, transitions are abrupt, and
the same observed value means different things on different trajectories.

Latent-state representations are not new to surveillance. Le Strat and Carrat introduced Poisson
hidden Markov models for epidemic surveillance, with states interpreted as epidemic and
non-epidemic periods [Le Strat 1999]; the approach has been developed since [Watkins 2009] and is
implemented in the standard `surveillance` package. At low false-alarm rates, HMM-based detection
compares favourably with CUSUM alternatives. Extreme value methods likewise have a foothold:
peaks-over-threshold and generalised Pareto approximation of exceedances [Coles 2001] have been
applied to seasonal viruses and hospital congestion in a Swiss hospital [Minkoff 2020 — verify].

**The claim here is therefore narrower and stronger than "these methods are absent".** What
exists is two-state epidemic/non-epidemic detection on a single surveillance series, and separate
extreme-value description of congestion. What does not exist is the object this project builds:
a **multi-regime, ordinally interpretable state process for health-system capacity**, estimated
jointly across dispatch, emergency and intensive care series, with **covariate-dependent
transition intensities**, an **extreme-value representation of the critical regime** coupled to
the state model, and **priors derived from the published literature**. The econometric tradition
that developed this apparatus for rare, costly, persistent regime transitions [Hamilton 1989] has
not been brought to bear on health-system surge in this form. `[[Confirm with a systematic search
before submission — a referee will test this sentence. LiteRev is the instrument; record the
search so it can be reported.]]`

## 1.5 Evaluation: the gap between prediction and decision

Finally, the field often evaluates itself against the wrong target. Forecasting studies
overwhelmingly report discrimination and error metrics — AUC, RMSE, MAE — which measure ranking
or approximation, not whether acting on the forecast produces better outcomes. Proper scoring
rules address part of this by rewarding calibrated predictive distributions rather than accurate
point predictions, and are minimised uniquely by the true predictive distribution
[Gneiting 2007]. Decision-analytic evaluation addresses the rest: net benefit weights errors by
their consequences at an explicit decision threshold [Vickers 2006], and value-of-information
analysis asks what better prediction would be worth.

For rare adverse states this is not a refinement but a necessity. An alarming regime is by
construction infrequent; an accuracy-based criterion rewards a model that never raises the alarm,
and a threshold chosen to optimise AUC bears no relation to the point at which an emergency
service can and should act differently. That most operational forecasting tools are never adopted
is usually attributed to implementation barriers. A more parsimonious explanation is that they
were optimised for a quantity nobody needed.

## 1.6 The gap this project addresses

- Forecasting methods perform well where history is long and poorly where decisions are urgent.
- A large body of relevant quantitative evidence exists but is not used as prior information,
  because automated extraction is weakest exactly on numerical quantities and its pooled error
  structure is uncharacterised, and because transportability is unestablished.
- The operational target — escalation state — has latent-regime and extreme-value
  representations in partial forms, but not in the coupled, multi-regime, prior-informed form the
  problem requires.
- Evaluation conventions measure something other than usefulness.

**No study has tested whether evidence derived systematically from the published literature
improves health-crisis forecasting in the cold-start regime, using proper scoring rules and
decision-analytic evaluation, in a real health system.** That is the question this project
answers, and it is answerable now because the extraction infrastructure exists — I built it.
