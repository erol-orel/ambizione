# To do — Ambizione, deadline 3 November 2026

**Today: 19 August 2026.** Target submission **30 October** to preserve a buffer before the SNSF deadline of 3 November at 17:00 CET.

Ordered by what blocks what. The critical-path items depend on other people saying yes; everything else is under your control.

---

## Immediate / critical path

- [ ] **⚠ CRITICAL PATH — Send the data-access requests.** HUG emergency (Desmettre), 144/CASU (Larribau), ICU. Ask for letters of support, not data, and ask whether daily aggregate extracts avoid individual-level approval requirements.
- [ ] **⚠ CRITICAL PATH — Settle the host.** Confirm DS4DH as primary host and whether an associated ISG affiliation is formally possible; obtain the required institutional confirmation.
- [ ] **⚠ CRITICAL PATH — Secure the mobility host.** Contact Prof. Valérie Chavez-Demoulin (UNIL) and obtain a concrete invitation/hosting statement for the planned stay.
- [ ] Confirm multi-canton case-data availability. If unavailable, keep the design on Geneva/open surveillance and do not imply broader access.

## Scientific lock

- [ ] Fix the **primary outcome series and forecast horizon** for H3a.
- [ ] Fix the **real-time onset rule** and **cold-start window `[[N]]`** before any historical evaluation design is finalised.
- [ ] Fix the **H3b non-inferiority margin `[[Δ]]`** before evaluation and justify it against the rung 3 → rung 4 effect size.
- [ ] Complete the H1 benchmark sample-size simulation (`[[n]]`, `[[τ² range]]`, variance-ratio threshold).
- [ ] Complete C2 recovery/calibration thresholds and the H3c secondary criterion.
- [ ] Specify the registered analysis-plan location.
- [ ] Run the novelty audit: search specifically for prior work combining literature-derived quantitative priors, cold-start crisis forecasting and latent/regime state representations. If a precedent exists, state the distinction rather than defending an absolute novelty claim.
- [ ] Verify every citation against the publisher record; do not rely on repository-generated reference metadata without checking.

## Budget / scheme compliance

The 2026 Ambizione rules are now reflected in the research plan: **no doctoral student or postdoc is budgeted**. Project funds are capped at **CHF 250,000 over four years**. If personnel support is needed, request only eligible **other-employee** support for bounded technical/extraction work.

- [ ] Email `research-grants-office@unige.ch` for the UNIGE internal deadline, internal proposal review, institutional salary rates for eligible other employees, and final budget-entry guidance.
- [ ] Build the final four-year project budget in official SNSF categories; keep total project funds ≤ CHF 250,000 and exclude non-eligible normal institutional operations.
- [ ] Declare the cantonal Legionella funding and any other significant related funding in mySNF.
- [ ] Check whether any planned open-access costs belong in a separate SNSF mechanism rather than the Ambizione project budget.

## Application documents

- [ ] Fill every remaining `[[…]]` in the research plan, especially sections 2, 4, 5 and 6.
- [ ] Finalise CV narratives and contribution statements for the major outputs, especially the *Nature Communications* paper.
- [ ] Answer the CV questions on co-supervision and peer-review record.
- [ ] Finish the statement of mobility only after the host is confirmed; make it a scientific/independence argument, not a travel history.
- [ ] Obtain host-institution and data-access letters.
- [ ] Prepare CCER submission with yourself as applicant if required for the operational data.
- [ ] Confirm secure computing/HPC access and the data-security arrangement before connecting clinical data.
- [ ] Deposit a versioned LiteRev-Evidence release on Zenodo if the repository/software claims will be presented as durable outputs.

## External review

- [ ] Send the full dossier around 22 September to 2–3 readers: one in-field senior colleague, one out-of-field reader, and one grants-office/former-panel reader.
- [ ] Ask specifically: (1) can they state H3a after reading the summary? (2) can they identify the primary comparison? (3) do they believe the project is feasible with the named resources? (4) do they see an independence problem?
- [ ] Run `05-review/hypothesis-audit.md` end to end and eliminate any claim that cannot be operationalised.
- [ ] Run `05-review/self-assessment.md` end to end; any score below 4 needs a concrete fix.

## Final build / submission

- [ ] Re-run the figure generator and assembly script from the committed sources; verify both are idempotent.
- [ ] Verify page/character limits against the **2026 call documents**, not an assumed limit.
- [ ] Verify font, spacing, single-PDF and no-annex requirements.
- [ ] Enter the final dossier in mySNF, including DMP, budget and relations/related-project declarations.
- [ ] Declare GESICA and the Horizon consortium where required and explain the delimitation from the Ambizione project.
- [ ] Final consistency audit: research plan ↔ budget ↔ CV ↔ mobility ↔ host letter ↔ data letters.
- [ ] Target submission ~30 October; absolute SNSF deadline: **3 November 2026, 17:00 CET**.

## Decisions still open

1. Primary host — DS4DH vs any alternative formal arrangement.
2. Associated ISG affiliation and exact role of HUG collaborators.
3. Mobility host and scientific scope of the stay.
4. Primary outcome series and horizon for H3a.
5. `[[N]]` cold-start window and real-time onset rule.
6. `[[Δ]]` non-inferiority margin.
7. Amount and duration of eligible other-employee support, if any.
8. Whether the Legionella extension remains in the final four-year plan.

## Where things are

| | |
| --- | --- |
| Research plan (assembled) | `03-research-plan/FINAL-research-plan.md` |
| Hypothesis audit | `05-review/hypothesis-audit.md` |
| Research plan sources | `03-research-plan/draft/` — then `sh draft/assemble.sh` |
| Figures | `03-research-plan/draft/figures/` |
| Budget | `04-other-documents/budget.md` |
| CV narratives + output list | `04-other-documents/cv-narratives/` |
| Statement of mobility | `04-other-documents/statement-of-mobility-draft.md` |
| Data-access package | `04-other-documents/data-access/` |
| Host decision | `02-profile/host-decision.md` |
| Literature to strengthen | `03-research-plan/literature-to-strengthen.md` |
| Pre-submission review | `05-review/self-assessment.md` |
