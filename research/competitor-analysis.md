# Competitor analysis: Pre-Interview Screening and Verification Pipeline

Step 7 of [`audience-analysis-steps.md`](audience-analysis-steps.md). Read [`niche_brief.md`](niche_brief.md) first.

**Date researched:** 3 November 2026.
**Method:** web search plus reading vendor pages. Most statements below come from the vendors' own marketing or help pages, so they say what a product *claims* to do, not what it does well. Prices are left out on purpose: none were confirmed from a pricing page, and they go in `competitors.csv` once opened (see "Next steps").

**How sure each statement is**

| Mark | Meaning |
|---|---|
| ✅ | Confirmed on the vendor's own page or a primary source during this research |
| ⚠️ | Partly, or only for some plans, sectors or countries |
| ❌ | Not offered, according to the sources read |
| ❓ | Not checked yet |
| (gk) | From general knowledge, not checked for this document |

---

## 1. Key findings

1. **Screening against must-have criteria is no longer unique.** Ashby's AI-Assisted Application Review already works almost exactly like our spec: the hiring team defines criteria, the AI marks each one "Meets" or "Does not meet" with a reason, and "it is up to the reviewer to advance or reject" ([Ashby](https://www.ashbyhq.com/blog/product/ai-assisted-application-review)). Factorial (Spain) and Teamtailor also offer AI CV screening. Our screening step on its own is not a reason to buy.
2. **Personalised rejection feedback exists, but sent automatically.** Employ's AI Screening Companion (inside Lever) says "rejected candidates automatically receive personalized feedback" ([Employ](https://www.employinc.com/blog/introducing-ai-screening-companion-your-built-in-assistant-for-smarter-faster-screening/)). We found no mention of a recruiter approving it first. Our difference is **recruiter-approved feedback that may only cite recorded, job-related unmet criteria**, which matters under GDPR Article 22 and the EU AI Act.
3. **Claim verification is a separate market.** Background-screening firms (First Advantage/Sterling, HireRight, Checkr, Zinc, Veremark, Certn) and sector tools (Credentially in healthcare) verify degrees, employment and ID. They usually start **after** a hiring decision or at offer stage, and sit outside the screening step, connected through ATS integrations.
4. **The gap that still looks open:** one lightweight flow that joins
   screening → human shortlist → proof requested **only after shortlist** → human-verified → interview-ready, plus recruiter-approved feedback and a process dashboard,
   aimed at **SMEs and agencies in Spain**. This is a candidate gap, not proof of demand. Interviews (step 6) have to confirm someone feels the pain.
5. **Free official degree checks exist and we can use them.** Spain's Ministry runs a free *Consulta de Títulos Universitarios Oficiales*: the graduate creates an authorisation code and the employer checks the degree with it ([Ministerio](https://www.ciencia.gob.es/Universidades/ConsultaTitulos.html)). The UK has HEDD, which confirms the degree classification (e.g. First Class Honours) with the candidate's consent ([HEDD](https://hedd.ac.uk/faq)). Our proof request could ask for a code instead of a scanned certificate. That is faster and harder to fake than a PDF.

---

## 2. Category A: ATS platforms with AI screening

These are the "ATS" products our web app is compared with. They own the job posting, the pipeline and the reporting. Our plan is to work **alongside** them (CSV import), not to replace them.

### Ashby — [ashbyhq.com](https://www.ashbyhq.com)
- **What it is:** an all-in-one recruiting platform (ATS, CRM, scheduling, analytics), popular with tech companies.
- **AI screening:** ✅ AI-Assisted Application Review. Job-level criteria; each criterion marked "Meets" / "Does not meet" with rationale and citations; "unknown" when the AI can't tell; unreadable CVs are "skipped". Opt-in in admin settings.
- **Human in the loop:** ✅ "It's ultimately the qualified humans on your team making an advance/reject decision." Reviewers can flag and override AI results.
- **Fairness and privacy:** ✅ third-party bias audit (supported by FairNow) with public results; PII redacted before AI processing; warnings about vague or EEO-risky criteria; applicants can opt out of AI processing.
- **Verification of claims:** ❓ not found; normally done by partners (gk).
- **Candidate feedback:** ❌ not mentioned in the feature announcement.
- **What it means for us:** the closest match to our screening design. Copy their good ideas (rationale per criterion, "unknown" state, PII redaction), and compete on the parts they don't cover.

### Greenhouse — [greenhouse.com](https://www.greenhouse.com)
- **What it is:** a structured-hiring ATS for mid-sized and large companies.
- **AI screening:** ⚠️ "Talent Matching" and candidate match scores are reported on its roadmap; Greenhouse says these are audited monthly for bias by Warden AI ([AI Act blog](https://www.aiactblog.nl/en/posts/ai-act-greenhouse-classification)). Not confirmed on Greenhouse's own pages for this document.
- **Verification:** handed to background-check partners through integrations (gk).
- **Dashboard:** ✅ (gk) strong reporting on pipeline and time to hire.
- **What it means for us:** match *scores* are something our spec explicitly avoids. That difference is useful in the pitch to risk-averse EU buyers.

### Lever + Employ AI Screening Companion — [lever.co](https://www.lever.co) · [employinc.com](https://www.employinc.com/ai-screening-companion/)
- **What it is:** Lever is an ATS owned by Employ (which also owns JazzHR and Jobvite).
- **AI screening:** ✅ the AI Screening Companion (announced November 2025) "surfaces the best matches for review".
- **Candidate feedback:** ✅ "automatically provides personalized feedback to rejected candidates". ❓ No mention of a recruiter approving it before it is sent.
- **Verification:** ⚠️ fraud detection and automated reference checks are announced for a future "Candidate Insights" product, not the current companion.
- **Availability:** ✅ fully available on Lever; Employ planned a standalone version by mid-2026 ([Hackett Group analysis](https://www.employinc.com/wp-content/uploads/2026/01/Employs-AI-Screening-Companion-Drives-Improved-Recruiting-Outcomes.pdf)). Not confirmed for JazzHR.
- **What it means for us:** **the most direct competitor for the feedback feature.** Our angle is approval before sending, plus a deterministic check that blocks drafts mentioning protected characteristics or reasons not in the screening record.

### Workable — [workable.com](https://www.workable.com)
- **What it is:** an ATS for small and mid-sized companies, sold in Europe.
- **AI screening:** ⚠️ a buyer's guide reports 0–100 scores against an "ideal candidate profile" ([HeroHunt](https://www.herohunt.ai/blog/best-ai-candidate-screening-software-2026-10-compared/)). Not confirmed on Workable's own pages.
- **Candidate feedback, verification:** ❓ not checked.
- **What it means for us:** same SME buyer as segment A. A numeric score is the kind of ranking our spec rules out.

### Teamtailor — [teamtailor.com](https://www.teamtailor.com)
- **What it is:** an ATS with a strong employer-branding career site, Swedish, widely used by European SMEs.
- **AI screening:** ✅ Co-pilot summarises each CV in five bullet points and suggests matching candidates from the database (only those who consented to future jobs) ([Teamtailor help](https://support.teamtailor.com/en/articles/9424192-co-pilot-candidate-suggestions)). ⚠️ A competitor's review says screening is mostly keyword-based ([Hirevire](https://hirevire.com/articles/teamtailor-review), biased source).
- **Setup:** ✅ opt-in add-on, turned on per module by an admin.
- **Verification, feedback:** ❓ not checked.
- **What it means for us:** has a marketplace, so it's a possible **channel** for an add-on, as named in step 13 of the steps file.

### Factorial — [factorial.es](https://factorial.es/software-reclutamiento-seleccion-personal-ats)
- **What it is:** an HR platform from Barcelona for SMEs (payroll, time off, ATS). Strong in Spain, Portugal and Brazil.
- **AI screening:** ✅ AI analyses CVs, picks out key skills and segments candidates; "AI Top Match" finds the best candidates per role ([Factorial IT](https://factorial.it/recruiting-selezione-personale)). ⚠️ The most advanced AI features are on higher-tier plans ([Upliora](https://www.upliora.es/blog/mejores-herramientas-ia-rrhh-seleccion-personal-ranking-2026)).
- **Verification, feedback:** ❓ not checked.
- **What it means for us:** **the most relevant incumbent for Spanish SMEs (segment A).** Many target customers may already have it, so a CSV import or integration from Factorial is worth planning.

### Personio — [personio.com](https://www.personio.com)
- **What it is:** an HR platform for European SMEs with a recruiting module (gk). Has a marketplace for partner apps (gk).
- **AI screening, verification, feedback:** ❓ not checked.
- **What it means for us:** another possible channel, named in step 13.

---

## 3. Category B: background screening and verification providers

They check claims (degree, employment, ID, criminal record). They usually do **not** screen CVs against the job or write feedback.

### First Advantage (now including Sterling) — [fadv.com](https://www.fadv.com)
- **What it is:** one of the largest global screening companies. It agreed to buy Sterling Check for about $2.2 billion in February 2024 ([HRO Today](https://www.hrotoday.com/news/first-advantage-to-acquire-sterling-check-corp-for-2-2-billion/)). Sterling's candidate portals still run separately ([First Advantage](https://fast.fadv.com/)).
- **Checks:** ✅ screening, identity and verification; investing in AI and digital ID (from the deal announcement).
- **What it means for us:** enterprise buyers. Too heavy and costly for many SMEs, which leaves room for a lighter tool.

### HireRight — [hireright.com](https://www.hireright.com)
- **What it is:** a large global background-screening provider (gk). Education, employment and criminal checks; integrates with ATSs (gk).
- **What it means for us:** same as First Advantage. Mostly used at offer stage (gk).

### Checkr — [checkr.com](https://checkr.com)
- **What it is:** an API-first background-check company, strongest in the US (gk).
- **What it means for us:** an example of developer-friendly integration. Less relevant for Spain.

### Zinc — [zincwork.com](https://zincwork.com)
- **What it is:** UK-based pre-employment checks.
- **Checks:** ✅ automates candidate document collection and reference follow-ups; uses HMRC data for UK employment verification ([G2](https://g2.com/products/zinc-work/discuss)); claims compliant checks in 190+ countries and ATS/HRIS integrations.
- **What it means for us:** close to our "proof request and reminders" feature, but as a separate screening service, not inside the shortlist step.

### Veremark — [veremark.com](https://www.veremark.com)
- **What it is:** a global background-screening platform with European roots; Series A in April 2024.
- **Checks:** ✅ identity, employment history, references, qualifications ([SAP partner page](https://www.sap.com/cz/products/hcm/partners/veremark-ltd-veremark-background-checks-for-sap-successfactors.html)).
- **What it means for us:** a candidate-friendly, tech-first verification provider. Could be a partner rather than a rival.

### Certn — [certn.co](https://certn.co)
- **What it is:** a Canadian background-check company.
- **Checks:** ⚠️ education, employment, identity, criminal record, sanctions lists ([Techjockey](https://www.techjockey.com/detail/certn), directory listing).
- **What it means for us:** less relevant for Spain.

### Veriff — [veriff.com](https://www.veriff.com)
- **What it is:** an identity-verification company from Estonia (ID document plus selfie) (gk).
- **What it means for us:** only covers "is this person who they say they are", not degrees or experience. ID checks are out of our MVP scope.

---

## 4. Category C: sector-specific onboarding and compliance

### Credentially — [credentially.io](https://www.credentially.io)
- **What it is:** onboarding and compliance software for healthcare (NHS in the UK; also the US).
- **Checks:** ✅ candidates upload documents; OCR reads and checks them; **each candidate is only asked for documents relevant to their role**; alerts before documents expire; can start Checkr and Nursys checks ([Credentially](https://www.credentially.io/features-page/flexible-compliance)).
- **What it means for us:** proof that "ask only for the documents this role needs" is valued, at least in regulated sectors (segment C). It is the closest product to our verification step, but it starts after hiring (onboarding), not before interview.

---

## 5. Category D: official degree-verification services

These are not competitors. They are **sources we can connect to** from the proof-request step.

| Service | Country | How it works | Cost | Link |
|---|---|---|---|---|
| Consulta de Títulos Universitarios Oficiales (RNTUO) | Spain | The graduate creates an authorisation code on the Ministry site; the employer checks the degree with it. Shows the degree, university and dates. Recent graduates may not appear yet. | Free | [ciencia.gob.es](https://www.ciencia.gob.es/Universidades/ConsultaTitulos.html) |
| HEDD (Higher Education Degree Datacheck) | UK | The employer registers, picks the university and requests a check **with the candidate's consent**. Confirms qualification, course, year and **classification** (e.g. First Class Honours). Mismatches go to a manual check, about 5 working days. | About £14 per check at some universities ([Heriot-Watt](https://www.hw.ac.uk/uk/students/studies/record/third-party-verifications-for-employers-and.htm)) | [hedd.ac.uk](https://hedd.ac.uk) |

**Idea for the spec:** for a degree claim, the proof request could offer "upload the certificate" **or** "send your RNTUO authorisation code" (Spain) / "consent to a HEDD check" (UK). The recruiter still confirms the result, which keeps the human gate.

---

## 6. Feature comparison

| Product | Screens CV vs. job criteria | Human makes the decision | Proof requested after shortlist | Verifies claims | Feedback to rejected candidates | Dashboard / analytics | Spain / EU focus |
|---|---|---|---|---|---|---|---|
| **Our app (spec)** | ✅ flags only | ✅ every step | ✅ | ⚠️ human review + GitHub check | ✅ drafted, recruiter-approved | ✅ totals only | ✅ |
| Ashby | ✅ | ✅ | ❓ | ❓ partners | ❌ | ✅ (gk) | ⚠️ |
| Greenhouse | ⚠️ match scores | ❓ | ❓ | ⚠️ partners (gk) | ❓ | ✅ (gk) | ⚠️ |
| Lever + Employ | ✅ | ❓ | ❓ | ⚠️ announced | ✅ automatic | ✅ (gk) | ⚠️ |
| Workable | ⚠️ 0–100 score | ❓ | ❓ | ❓ | ❓ | ✅ (gk) | ✅ |
| Teamtailor | ⚠️ summaries, suggestions | ❓ | ❓ | ❓ | ❓ | ✅ (gk) | ✅ |
| Factorial | ✅ | ❓ | ❓ | ❓ | ❓ | ✅ (gk) | ✅ Spain |
| First Advantage / Sterling | ❌ | — | ⚠️ offer stage (gk) | ✅ | ❌ | ⚠️ (gk) | ⚠️ |
| Zinc | ❌ | — | ⚠️ separate service | ✅ | ❌ | ❓ | ⚠️ UK |
| Veremark | ❌ | — | ⚠️ separate service | ✅ | ❌ | ❓ | ⚠️ |
| Credentially | ❌ | — | ⚠️ onboarding stage | ✅ | ❌ | ❓ | ⚠️ UK, healthcare |

---

## 7. Positioning map

Two axes from step 7: **how well a product fits into the screening step** (left = outside, right = inside) and **how deep it checks claims** (bottom = not at all, top = deep).

```text
                       deep claim checking
                               ▲
   First Advantage/Sterling    │
   HireRight  Zinc  Veremark   │         ← empty corner?
   Certn  Credentially         │           OUR APP: inside the screening step,
                               │           proof after shortlist, human-verified,
                               │           + recruiter-approved feedback
 outside ──────────────────────┼──────────────────────────► inside the screening step
                               │
                               │   Ashby   Lever+Employ
                               │   Factorial  Workable
                               │   Teamtailor  Greenhouse
                               ▼
                         no claim checking
```

Third flag, **drafts specific feedback for rejected candidates:** only Lever + Employ (sent automatically) among the products checked, and our app (recruiter-approved).

---

## 8. What this means for the project

1. **Lead with verification and feedback, not screening.** In the pitch and demo, screening is the expected base, since Ashby and Factorial already do it. The value is "proof collected before interview, no chasing" and "specific, approved feedback".
2. **Stress human approval as the feature.** Lever sends feedback automatically. Workable and Greenhouse use scores. Our spec keeps a human at every gate and never ranks. For EU buyers worried about GDPR Article 22 and the EU AI Act, that is a selling point.
3. **Keep the CSV import.** Factorial, Teamtailor and Personio are probably already used by our target SMEs. Working alongside them is easier to sell than replacing them, and their marketplaces are possible channels.
4. **Consider official degree checks as a stretch criterion.** RNTUO codes (Spain) or HEDD consent (UK) make the "First Class Honours" example stronger than a scanned PDF.
5. **Borrow good ideas from Ashby:** a reason and citation for each criterion result, an "unknown" state (our spec already has "needs human review"), a public bias-test summary, and an AI opt-out for candidates.

---

## 9. Next steps

- [ ] Open each pricing page and fill `research/competitors.csv` (product, pricing URL, price model, date seen), as step 7 requires.
- [ ] Confirm the ❓ cells on vendors' own help pages, especially whether Lever/Employ feedback can be reviewed before sending.
- [ ] Collect public reviews (G2, Capterra) for Ashby, Factorial, Teamtailor and Zinc, and run the feature and rating-gap analysis from step 7. Check whether reviews mentioning "AI" rate lower.
- [ ] Ask interviewees (step 6) which of these tools they use, and whether they already pay for background checks.
- [ ] Check the RNTUO authorisation-code process on the Ministry site itself before adding it to the spec.

---

## Sources

- Ashby, AI-Assisted Application Review: https://www.ashbyhq.com/blog/product/ai-assisted-application-review
- Employ, AI Screening Companion announcement: https://www.employinc.com/blog/introducing-ai-screening-companion-your-built-in-assistant-for-smarter-faster-screening/
- Employ, AI Screening Companion page: https://www.employinc.com/ai-screening-companion/
- Hackett Group analysis of Employ's AI Screening Companion (Jan 2026): https://www.employinc.com/wp-content/uploads/2026/01/Employs-AI-Screening-Companion-Drives-Improved-Recruiting-Outcomes.pdf
- AI Act blog, Greenhouse classification: https://www.aiactblog.nl/en/posts/ai-act-greenhouse-classification
- HeroHunt, AI candidate screening software compared (2026): https://www.herohunt.ai/blog/best-ai-candidate-screening-software-2026-10-compared/
- Teamtailor help, Co-pilot candidate suggestions: https://support.teamtailor.com/en/articles/9424192-co-pilot-candidate-suggestions
- Teamtailor help, Co-pilot overview: https://intercom.help/teamtailor/en/articles/8403166-co-pilot-overview
- Hirevire, Teamtailor review (competitor source): https://hirevire.com/articles/teamtailor-review
- Factorial, recruiting (Italian site): https://factorial.it/recruiting-selezione-personale
- Factorial, ATS (Spanish site): https://factorial.es/software-reclutamiento-seleccion-personal-ats
- Upliora, AI tools for HR in Spain 2026: https://www.upliora.es/blog/mejores-herramientas-ia-rrhh-seleccion-personal-ranking-2026
- HRO Today, First Advantage to acquire Sterling: https://www.hrotoday.com/news/first-advantage-to-acquire-sterling-check-corp-for-2-2-billion/
- First Advantage integration site: https://fast.fadv.com/
- G2, Zinc discussion: https://g2.com/products/zinc-work/discuss
- SAP, Veremark partner page: https://www.sap.com/cz/products/hcm/partners/veremark-ltd-veremark-background-checks-for-sap-successfactors.html
- Techjockey, Certn listing: https://www.techjockey.com/detail/certn
- Credentially, flexible compliance: https://www.credentially.io/features-page/flexible-compliance
- Ministerio de Ciencia, Consulta de Títulos Universitarios Oficiales: https://www.ciencia.gob.es/Universidades/ConsultaTitulos.html
- HEDD FAQ: https://hedd.ac.uk/faq
- Heriot-Watt, third-party verifications (HEDD fee): https://www.hw.ac.uk/uk/students/studies/record/third-party-verifications-for-employers-and.htm
