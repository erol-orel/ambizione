# Module 1 — Contributions to the generation of new ideas, tools, methodologies or knowledge

> Outputs cited here: **4** — LiteRev (JMIR 2023); LiteRev-Evidence platform; HIV prediction
> (PLoS ONE 2022); Delta/Omicron severity (CMI Communications 2024).

---

I came to biomedical research after fifteen years as a quantitative analyst and risk manager,
where my work concerned the prediction of rare, costly events: extreme value estimation for
non-Gaussian tails, regime and factor models, stress testing and scenario analysis. That
inheritance shapes everything below. My contribution to health research has consistently been to
bring methods developed for anticipating discontinuities in one domain to problems in another
where the same structure exists but the machinery does not.

**Prediction where data are incomplete.** My doctoral work asked whether individual health status
could be predicted from socio-behavioural information alone, in settings where clinical data are
sparse. In *PLoS ONE* (2022) I predicted individual HIV status across East and Southern Africa
using gradient-boosted models, and — the part I consider the real contribution — characterised
where such models transported between countries and where they did not. That question, of when an
estimate obtained in one population is usable in another, has stayed with me and is now the centre
of my research programme. Related work extended it to treatment-interruption prediction and to
latent structure across populations.

**A tool, and then a platform.** Reviewing literature at the scale these questions demand was the
bottleneck, so I built the instrument. **LiteRev** (*Journal of Medical Internet Research*, 2023,
first author) combines natural language processing, dimensionality reduction, clustering and
nearest-neighbour retrieval to accelerate the identification and structuring of relevant research.
It is used beyond my own work: a recent systematic review of artificial intelligence in emergency
medical services used LiteRev in its methods to structure 138 retained publications.

Since 2024 I have developed **LiteRev-Evidence**, which extends this from retrieval into
structured quantitative extraction. It is a production system rather than a prototype: a
continuously updated corpus of over 81,000 publications with 324,000 embedded passages,
structured extraction with provenance and study-quality scoring, quality-weighted pooling of
extracted parameters into distributions, and compartmental, time-series and machine-learning
components that consume them. Thirty-one operational scenarios have been elaborated with
emergency-medicine partners.

Building it produced the question I now want to answer, and I regard that as the most significant
intellectual contribution of the work. The platform will readily pool published estimates into
prior distributions — and I cannot establish whether it should. Published effect sizes are
selectively reported, estimated under different health systems, and automated extraction is
weakest precisely on numerical quantities. Whether such evidence improves forecasting when local
data are scarce, or misleads confidently at the moment it matters most, is unresolved and
consequential.

**Clinical and epidemic knowledge.** Alongside the methodological work I have contributed
substantive findings, including a comparison of clinical severity between Delta and Omicron
sub-lineages in a Swiss tertiary centre (*CMI Communications*, 2024, first author), work that
required close engagement with hospital clinical data and with the people who generate it.
