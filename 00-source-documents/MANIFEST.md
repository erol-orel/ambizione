# Source documents

## `call-documents/` — three obtained

The applicant supplied these on 19 August 2026. `snf.ch` is blocked by this session's network
egress proxy, so they could not be downloaded here.

| File | Version | Status |
| --- | --- | --- |
| `ambizione_guidelines.pdf` | 11.08.2026 | **Read in full.** Page/character limits, prescribed research-plan structure, mobility form, CV route, timeline |
| `ambizione_reglement_e.pdf` | 25.02.2026 | **Read in full.** Eligibility (Art. 5), mobility (Art. 9), eligible costs (Art. 10–12), assessment criteria (Art. 15) |
| `ambizione_confirmation_institution_e.pdf` | 03.08.2026 | **Read in full.** The two confirmation letter templates |

Findings and every change they forced are in `05-review/snsf-compliance-audit.md`.

## Still worth having

| File | Where | Why |
| --- | --- | --- |
| `snsf_cv_template` | portal.snf.ch | The CV is now compiled **on the SNSF Portal** to a fixed template and uploaded as PDF. ORCID required, public profile sent to reviewers. `cv-narratives/` is input to it, not a substitute |
| `general_implementation_regulations.pdf` | SNSF funding regulations | Clause 1.11 (eligibility-window extensions), Clause 2.8 (CHF 100,000 cap on equipment), Clause 7 (staff) |
| `evaluation_procedure` | SNSF → how we select | Two phases; **Life Sciences interviews 3–4 June 2027** |
| `unige_internal_deadline` | research-grants-office@unige.ch | The binding deadline. UNIGE sets its own, well before 3 November |
| Mobility form | mySNF | The statement of mobility is a **provided form**, five dimensions, Adobe Acrobat only |

**No longer needed:** a cover letter and career plan are *not* required — uploaded files are
deleted (Guidelines 2.13).

## Download

```sh
sh 00-source-documents/fetch-call-documents.sh
```

The two UNIGE items need manual saving — the page is HTML, and the internal deadline has to come
from the grants office by email.

## `my-materials/` — already in the repo

| File | What it is |
| --- | --- |
| `cv-orel-current.pdf` | Current CV and publication list. **Note: this is a classic CV. The SNSF requires the narrative format — it is a rewrite, not a reformat.** See `04-other-documents/cv-and-output-list.md`. |
| `legionella-protocol-v1.4-ccer.docx` | CCER research protocol v1.4 (05.05.2026), cantonal Legionella project. |
| `legionella-basec-2026-00324-form.pdf` | BASEC 2026-00324 application form — ethics status, funders, data sources. |
| `gesica-interreg-application-form.pdf` | GESICA Interreg VI France–Suisse application (Sept 2024 – Feb 2027). Partners, objectives, work plan. |
| `gesica-social-media-data-sources-report.pdf` | GESICA report on social media data sources for weak-signal detection. |
| `gesica-disease-model-source-table.xlsx` | GESICA reference table: 76 notifiable diseases classified into 8 model classes, 22 Geneva/Vaud surveillance sources with latency and access, and the disease × source matrix. |
| `gesica-data-foundation-report.docx` | GESICA report on the respiratory disease scope, variables of interest and data sources for Geneva and Vaud. |
| `ai-in-ems-systematic-review-2026.pdf` | AI in Emergency Medical Services systematic review (submitted Feb 2026), Orel 3rd author, LiteRev used in the methods. |

## Related repositories

- **`github.com/erol-orel/LiteRev-Evidence`** — the platform behind literev-scenario.com.
  Deliberately *not* vendored here: separate project, own history, and its git history contains
  credential material. Assessed in `03-research-plan/literev-evidence-assessment.md`.

## Still to add

- [ ] **Written data-access commitments: HUG ED, 144/CASU, ICU occupancy.** The load-bearing
      assumption of Candidate D — see `03-research-plan/candidate-D-crisis-forecasting.md`
- [ ] The Horizon proposal's final submitted version, for the overlap declaration
- [ ] Ambizione applications from UNIGE colleagues that were funded (ask the ISG and the grants office — this is normal and the best single reference you can get)
- [ ] Your PhD thesis defence certificate with the exact date
- [ ] SIG / OCEN / cantonal doctor data agreements and letters of support
- [ ] The 2017 Geneva outbreak investigation report, if obtainable
- [ ] SwissLEGIO protocol and published output
