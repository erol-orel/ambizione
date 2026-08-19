# Core idea — the scientific question

## The one-paragraph version

At the onset of a health crisis, the quantity that decision-makers need to forecast — local demand, presentations or occupancy — is precisely the quantity for which almost no local outcome data yet exist. Yet quantitative evidence from analogous events is abundant. This project asks: **can accumulated published evidence compensate for the lack of local outcome data at crisis onset, and can we detect early enough when that evidence should not be trusted?** I will build an uncertainty-aware framework that extracts quantitative estimates from the published literature, converts them into transportable and explicitly discountable prior distributions, and updates them as local observations accumulate. A latent regime representation of health-system state and short-window resilience indicators will provide a complementary local signal of impending escalation. The decisive test is not whether the model is sophisticated: using strict rolling-origin experiments that reconstruct the information available at each historical moment, I will determine whether evidence-derived priors improve probabilistic forecasts in the cold-start phase, how quickly that advantage disappears, and under what conditions priors harm. Decision-analytic evaluation will establish whether any predictive gain is large enough to change operational choices. The result will be a validated answer — positive, conditional or negative — to whether published quantitative evidence should earn a formal role in crisis forecasting.

## The four questions, answered in one sentence each

**1. What is the question?**

> Can published quantitative evidence improve forecasting when local outcome data are scarce, and can we identify early when the evidence is misleading?

**2. Why is it still open — what specifically blocks the field?**

> Relevant estimates exist in thousands of heterogeneous publications, but their extraction error, between-study heterogeneity and transportability have not been characterised well enough to know whether borrowing them improves or degrades cold-start forecasts.

**3. Why you, and why now?** What do you have that makes this tractable for you and not for others?

> I combine fifteen years of quantitative-risk modelling with biomedical epidemiology, a working evidence-synthesis platform that already extracts and pools quantitative parameters from 80,000+ documents, and established access to Geneva emergency and surveillance data.

**4. What exists at the end of four years that does not exist today?**

> A validated, open framework and benchmark showing when literature-derived priors improve cold-start health-system forecasting, when they fail, and how much that information is worth for decisions.

## The independence test

> This is distinct from my previous and current collaborative work because the scientific question, methodological core, evidence platform and planned doctoral programme are mine: I am testing an assumption underneath existing crisis-intelligence infrastructure rather than building another infrastructure project within it.

## The hostile-reader test

**Objection:**

> “Published evidence comes from different populations, definitions and policy regimes; automated extraction is imperfect; and there may be too few crisis transitions to estimate a complicated regime model. Why should I believe the resulting prior is more useful than a simple local baseline?”

**Answer:**

> The project does not assume that borrowing works. It treats extraction error and transportability as measurable sources of uncertainty, compares evidence-derived priors against weakly informative and established borrowing strategies, and uses strict rolling-origin evaluation to expose both benefit and harm. If the evidence does not improve forecasts, or if the regime representation is not identifiable, that is a valid result with a defined fallback — not a hidden failure.
