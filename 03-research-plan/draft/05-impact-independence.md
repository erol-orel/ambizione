# 5. Relevance, impact and scientific independence

## 5.1 Scientific relevance

The project tests an assumption that crisis forecasting currently makes informally: that accumulated evidence from elsewhere can provide useful information when local outcome data are insufficient. The result is useful in either direction. If literature-derived priors improve cold-start forecasts, the project provides a principled and auditable way to borrow information. If the benefit is weak, conditional or negative, the project establishes when borrowing should not be trusted — an equally important result because manual parameter selection from a few familiar papers is common but rarely evaluated as a forecasting intervention.

The project also leaves three durable resources:

- **A quantitative extraction benchmark** for testing whether automated evidence synthesis preserves the uncertainty needed for quantitative reuse.
- **An open reference framework** for evidence-informed latent-state forecasting, with explicit borrowing, conflict detection and calibration rather than a black-box forecast.
- **A decision-analytic evaluation framework** showing when a statistical improvement is large enough to matter operationally.

These contributions are deliberately subordinate to the central scientific question. The project is not primarily a new LLM extraction system, a new early-warning indicator, or a new forecasting competition. It is a test of whether external quantitative evidence earns its place in cold-start prediction.

## 5.2 Practical and societal impact

The practical contribution is preparedness rather than a promised clinical deployment. During the first weeks of a crisis, emergency systems must decide whether to open capacity, redistribute resources or escalate before local outcomes provide a reliable empirical base. The project will quantify whether external evidence can improve those decisions and, crucially, how much uncertainty should remain around the resulting recommendation.

The Geneva setting provides a realistic operational anchor through established emergency and public-health collaborations. The contrasting validation domains are designed to show what transfers and what does not. A negative result would also have practical value by identifying situations in which literature-derived parameters should not be allowed to drive operational decisions.

## 5.3 Scientific independence

**This project is my first independent research programme, not an extension of a supervisor's or consortium's work.** Its independence is demonstrable in four ways.

**1. The question is mine.** The question arose from a problem I encountered while developing LiteRev-Evidence: a system could pool published quantitative estimates into prior distributions, but there was no empirical basis for knowing whether those priors improved forecasting in a genuinely new setting. The Ambizione project tests that assumption rather than building another infrastructure component for an existing programme.

**2. The methodological core is mine.** I bring fifteen years of quantitative-finance experience in regime models, extreme-value risk and stress testing into biomedical crisis forecasting. These methods were not inherited from my doctoral or current research group; their transfer to this problem is part of the intellectual trajectory that defines the project.

**3. The key instrument is mine.** I developed LiteRev and, subsequently, LiteRev-Evidence. The platform is already operational and is used as the instrument through which the project asks its scientific question. Ambizione funds the research programme around the instrument, not the creation of the instrument itself.

**4. The research line and scientific leadership will be mine.** I will lead the methodological work, the confirmatory analysis and the integrated programme. Limited approved support staff, if requested, will carry bounded technical/extraction tasks and will not be presented as independent scientific leads. The project is distinct from my collaborative roles in GESICA and the Horizon consortium:

| | GESICA | Horizon consortium | **Ambizione project** |
| --- | --- | --- | --- |
| Primary aim | Cross-border EMS decision/infrastructure work | Epidemic-intelligence infrastructure | **Test the value and limits of evidence-derived priors in cold-start forecasting** |
| My role | Contributor | Contributor | **Principal investigator** |
| Main output | Collaborative system/infrastructure | Collaborative platform/data outputs | **Independent inferential result, method and research line** |
| Scientific ownership | Shared | Shared | **Question, methodological core and programme led by me** |

The host arrangement reinforces rather than dilutes this independence. I will move into **Data Science for Digital Health, Department of Radiology and Medical Informatics**, a different department and scientific community from the one in which I trained, while maintaining an associated connection to the Institute of Global Health and a formal clinical collaboration with HUG emergency medicine. The host provides methods, domain access and clinical interaction; it does not define the research question or own the programme.

The career outcome is therefore concrete: Ambizione would allow me to establish an independent line at the intersection of evidence synthesis, quantitative time-series modelling and emergency public health, lead the research programme directly, and develop a line that can continue beyond the grant independently of the collaborative infrastructure from which it originated.
