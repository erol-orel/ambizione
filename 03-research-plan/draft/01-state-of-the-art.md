# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasting health-system crises: strong in steady state, weak at onset

Anticipating surges in emergency care demand is an established field. Syndromic surveillance detects departures from expected baselines — the Farrington quasi-Poisson framework [Farrington 1996] and its reweighted "Flexible" extension [Noufaily 2013] remain operational mainstays. For quantitative prediction, seasonal ARIMA, decomposition models and recurrent architectures are routinely compared, and forecast ensembles perform strongly in data-rich settings [Cramer 2022; Sherratt 2023].

Prehospital data can lead: dispatch records capture care-seeking before laboratory-confirmed surveillance, a three-region European comparison identified the 2009 A(H1N1) autumn-wave onset eight days in advance [Rosenkötter 2013], and long emergency-call series track influenza-like illness [EMS-ILI 2025]. Our systematic review maps this literature and its limits [Edjinedja 2026].

The decisive limitation is **history dependence**: data-adaptive models need enough local observations to learn seasonality, weekday structure, weather response and crisis dynamics, so the published evidence for operational performance is concentrated in the data-rich regime. The difficult question is what to do during the first days or weeks of a novel or displaced crisis, when the local outcome series is short and unstable.

### 2.1.2 The cold-start problem is specifically a labelled-outcome problem

At crisis onset, context variables are abundant but the outcome to be forecast is not. Surveillance variables divide into **outcomes** (presentations, incidence, occupancy), **early signals** (dispatch symptoms, wastewater, web search), **susceptibility variables** (vaccination, seroprevalence) and **covariates** (weather, contacts, calendar). The first class is scarce; the others may abound. This is not simply small-*n*: it is forecasting a poorly observed outcome in a large covariate space.

This matters because abundance of candidate predictors can itself mislead: Google Flu Trends famously overestimated influenza activity by more than a factor of two [Lazer 2014]. More information is not automatically more information about the quantity that matters.

Early signals help but do not eliminate the problem: wastewater may lead clinical presentation, but converting viral load into presentations needs a shedding-to-incidence relationship that itself comes from external evidence; transfer learning needs contemporaneous observations from comparable places; mechanistic models need parameters set by hand from a few studies, uncertainty asserted rather than derived. The common issue is **how to use external quantitative information without pretending it is perfectly transferable**.

### 2.1.3 The unused resource: published evidence as quantitative prior information

Thousands of studies report quantities relevant at crisis onset: weather–demand associations, surge multipliers, transmission parameters and length-of-stay distributions. Bayesian borrowing is well developed — power priors discount historical information [Ibrahim 2000], commensurate priors adapt to agreement between sources [Hobbs 2011], meta-analytic-predictive priors derive a new-setting distribution with robust protection against prior–data conflict [Schmidli 2014].

Informative priors have been used to forecast disease under sparse local data [Cook 2023]. What has not been established is narrower and harder: whether an **automatically constructed** evidence prior — extraction error and transportability uncertainty propagated into it — improves **operational cold-start forecasts under strict historical information constraints**, and whether harmful borrowing is detected early enough to act. Two problems make that test non-trivial.

**Extraction.** Effect measures are reported inconsistently, across definitions, units and uncertainty representations. Automated extraction makes large-scale synthesis feasible, but our review of the emerging literature shows numerical extraction remains less reliable than categorical: reported numerical accuracy spans roughly 47–88% versus 74–96% for categorical items, and omissions dominate errors [Shankar 2026]. The question is not whether a system can retrieve numbers, but whether extraction and pooling preserve the dispersion a calibrated prior needs.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policy regimes. Formal transportability and reweighting tools exist [Bareinboim 2016; Dahabreh 2019; Degtiar 2023], but are not integrated into an operational framework asking whether literature-derived information improves forecasts in a new crisis.

These are not merely engineering obstacles; they define the scientific test: **can accumulated evidence earn a formal role in cold-start forecasting, and when should it be discounted or rejected?**

### 2.1.4 Representing escalation as a state, not only a point forecast

A second, supporting problem is the target itself: emergency operations are interested in state — routine, elevated, strained or critical — rather than only a point prediction of tomorrow's count. Latent-state representations are established in surveillance: Poisson hidden Markov models have long distinguished epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009], and extreme-value methods have been applied to Swiss hospital visits and congestion [Coles 2001; Ranjbar 2022].

This project uses these ideas in a deliberately limited way: a latent ordinal state provides the common representation in which borrowing strategies are compared, with an extreme-value component for rare critical exceedances. The contribution is not the models but their use as a **common state representation for testing evidence borrowing at crisis onset**.

A complementary signal comes from critical-slowing-down theory: systems approaching some transitions show rising variance and lag-1 autocorrelation beforehand [Scheffer 2009], with epidemic applications [O'Regan 2013; Brett 2018; Southall 2021]. Attractive here because they use the shape of a short recent series rather than a long history of comparable crises, they are a **secondary information channel** tested empirically, not a universal early-warning mechanism.

### 2.1.5 From forecast accuracy to decision value

Forecasting studies commonly report discrimination or error measures such as AUC and RMSE. Proper scoring rules evaluate probabilistic forecasts and reward calibration [Gneiting 2007], but even a well-calibrated forecast is operationally irrelevant if it changes no decision. Decision-analytic methods instead evaluate predictions under explicit consequences and thresholds [Vickers 2006].

This matters in crisis response because false alarms and missed escalations have asymmetric, persistent costs. Clinical monitoring is the concrete warning: 72–99% of reported alarms have been false or non-actionable in reviewed settings [Winters 2018]; heat-health thresholds calibrated to mortality need not match those for morbidity or emergency demand [Lee 2021]. The project therefore evaluates forecasting methods first statistically, then under an elicited operational loss structure.

### 2.1.6 The specific gap addressed by this project

Ongoing programmes occupy the neighbouring ground: multi-model forecasting hubs run routinely (ECDC RespiCast, US CDC FluSight), Horizon Europe funds epidemic-intelligence infrastructure — including GeoAI4EI, in which I take part — and the Franco-Swiss GESICA programme builds cross-border crisis intelligence. All build surveillance, forecasting or decision-support capability from local data; none tests whether accumulated external evidence deserves a formal role before local data become informative.

The four pieces above exist separately — forecasting that needs local history, Bayesian borrowing with discounting, latent-state and resilience representations of escalation, and decision analysis. What has not been established is whether they connect around the **cold-start question**: whether systematically extracted quantitative evidence improves probabilistic forecasting before local outcome data become informative, and whether harmful borrowing is detectable early enough to discount. The supporting components are justified only insofar as they make that comparison valid.
