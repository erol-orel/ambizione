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

Two features matter here. First, **prehospital data are a leading indicator**: dispatch and
ambulance records carry syndromic signal ahead of laboratory-confirmed surveillance, capturing
care-seeking before it becomes a notified case. A three-region European comparison identified the
onset of the 2009 A(H1N1) autumn wave eight days in advance [Rosenkötter 2013], and a ten-year
series of emergency calls tracks influenza-like illness incidence [EMS-ILI 2024]; our systematic
review maps this literature and its limits [Edjinedja 2026].

Second, and decisively, **performance is conditional on history**. Data-adaptive models need
years of observations to learn seasonality, weekday structure and weather response, and even the
deliberately robust Farrington family degrades when baselines are short — the recognised
difficulty in applying it to emerging diseases. The published figures that motivate operational
adoption are almost invariably obtained in the data-rich regime.

## 1.2 The cold-start problem

The regime in which forecasts matter most is the opposite one. At the onset of a novel or
displaced crisis — a new pathogen, an unprecedented heat event, a contamination incident — the
relevant local series is short, unstable and possibly unrepresentative of what follows. Decisions
taken in those first weeks are consequential, expensive and hard to reverse: opening surge
capacity, cancelling elective activity, redistributing ambulances, triggering cantonal escalation.

The early COVID-19 period demonstrated this at scale: forecast quality improved through the
pandemic [Cramer 2022], and that improvement tracked the accumulation of local data at least as
closely as methodological innovation. The field, in effect, solved the easy regime.

Existing responses are partial. Transfer learning and multi-region pooling require other locations
to be observed contemporaneously and comparably. Mechanistic models function with little data but
demand parameter values that in practice are set by hand, from a few familiar papers, with
uncertainty asserted rather than derived. Scenario projection sidesteps prediction altogether.

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
reporting is selective. Automated extraction with large language models makes this tractable
at scale, and a systematic review of that literature is directly informative about its limits —
accuracy ranges from 47% to 99.9%, markedly worse for **numerical** items (47–88%) than
categorical ones (74–96%), with **omission** rather than fabrication dominant (60–74% of errors,
against hallucination rates of 0.08–6%) [Shankar 2026]. Extraction is therefore weakest precisely
on the quantities a prior needs. What is unestablished is the *structure* of that error once
estimates are pooled: whether the distributions are merely noisy or systematically too narrow.

**Transportability.** Even a perfectly extracted estimate may not transfer. The formal literature
establishes when an effect estimated in one population identifies a quantity in another, via
selection diagrams and do-calculus [Bareinboim 2016], via sampling-score reweighting in the
potential-outcomes tradition [Dahabreh 2019], and as reviewed comparatively by [Degtiar 2023].
The conditions are demanding. A prior built from studies conducted under different health systems,
case definitions and policy regimes may be not merely uninformative but actively misleading — and
a confidently wrong prior in the cold-start regime is worse than no prior, because it is most
influential exactly when local data cannot correct it.

**These two problems are the scientific content of this proposal.** Usually treated as
implementation obstacles, they are better understood as the empirical question of whether
published evidence can earn its place in operational forecasting.

## 1.4 Representing escalation: latent regimes and tails

A second gap concerns what is being forecast. Operational early warning is not a point prediction
of a count; it is a judgement about **state** — whether the system is functioning normally, under
strain, or heading for failure. Practice typically produces this by thresholding a point forecast,
which discards the structure of the problem: escalation is persistent, transitions are abrupt, and
the same observed value means different things on different trajectories.

Latent-state representations are not new to surveillance: Le Strat and Carrat introduced Poisson
hidden Markov models with states interpreted as epidemic and non-epidemic periods [Le Strat 1999],
developed since [Watkins 2009] and implemented in the standard `surveillance` package, and at low
false-alarm rates HMM detection compares favourably with CUSUM alternatives. Extreme value methods likewise have a foothold, and the closest precedent to this work is Swiss:
peaks-over-threshold and generalised Pareto approximation of exceedances [Coles 2001] have been
applied, in discrete form, to the extremes of influenza-like hospital visits and hospital
congestion using daily data from a large Swiss hospital [Ranjbar 2022]. That study establishes
both that the approach is applicable to Swiss hospital data and that the tail behaviour is
non-trivial — which is precisely why the present project treats the critical regime with an
extreme-value model rather than leaving it to a handful of observed transitions.

**A theoretically motivated route to anticipating transitions.** A separate literature, developed
in ecology and imported into epidemiology, holds that systems approaching a critical transition
exhibit **critical slowing down**: fluctuations around the current state recover more slowly from
perturbation, so their variance and lag-1 autocorrelation rise measurably *before* the transition
occurs [Scheffer 2009]. The theory has been developed specifically for epidemic transitions
[O'Regan 2013; Brett 2018] and reviewed comparatively [Southall 2021], and resilience indicators
of this kind have recently been evaluated at scale across many diseases and regions.

This matters for a non-obvious reason. These indicators are computed from the *shape of recent
fluctuations*, not from a long history of previous crises, so they are informative in exactly the
regime where data-adaptive models fail. They constitute a **second, independent route to
information at crisis onset** — theoretically grounded rather than evidence-derived — and to my
knowledge nobody has combined the two: resilience indicators as covariates on the transition
intensities of a fitted regime-switching model, with priors on those intensities drawn from
published evidence. Whether they are complementary or redundant is an empirical question.

**The claim here is therefore narrower and stronger than "these methods are absent".** What
exists is two-state epidemic/non-epidemic detection on a single surveillance series, and separate
extreme-value description of congestion. What does not exist is the object this project builds:
a **multi-regime, ordinally interpretable state process for health-system capacity**, estimated
jointly across dispatch, emergency and intensive care series, with **covariate-dependent
transition intensities**, an **extreme-value representation of the critical regime coupled to the state model** — where
[Ranjbar 2022] models the tail as a stand-alone description rather than as the tail of a latent
state process — **resilience indicators from critical-slowing-down theory as covariates on the
transitions**, and **priors derived from the published literature**. The econometric tradition
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

That this gap is real rather than rhetorical is something our systematic review measured: across
138 studies of artificial intelligence in emergency medical services for disasters and health
emergencies, explicit treatment of **uncertainty, transparency and explainability remained
infrequent**, though the field regards these as preconditions for clinical adoption
[Edjinedja 2026]. The same review documents a second obstacle: prehospital data are markedly
incomplete — completeness averaging 52% for triage records, 70% for care reports and 57% for
emergency forms, with individual variables missing in over 90% of records in some registries — so
any method proposed here must tolerate missingness of a magnitude that would be disqualifying
elsewhere.

For rare adverse states this is a necessity rather than a refinement. An alarming regime is by
construction infrequent; an accuracy-based criterion rewards a model that never raises the alarm,
and a threshold optimising AUC bears no relation to the point at which an emergency service can
act differently. The consequences are documented. Between 72% and 99% of clinical monitoring
alarms are false or clinically non-actionable, producing override, delayed response and lost trust
[Winters 2018]; heat–health warning systems set thresholds against a single health proxy, and the
temperatures at which morbidity and mortality rise differ by several degrees, so systems calibrated
on deaths misfire on emergency demand [Lee 2021]; and clinical prediction models adhere to a median
of 44% of TRIPOD items and degrade on external validation [Damen 2025]. That so few forecasting
tools are adopted is usually attributed to implementation barriers; a more parsimonious explanation
is that they were optimised for a quantity nobody needed.

## 1.6 The gap this project addresses

- Forecasting methods perform well where history is long and poorly where decisions are urgent.
- A large body of relevant quantitative evidence exists but is not used as prior information,
  because automated extraction is weakest exactly on numerical quantities and its pooled error
  structure is uncharacterised, and because transportability is unestablished.
- The operational target — escalation state — has latent-regime, extreme-value and
  critical-slowing-down representations in separate partial forms, but not in the coupled,
  multi-regime, theory-and-evidence-informed form the problem requires.
- Evaluation conventions measure something other than usefulness.

**No study has tested whether evidence derived systematically from the published literature
improves health-crisis forecasting in the cold-start regime, using proper scoring rules and
decision-analytic evaluation, in a real health system.** That is the question this project
answers, and it is answerable now because the extraction infrastructure exists — I built it.
