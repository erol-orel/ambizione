# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasting health-system crises: strong in steady state, weak at onset

Syndromic surveillance detects departures from expected baselines [Farrington 1996; Noufaily 2013], and forecast ensembles perform strongly in data-rich settings [Cramer 2022; Sherratt 2023]. Dispatch records lead confirmed surveillance: the 2009 A(H1N1) autumn onset was identified eight days in advance across three European regions [Rosenkötter 2013], long call series track influenza-like illness [Bonora 2025], and our systematic review maps the field [Edjinedja 2026].

The decisive limitation is **history dependence**: data-adaptive models need enough local observations to learn seasonality, weather response and crisis dynamics. What to do in the first weeks of a novel or displaced crisis remains open.

**The cold-start problem is specifically a labelled-outcome problem.** At crisis onset, context variables abound but the outcome to be forecast does not, and abundance itself can mislead: Google Flu Trends overestimated influenza activity by more than a factor of two [Lazer 2014]. Early signals do not close the gap: wastewater needs a shedding-to-incidence relationship that itself comes from external evidence; transfer learning needs contemporaneous comparable observations; mechanistic models need hand-set parameters from a few studies. The common issue is **how to use external quantitative information without pretending it is perfectly transferable**.

### 2.1.2 The unused resource: published evidence as quantitative prior information

Bayesian borrowing is well developed: power priors [Ibrahim 2000], commensurate priors [Hobbs 2011], meta-analytic-predictive priors with robust conflict protection [Schmidli 2014]. Informative priors have been used to forecast disease under sparse local data [Cook 2023]. What has not been established is narrower and harder: whether an **automatically constructed** evidence prior, with extraction error and transportability uncertainty propagated into it, improves **operational cold-start forecasts under strict historical information constraints**, and whether harmful borrowing is detected early enough to act.

**Extraction.** Automated extraction makes large-scale synthesis feasible, but numerical extraction remains less reliable than categorical (reported accuracy roughly 47–88% versus 74–96%), and omissions dominate errors [Shankar 2026]. The question is whether extraction and pooling preserve the dispersion a calibrated prior needs.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policy regimes. Formal transportability tools exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023] but are not integrated into any operational cold-start framework.

### 2.1.3 Representing escalation as a state, not only a point forecast

Emergency operations are interested in state (routine, elevated, strained, critical) rather than only tomorrow's count. Latent-state representations are established in surveillance: Poisson hidden Markov models distinguish epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009]; extreme-value methods have been applied to Swiss hospital visits [Coles 2001; Ranjbar 2022]. Here they serve one purpose: a latent ordinal state as the **common representation for testing evidence borrowing at crisis onset**, with an extreme-value component for rare critical exceedances. Critical-slowing-down theory (rising variance and lag-1 autocorrelation before some transitions [Scheffer 2009]; epidemic applications [O'Regan 2013; Brett 2018; Southall 2021]) uses the shape of a short recent series: a **secondary information channel**, tested empirically.

### 2.1.4 From forecast accuracy to decision value

Proper scoring rules reward calibration [Gneiting 2007], but a calibrated forecast is irrelevant if it changes no decision; decision-analytic methods evaluate predictions under explicit consequences [Vickers 2006]. 72–99% of reported clinical alarms have been false or non-actionable [Winters 2018]; mortality-calibrated heat thresholds need not match demand thresholds [Lung 2021]; pollution–asthma emergency associations lack recent Swiss acute-episode studies [Zheng 2015]. Methods are therefore evaluated first statistically, then under an elicited operational loss structure.

### 2.1.5 The specific gap addressed by this project

Ongoing programmes occupy the neighbouring ground: multi-model forecasting hubs run routinely (ECDC RespiCast, US CDC FluSight), Horizon Europe funds epidemic-intelligence infrastructure (including GeoAI4EI, in which I take part), and the Franco-Swiss GESICA programme builds cross-border crisis intelligence. These programmes develop surveillance, forecasting and decision-support capability from local data; their stated objectives do not include testing whether automatically synthesised external evidence should enter a forecast as formal prior information at local cold start.

What has not been established is whether these pieces connect around the **cold-start question**: whether systematically extracted evidence improves forecasting before local outcome data become informative, and whether harmful borrowing is detectable early enough to discount.
