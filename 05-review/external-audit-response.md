# Response to the external audit of 30 September 2026

Disposition of every substantive point, with what was applied and what was rejected and why.
The audit's overall verdict — strong science, document not yet submission-ready — matches this
repository's own assessment (`final-quality-audit.md`): the remaining gap is applicant inputs
(placeholders, letters, statuses), not writing.

## Accepted and applied (research plan changed)

| # | Audit point | What was done |
| --- | --- | --- |
| 1 | **Novelty claim too broad** (§3) | §2.1.3 now acknowledges that informative priors under sparse local data exist (with a `[[cite examples]]` marker — I could not verify the USGS/Sci Rep 2023 paper from this environment and will not cite unverified) and narrows the gap to the end-to-end test: automatically constructed priors with extraction + transportability uncertainty propagated, strict historical information sets, harmful-borrowing detection |
| 2 | **CASU-144 vs "demand"** (§5) | T3.0 now scopes the primary claim explicitly: the operational demand signal observed by the dispatch system; broader hospital-demand claims only where validated against ED/ICU channels |
| 3 | **Episode-level power** (§8) | T3.3 now states the unit of inference (episode; origins are repeated measures) and that the design is powered by simulation-based operating characteristics — type I error, power, interval width under within-episode dependence — run before registration point 2 |
| 4 | **Literature vs situational intelligence** (§10) | T3.2 now tiers the prior: **confirmatory = peer-reviewed literature + preprints only** under the rolling cut-off; situational reporting (WHO DON, ECDC RRA) is a **pre-specified secondary prior variant**. H3a tests literature borrowing, not dynamic evidence fusion. T1.2's source-type stratum retained |
| 5 | **One concrete decision for H4** (§11) | T4.1 fixes the primary decision: trigger surge-capacity escalation when P(strained/critical) crosses the elicited threshold; its losses anchor T4.2 |
| 6 | **Host tense contradiction** (§15) | §2.6 "is signed" → "will be signed" — the letter is requested, not in hand |
| 7 | **Missing bibliography entries** (§17) — *verified: true* | [Lazer 2014], [Höhle 2014], [McGough 2020] added with full references; [Winters 2018], [Lee 2021] added as flagged skeletons (I will not invent author lists). [Xu 2023] key corrected to [Barber 2023] (our own note had already flagged it; entry is uncited in text — cite or drop) |
| 8 | **Meta-language / defensiveness** (§13, §19) | Roughly a dozen self-referential sentences cut or folded ("the distinction is not cosmetic", "nothing is described above its actual status", "that is the precise claim", etc.). ~1,300 characters recovered, spent on points 1–5 |

## Accepted in part

- **H1 overcommitted (§4).** The directional hypothesis is *kept* — a pre-registered directional
  prediction is scientifically stronger than the audit's neutral rewrite, and H1 already states
  that absence of the effect is informative. What was fixed is the justification: the direction
  is now derived mechanistically (omitted uncertainty statements and missed variance components
  shrink dispersion estimates systematically, not randomly) rather than asserted from error rates.
- **Character target 55–57k (§18).** The audit's counts are of raw markdown and overstate (its
  own caveat concedes this); our stripped counter reads 59,995. The real requirement — margin
  against the binding mySNF counter — is accepted differently: **upload a draft PDF to mySNF
  early and calibrate against its counter**, then set the final target. Cutting 3–5k of substance
  today, before the placeholder fill, would be premature amputation.
- **Simplify the stack (§7).** Largely already done (EVT, CSD, conformal, equity, shadow mode are
  explicitly supporting/secondary). Further trims applied where cheap. **Legionellosis is NOT
  removed**: it is the applicant's own BASEC-approved, uniquely linked dataset, already scoped as
  a year-4 extension whose omission "does not invalidate the main result", and it does real work
  in §2.2 (feasibility, independence). Removing it saves ~400 characters and costs a genuine
  asset.

## Rejected, with reasons

1. **"Aim for 55,000–57,000."** See above — calibrate on mySNF, don't pre-cut substance.
2. **Neutral H1.** A directional, mechanistically justified, falsifiable hypothesis with a
   pre-stated interpretation of its failure is better science and better review optics than
   "extraction will distort dispersion" (which is nearly unfalsifiable — some distortion is
   certain).
3. **Remove legionellosis.** See above.
4. **"49 placeholders" as a defect.** They are the repository's deliberate convention for
   applicant-only facts, catalogued in `placeholders.md` with owners; the audit is right that
   none may survive into the submitted PDF, and that was already the plan.
5. **Em-dash count (139)** — noted, no action; a style preference, not a rule.

## The audit's claims checked against the repository

- Missing bibliography entries: **confirmed** (5 of 5) — the one genuinely new defect found.
- Xu 2023 mis-key: **confirmed**, though our own entry already carried the fix instruction.
- Host tense contradiction: **confirmed**.
- Zheng et al. non-consortium: already flagged by us; unchanged (flag stands).
- "Proposal claims host confirmation signed while table says requested": partially right —
  wording, not the table, was at fault; fixed.
- Its USGS/Sci Rep 2023 prior-art citation: **not verifiable from this environment** (network
  egress blocks); incorporated as a `[[cite examples — verify]]` marker rather than a citation.

## Where this leaves the dossier

The plan at 59,995/60,000 with the audit's three "essential" scientific changes in place
(novelty narrowed; outcome scoped; episode-level powering stated). The submission blockers are
unchanged and unchanged in ownership: placeholders, letters, statuses, bibliography completion,
the mySNF count — all listed in `final-quality-audit.md` §4 and `TODO.md`.
