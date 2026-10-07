# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasting health-system crises: strong in steady state, weak at onset

Syndromic surveillance detects departures from expected baselines [Farrington 1996; Noufaily 2013], and forecast ensembles perform strongly in data-rich settings [Cramer 2022; Sherratt 2023]. Dispatch records lead confirmed surveillance: the 2009 A(H1N1) autumn onset was identified eight days early in three European regions [Rosenkötter 2013], long call series track influenza-like illness [Bonora 2025], and our systematic review maps the field [Edjinedja 2026].

The decisive limitation is **history dependence**: data-adaptive models need enough local observations to learn seasonality, weather response and crisis dynamics; reviews of emergency-demand forecasting catalogue which model families perform for which outcome and horizon [Wargon 2009]; every recommended model is trained on years of local history.

**The cold-start problem is a labelled-outcome problem.** At crisis onset, context variables abound but the outcome to be forecast does not, and abundance itself can mislead: Google Flu Trends overestimated influenza by more than a factor of two [Lazer 2014]. Early signals do not close the gap: wastewater needs a shedding-to-incidence relationship that itself comes from external evidence; transfer learning needs comparable contemporaneous observations. The common issue is **how to use external quantitative information without pretending it is perfectly transferable**.

### 2.1.2 The unused resource: published evidence as quantitative prior information

Bayesian borrowing is well developed: power priors [Ibrahim 2000], commensurate priors [Hobbs 2011], meta-analytic-predictive priors with robust conflict protection [Schmidli 2014]. Informative priors have been used to forecast disease under sparse local data [Cook 2023]. What has not been established is narrower and harder: whether an **automatically constructed** evidence prior, with extraction error and transportability uncertainty propagated into it, improves **operational cold-start forecasts under strict historical information constraints**, and whether harmful borrowing is detected in time to act.

**Parameter values are not the only transferable object.** The literature also carries **predictor variables and lag structures**, **model-form evidence** (which algorithm families work for which crisis type and horizon) and **outcome and threshold definitions**. Living systematic reviews keep syntheses current [Elliott 2014], yet no operational forecasting framework consumes these objects systematically.

**Extraction.** Automated extraction makes large-scale synthesis feasible, but numerical extraction remains less reliable than categorical (reported accuracy roughly 47–88% versus 74–96%), and omissions dominate errors [Shankar 2026]. The question is whether extraction and pooling preserve the dispersion a calibrated prior needs.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policy regimes. Formal transportability tools exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023] but are not integrated into any operational cold-start framework.

### 2.1.3 Representing escalation as a state, not only a point forecast

Emergency operations often need an interpretable escalation state (routine, elevated, strained, critical), not only tomorrow's count. Latent-state representations are established in surveillance: Poisson hidden Markov models distinguish epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009]; extreme-value methods frame rare critical exceedances [Coles 2001], applied to Swiss hospital congestion [Ranjbar 2022]. Here they serve one purpose: a latent ordinal state as the **common representation for testing evidence borrowing at crisis onset**, with an extreme-value component for rare critical exceedances. Mechanistic transmission models [Keeling 2008] enter as components only where the crisis is epidemiological; environmental crises such as heat are driven by exposure–response, not transmission. Critical-slowing-down theory (rising variance and lag-1 autocorrelation before some transitions [Scheffer 2009]; epidemic applications [O'Regan 2013; Brett 2018; Southall 2021]) reads the shape of a short recent series: a **secondary information channel**, tested empirically.

### 2.1.4 From forecast accuracy to decision value

Proper scoring rules reward calibration [Gneiting 2007], but a calibrated forecast is irrelevant if it changes no decision; decision-analytic methods evaluate predictions under explicit consequences [Vickers 2006]. alert systems fail operationally when alarms are overwhelmingly non-actionable (72–99% in clinical monitoring [Winters 2018]); mortality-calibrated heat thresholds need not match demand thresholds [Lung 2021]; pollution–asthma emergency associations lack recent Swiss acute-episode studies [Zheng 2015]. Methods are therefore evaluated first statistically, then under an elicited operational loss structure.

### 2.1.5 The specific gap addressed by this project

Ongoing programmes occupy the neighbouring ground: multi-model forecasting hubs run routinely (ECDC RespiCast, US CDC FluSight), Horizon Europe funds epidemic-intelligence infrastructure (including GeoAI4EI, in which I take part), and the Franco-Swiss GESICA programme builds cross-border crisis intelligence. All build surveillance, epidemic-intelligence, forecasting or decision-support capability; their stated objectives do not address whether automatically synthesised external quantitative evidence should enter a forecast as formal prior information at local cold start.

What has not been established is whether these pieces connect around the **cold-start question**, and whether the loop from living evidence synthesis to variable choice, model choice, thresholds and automatically re-validated forecasts can be closed under pre-registered rules.
