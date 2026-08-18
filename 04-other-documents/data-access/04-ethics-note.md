# Ethics — start in parallel, not after

## Why now

Two reasons, and the second is the one people miss.

**Practical.** A CCER submission takes months. If the grant starts in late 2027 and ethics has not
begun, WP3's data assembly slips and the milestone at M20 is at risk. Referees who know the Swiss
system will do this arithmetic.

**Evidential.** Being the **applicant** on your own ethics submission is one of the most concrete
demonstrations of independence available to you. On BASEC 2026-00324 you are the data lead and
Prof. Keiser is project leader and sponsor. A submission where you hold both roles is a fact a
referee can check, and it says more than any sentence in §5 can.

## Scope

`[[Confirm with the CCER and the UNIGE data protection officer.]]`

The project needs **aggregated daily counts**, not individual-level clinical data, for WP3 and
WP4. This may place it in a lighter category than the Legionella study, which required
address-level linkage. Establish this early — the answer changes both the timeline and the
feasibility argument in the research plan, and if a daily aggregate avoids individual-level
approval it is worth one sentence in §6.

The prospective shadow-mode component (T4.4) needs separate consideration: forecasts are recorded
and not used for decisions, which should place it outside interventional research, but it should
be declared in the submission rather than added later.

## The precondition nobody will raise until it blocks you

The data-protection review will ask how the data is stored, transmitted and recovered. The
LiteRev-Evidence platform currently `[[at time of writing]]` serves over plain HTTP, keeps secrets
in a systemd override, and has no working migration path for its schema — and its own audit
records an API key printed into a public CI log.

**Fix this before the ethics submission, not after it is rejected.** The work is roughly:

- [ ] Rotate the exposed credential; confirm repository visibility
- [ ] TLS on the live host; secrets into a managed store
- [ ] Schema under Alembic; unique constraints; documented recovery procedure
- [ ] A short written description of the security posture, reusable in both the CCER submission
      and §6 of the research plan

Done, this stops being a liability and becomes a sentence you want in the proposal: audited,
reproducible infrastructure already handling a six-figure corpus, ready to receive sensitive
operational data.

## Sequence

| When | What |
| --- | --- |
| Now | Confirm scope and category with CCER / DPO; begin hardening |
| Sept | Support letters in hand; hardening complete |
| Oct | Security description written into §6; CCER submission drafted |
| After the decision | Submit CCER with yourself as applicant |
