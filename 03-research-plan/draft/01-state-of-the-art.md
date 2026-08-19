# 1. Current state of research in the field

## 1.1 Forecasting health-system crises: strong in steady state, weak at onset

Anticipating surges in emergency care demand is an established field with a mature toolkit. Syndromic surveillance detects departures from expected baselines — the Farrington quasi-Poisson framework [Farrington 1996] and its reweighted "Flexible" extension [Noufaily 2013] remain important operational approaches. For quantitative prediction, seasonal ARIMA, decomposition models and, where history allows, recurrent architectures are routinely compared, and forecast ensembles have demonstrated strong performance in data-rich settings [Cramer 2022; Sherratt 2023].

Prehospital data can provide a leading signal. Dispatch and ambulance records capture care-seeking before laboratory-confirmed surveillance; a three-region European comparison identified the onset of the 2009 A(H1N1) autumn wave eight days in advance [Rosenkötter 2013], and longer emergency-call series track influenza-like illness [EMS-ILI 2024]. Our systematic review maps this literature and its limits [Edjinedja 2026].

The decisive limitation is **history dependence**. Data-adaptive models need enough local observations to learn seasonality, weekday structure, weather response and crisis dynamics. The published evidence for operational performance is consequently concentrated in the data-rich regime. The difficult question is what to do during the first days or weeks of a novel or displaced crisis, when the local outcome series is short and unstable.

## 1.2 The cold-start problem is specifically a labelled-outcome problem

At crisis onset, context variables are abundant but the outcome to be forecast is not. Surveillance variables can be distinguished as **outcomes** (presentations, incidence, occupancy), **early signals** (dispatch symptoms, wastewater, web search), **susceptibility variables** (vaccination, seroprevalence) and **covariates** (weather, contacts, calendar). The first class is scarce; the others may be abundant. This is therefore not simply small-*n*: it is a problem of forecasting a poorly observed outcome in a large covariate space.

Early signals help but do not eliminate the problem. Wastewater, for example, may lead clinical presentation, but converting viral load into expected presentations requires a shedding-to-incidence relationship that itself comes from external evidence. Transfer learning similarly requires contemporaneous observations from comparable locations. Mechanistic models require parameter values that are often set manually from a small number of studies, with uncertainty asserted rather than derived. The common unresolved issue is therefore **how to use external quantitative information without pretending that it is perfectly transferable**.

## 1.3 The unused resource: published evidence as quantitative prior information

Thousands of studies report quantities potentially relevant at crisis onset: weather–demand associations, surge multipliers, transmission parameters, intervention effects and length-of-stay distributions. Bayesian methods for historical borrowing are well developed: power priors discount historical information [Ibrahim 2000], commensurate priors adapt borrowing to agreement between sources [Hobbs 2011], and meta-analytic-predictive priors derive a distribution for a new setting from previous studies while allowing robust protection against prior–data conflict [Schmidli 2014].

What is missing is a demonstrated bridge from that statistical machinery to **operational cold-start forecasting**. Two problems make the bridge non-trivial.

**Extraction.** Quantitative effect measures are reported inconsistently, with different definitions, units and uncertainty representations. Automated extraction makes large-scale synthesis increasingly feasible, but our review of the emerging literature shows that numerical extraction remains less reliable than categorical extraction, with omissions a major source of error [Shankar 2026]. The unresolved question is not whether an automated system can retrieve numbers, but whether extraction and pooling preserve the dispersion needed for a calibrated prior.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policy regimes. The formal literature provides tools for transportability and reweighting [Bareinboim 2016; Dahabreh 2019; Degtiar 2023], but these tools have not been integrated into an operational framework that explicitly asks whether literature-derived information improves forecasts in a new crisis.

These are therefore not merely engineering obstacles. They define the scientific test: **can accumulated evidence earn a formal role in cold-start forecasting, and under what conditions should it be discounted or rejected?**

## 1.4 Representing escalation as a state, not only a point forecast

A second, supporting problem concerns the target itself. Emergency operations are interested in state — routine, elevated, strained or critical — rather than only in a point prediction of tomorrow's count. Latent-state representations are established in surveillance: Poisson hidden Markov models have long been used to distinguish epidemic and non-epidemic periods [Le Strat 1999; Watkins 2009]. Extreme-value methods have also been applied to Swiss hospital visits and congestion [Coles 2001; Ranjbar 2022].

This project combines these ideas in a deliberately limited way: a latent ordinal state provides the common representation needed to compare borrowing strategies, while an extreme-value component handles rare critical exceedances. The contribution is not the invention of hidden Markov or extreme-value models; it is their use as a **common state representation for testing evidence borrowing at crisis onset**.

A complementary theoretical signal comes from critical-slowing-down theory. Systems approaching some critical transitions can show rising variance and lag-1 autocorrelation before the transition [Scheffer 2009], with applications and reviews in epidemic dynamics [O'Regan 2013; Brett 2018; Southall 2021]. These indicators are attractive here because they use the shape of a short recent series rather than a long history of comparable crises. They are therefore treated as a **secondary information channel** whose incremental value is tested empirically, not as a universal early-warning mechanism.

## 1.5 From forecast accuracy to decision value

Forecasting studies commonly report discrimination or error measures such as AUC, RMSE and MAE. Proper scoring rules evaluate probabilistic forecasts and reward calibration [Gneiting 2007], but even a well-calibrated forecast may be operationally irrelevant if it does not change a decision. Decision-analytic methods instead evaluate predictions under explicit consequences and thresholds [Vickers 2006].

This distinction matters in crisis response because false alarms and missed escalations have asymmetric and persistent costs. Our systematic review of AI in emergency medical services for disasters and health emergencies found that explicit treatment of uncertainty, transparency and explainability remains uncommon [Edjinedja 2026]. The project therefore evaluates forecasting methods first statistically and then under an elicited operational loss structure.

## 1.6 The specific gap addressed by this project

The literature establishes four pieces separately:

- forecasting and surveillance methods work substantially better once sufficient local history exists;
- Bayesian methods can borrow information from historical studies while allowing discounting and conflict handling;
- latent-state, extreme-value and resilience methods offer partial representations of escalation;
- decision analysis provides a way to evaluate whether predictive information changes action.

What has not been established is whether these pieces can be connected around the **cold-start question**: whether systematically extracted quantitative evidence improves probabilistic forecasting before local outcome data become informative, and whether harmful borrowing can be detected early enough to be discounted.

The project therefore makes a deliberately falsifiable claim rather than a broad novelty claim: **the primary contribution is an empirical answer to the value of evidence-derived priors in cold-start health-system forecasting.** The supporting methodological components are justified only insofar as they make that comparison scientifically valid.
