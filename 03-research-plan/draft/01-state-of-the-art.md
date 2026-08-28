# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasting health-system crises: strong in steady state, weak at onset

Anticipating surges in emergency care demand is an established field with a mature toolkit. Syndromic surveillance detects departures from expected baselines — the Farrington quasi-Poisson framework [Farrington 1996] and its reweighted "Flexible" extension [Noufaily 2013] remain important operational approaches. For quantitative prediction, seasonal ARIMA, decomposition models and, where history allows, recurrent architectures are routinely compared, and forecast ensembles have demonstrated strong performance in data-rich settings [Cramer 2022; Sherratt 2023].

Prehospital data can provide a leading signal: dispatch and ambulance records capture care-seeking before laboratory-confirmed surveillance, a three-region European comparison identified the onset of the 2009 A(H1N1) autumn wave eight days in advance [Rosenkötter 2013], and longer emergency-call series track influenza-like illness [EMS-ILI 2024]. Our systematic review maps this literature and its limits [Edjinedja 2026].

The decisive limitation is **history dependence**: data-adaptive models need enough local observations to learn seasonality, weekday structure, weather response and crisis dynamics, so the published evidence for operational performance is concentrated in the data-rich regime. The difficult question is what to do during the first days or weeks of a novel or displaced crisis, when the local outcome series is short and unstable.

### 2.1.2 The cold-start problem is specifically a labelled-outcome problem

At crisis onset, context variables are abundant but the outcome to be forecast is not. Surveillance variables can be distinguished as **outcomes** (presentations, incidence, occupancy), **early signals** (dispatch symptoms, wastewater, web search), **susceptibility variables** (vaccination, seroprevalence) and **covariates** (weather, contacts, calendar). The first class is scarce; the others may be abundant. This is therefore not simply small-*n*: it is a problem of forecasting a poorly observed outcome in a large covariate space.

This distinction matters because abundance of candidate predictors can itself mislead: Google Flu Trends famously overestimated influenza activity by more than a factor of two [Lazer 2014]. More information is not automatically more information about the quantity that matters.

Early signals help but do not eliminate the problem. Wastewater may lead clinical presentation, but converting viral load into expected presentations needs a shedding-to-incidence relationship that itself comes from external evidence; transfer learning needs contemporaneous observations from comparable locations; mechanistic models need parameters usually set by hand from a few studies, with uncertainty asserted rather than derived. The common unresolved issue is **how to use external quantitative information without pretending it is perfectly transferable**.

### 2.1.3 The unused resource: published evidence as quantitative prior information

Thousands of studies report quantities potentially relevant at crisis onset: weather–demand associations, surge multipliers, transmission parameters, intervention effects and length-of-stay distributions. Bayesian methods for historical borrowing are well developed — power priors discount historical information [Ibrahim 2000], commensurate priors adapt borrowing to agreement between sources [Hobbs 2011], and meta-analytic-predictive priors derive a distribution for a new setting from previous studies with robust protection against prior–data conflict [Schmidli 2014].

What is missing is a demonstrated bridge from that statistical machinery to **operational cold-start forecasting**. Two problems make the bridge non-trivial.

**Extraction.** Quantitative effect measures are reported inconsistently, with different definitions, units and uncertainty representations. Automated extraction makes large-scale synthesis increasingly feasible, but our review of the emerging literature shows that numerical extraction remains less reliable than categorical extraction: reported numerical accuracy spans roughly 47–88%, compared with 74–96% for categorical items, and omissions account for a large share of errors [Shankar 2026]. The unresolved question is not whether an automated system can retrieve numbers, but whether extraction and pooling preserve the dispersion needed for a calibrated prior.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policy regimes. Formal tools for transportability and reweighting exist [Bareinboim 2016; Dahabreh 2019; Degtiar 2023], but have not been integrated into an operational framework asking whether literature-derived information improves forecasts in a new crisis.

These are therefore not merely engineering obstacles. They define the scientific test: **can accumulated evidence earn a formal role in cold-start forecasting, and under what conditions should it be discounted or rejected?**

### 2.1.4 Representing escalation as a state, not only a point forecast

A second, supporting problem concerns the target itself. Emergency operations are interested in state — routine, elevated, strained or critical — rather than only in a point prediction of tomorrow's count. Latent-state representations are established in surveillance: Poisson hidden Markov models have long been used to distinguish epidemic and non-epidemic periods [Le Strat 1999; Watkins 2009]. Extreme-value methods have also been applied to Swiss hospital visits and congestion [Coles 2001; Ranjbar 2022].

This project uses these ideas in a deliberately limited way: a latent ordinal state provides the common representation in which borrowing strategies are compared, with an extreme-value component for rare critical exceedances. The contribution is not the models but their use as a **common state representation for testing evidence borrowing at crisis onset**.

A complementary signal comes from critical-slowing-down theory: systems approaching some critical transitions show rising variance and lag-1 autocorrelation beforehand [Scheffer 2009], with applications in epidemic dynamics [O'Regan 2013; Brett 2018; Southall 2021]. They are attractive here because they use the shape of a short recent series rather than a long history of comparable crises, and are treated as a **secondary information channel** tested empirically, not as a universal early-warning mechanism.

### 2.1.5 From forecast accuracy to decision value

Forecasting studies commonly report discrimination or error measures such as AUC, RMSE and MAE. Proper scoring rules evaluate probabilistic forecasts and reward calibration [Gneiting 2007], but even a well-calibrated forecast may be operationally irrelevant if it does not change a decision. Decision-analytic methods instead evaluate predictions under explicit consequences and thresholds [Vickers 2006].

This matters in crisis response because false alarms and missed escalations have asymmetric, persistent costs. Clinical monitoring is the concrete warning: 72–99% of reported alarms have been false or non-actionable in reviewed settings [Winters 2018]. Heat-health warnings are another: thresholds calibrated to mortality need not match those for morbidity or emergency demand [Lee 2021]. The project therefore evaluates forecasting methods first statistically, then under an elicited operational loss structure.

### 2.1.6 The specific gap addressed by this project

The four pieces above exist separately — forecasting that needs local history, Bayesian borrowing with discounting, latent-state and resilience representations of escalation, and decision analysis. What has not been established is whether they connect around the **cold-start question**: whether systematically extracted quantitative evidence improves probabilistic forecasting before local outcome data become informative, and whether harmful borrowing is detectable early enough to discount. The claim is therefore deliberately falsifiable rather than broadly novel, and the supporting components are justified only insofar as they make that comparison valid.
