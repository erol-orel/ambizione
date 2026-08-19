# Eligibility verification — RESOLVED

**Confirmed with the UNIGE Research Office (RGO): the applicant is eligible, and there is
no mobility requirement.**

Both open questions are closed. The clause that worried me — twelve months of research at a
higher education institution other than the doctoral one — does **not** apply to Ambizione. It
belongs to Postdoc.Mobility, or is a garbled rendering of the connection-to-Switzerland criterion.
I could not verify this myself: `www.snf.ch` and every university mirror are blocked by this
environment's network egress proxy, which runs a fixed allowlist. The RGO settled it.

## Consequences

1. **No research stay is proposed.** The mobility documents previously carried an outgoing stay
   built to satisfy a requirement that does not exist. It is removed everywhere — no candidate
   hosts, no invitation letter, no budget line. `statement-of-mobility.md` now leads with the
   sectoral and intellectual arguments and states the geographic position plainly.
2. **The institutional claim is organisational**: leading an independent research programme within
   the Institute rather than remaining a member of an existing group. That has to be established
   by the host letter, not asserted in the applicant's own prose.

## Still worth checking against the call documents

Not blocking, but the call documents have still never been read directly, and the repository
carries several `[VERIFY]` claims that were taken from secondary sources:

```
sh 00-source-documents/fetch-call-documents.sh
```

| Claim in the repository | Where |
| --- | --- |
| 15 pages / 60,000 characters including spaces, bibliography excluded | Applies to every character-budget decision made so far |
| CHF 250,000 project funds over four years; salary separate | §6.3, budget |
| Doctoral students and postdocs cannot be employed | §4 staffing, §6.3, all emails |
| Two host confirmations: detailed and general | `host-institution-letters.md` |
| Each host or contact person may support only one Ambizione applicant in this call | Corroborated across several university pages; confirm with the Institute that nobody else is being supported under the same signatory |

The last row is the only one with a real chance of an unpleasant surprise, and it is a question
for the Institute rather than for the documents.
