# Title

**COLDSTART — Evidence-informed forecasting of health-system crises when local data are scarce**

# Summary

When a health crisis begins, the data needed to forecast it does not yet exist. Emergency
services and hospitals must decide how many ambulances to staff, how many intensive care beds to
open and when to escalate, at precisely the moment when the local time series is a handful of
observations long. The forecasting methods that perform best in steady state — and the ensemble
infrastructures now organised around them — require years of history, so they are weakest exactly
where the decisions are most consequential and least reversible.

There is, however, information available at the outset, from two directions. The first is the
accumulated published evidence from analogous events elsewhere. Thousands of studies report transmission parameters, weather–demand
associations, surge magnitudes and intervention effects. That evidence is not used quantitatively in operational forecasting, because turning
heterogeneous published estimates into usable priors is difficult and nobody has established
whether doing so helps or harms. The second is the local series itself: dynamical systems theory
holds that a system approaching a critical transition loses resilience, so the variance and
autocorrelation of its fluctuations rise **before** the transition — a signal computable from a
short window, and therefore available when nothing else is.

This project asks that question directly. Building on **LiteRev-Evidence**, a production
literature-synthesis platform I developed that already extracts and pools quantitative parameters
from a corpus of over 80,000 documents, I will (i) establish how reliably quantitative evidence
can be extracted automatically and where that extraction is systematically biased; (ii) develop a
**Bayesian regime-switching** framework — with extreme value methods for the tail, resilience
indicators on its transition intensities, and a conformal layer guaranteeing calibrated coverage
even under misspecification — representing health-system state as latent regimes rather than as a
threshold on a point forecast;
(iii) test, by rolling-origin evaluation that respects the true information set available at each
historical moment, whether evidence-derived priors improve forecast skill in the cold-start
regime, and characterise when they mislead; and (iv) evaluate the result on the criterion that
matters — whether it changes decisions and outcomes — through threshold elicitation with emergency
responders, retrospective counterfactual analysis of what earlier escalation would have changed,
and a prospective shadow-mode deployment.

Validation spans crisis archetypes with different dynamics: a respiratory epidemic, a heatwave,
and — using linked case–installation data unique to Geneva — a waterborne outbreak.

The approach is deliberately imported from outside epidemiology. Regime-switching models, extreme
value theory and stress testing are standard instruments for anticipating rare, costly transitions
in quantitative finance, where I worked for fifteen years before moving into public health. They
have barely been applied to health-system surge. The combination of that methodological
inheritance with a working evidence-synthesis platform and established links to Geneva's emergency
system is, as far as I am aware, unique.

The deliverables are a validated answer to whether published evidence can be made to earn its
place in operational forecasting, an open framework for doing so, and — if the answer is negative
or conditional — a clear account of the conditions under which it fails. Both outcomes are
useful, which is what makes the question worth four years.
