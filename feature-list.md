# Feature list: Pre-Interview Screening and Verification Pipeline

The detailed list of features to design the mock-up from, and later to build. It expands the acceptance criteria in `Python Programming - HR Analysis.docx` and uses what we learned in [`research/competitor-analysis.md`](research/competitor-analysis.md).

## Decisions this list is built on

| Question | Decision | Effect |
|---|---|---|
| Who is the customer? | **SME in-house HR** (segment A): a company with 50 to 500 staff and one or two recruiters hiring for their own roles | One company per workspace, no client accounts |
| How are must-haves set? | **Paste the job description.** AI suggests must-haves from the closed list of types; the recruiter edits and confirms | New feature R-2 |
| What do candidates see? | **A simple upload page** reached from an email link. No account, no login | Candidates appear in only two screens |
| How are claims verified? | **Document upload + recruiter review**, **GitHub check**, **reference contact form** | The reference form contradicts the spec's non-goal "No contacting former employers or universities". It is listed here as a stretch feature, and the spec needs updating if we keep it |

## How to read this list

- **Priority:** **MVP** = in the 2-week build. **Stretch** = if time allows. **Later** = after the course, noted so the design leaves room for it.
- **Spec** column: the acceptance criterion it comes from, as section + item number (e.g. C2 = section C, second item). "New" means it is not in the spec yet.
- **The rule behind everything:** the system flags, drafts and organises; a named recruiter confirms every shortlist, every verified item and every rejection message. Nothing ranks or scores candidates.

---

## 1. Users and access

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| U-1 | Recruiter login with a named account | MVP | D1, G2 | Needed so every confirmation in the audit log has a person's name |
| U-2 | Two user types: **Recruiter** (does everything) and **HR lead** (dashboard and audit log, read-only on candidates) | MVP | New | Keeps the buyer's view (dashboard) separate from the daily user's |
| U-3 | Company settings: retention period (days), reminder delay (days), sender name and email | MVP | E4, G1 | Defaults: 30-day retention, 3-day reminder |
| U-4 | Hiring manager read-only view of interview-ready candidates | Later | New | Hiring managers are the "consumer of the output" in the niche brief |

## 2. Role setup

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| R-1 | Create a role: title, department, location, closing date | MVP | A1 | |
| R-2 | **Paste the job description → AI suggests must-haves.** Each suggestion has a type from the closed list (years of experience, degree level, required skill, certification, language), a value (e.g. "5 years", "Bachelor's, First Class Honours", "Python") and the sentence from the job description it came from | MVP | New | The recruiter must accept, edit or delete every suggestion. Nothing is saved without confirmation |
| R-3 | Add or edit must-haves by hand, using the same closed list of types | MVP | A2 | Also the fallback when the AI suggestion fails |
| R-4 | Mark criteria as **must-have** or **nice-to-have** | Stretch | New | Nice-to-haves are shown but never cause a "missing" flag |
| R-5 | **Verification list** per role: which claim types need proof (degree, certification, employment, GitHub, reference) | MVP | A1, E1 | Pre-filled from the must-haves, editable |
| R-6 | Block saving a role with zero must-haves | MVP | A1 | Validation error |
| R-7 | Block criteria that mention protected characteristics (age, gender, nationality, marital or family status, etc.) | MVP | A2 | Deterministic word check, also applied to AI suggestions |
| R-8 | Role status: draft → open → closed | MVP | G1 | Closing starts the retention countdown |

## 3. Applicant intake

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| I-1 | Upload CVs to a role (PDF, DOCX or pasted text), one or many at once | MVP | B1 | Fixtures are synthetic CVs |
| I-2 | **CSV import** from another ATS or a spreadsheet (name, email, CV text or file name) | MVP | B3 | Rows with missing columns are listed back with the reason and not imported |
| I-3 | Add one candidate by hand | Stretch | New | |
| I-4 | Flag a likely duplicate (same email in the same role) | Stretch | New | Warn only, never merge automatically |
| I-5 | Public apply form or job-board posting | Later | — | Out of scope: we work alongside the company's ATS |

## 4. CV reading (claim extraction)

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| X-1 | AI extracts structured claims: degrees (level, subject, classification, university, year), jobs (title, employer, dates), certifications, skills, languages, GitHub link | MVP | B1 | Must match the fixtures' expected JSON exactly |
| X-2 | **Remove personal details before sending text to the AI** (name, email, phone, address) | MVP | G3 | A test checks the outgoing text |
| X-3 | Extraction fails or returns broken JSON → candidate marked **"needs manual entry"**, never screened out | MVP | B2 | |
| X-4 | Recruiter can view and correct the extracted claims next to the CV | MVP | New | Corrections are logged |
| X-5 | Years of experience are calculated from job dates, and the working is shown (e.g. "2019–2022 + 2022–2025 = 6 years") | MVP | C1 | Makes the "at least 5 years" check easy to explain |

## 5. Screening (flags, not decisions)

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| S-1 | Each must-have gets a result: **meets**, **missing** or **needs human review**, with a one-line reason and the CV text it relied on | MVP | C1, C2 | Reason + quote idea taken from Ashby |
| S-2 | Overall result: **"meets all must-haves"**, **"missing: [criterion]"** or **"needs human review"**. Never "rejected" | MVP | C1 | |
| S-3 | Unclear claims (e.g. "5 years in data" for a "Python developer" criterion) → "needs human review" | MVP | C2 | |
| S-4 | Same claims → same result regardless of name, age or nationality | MVP | C3 | Paired-fixture test |
| S-5 | Candidate list per role, **filtered** by status. Sorted only by date applied or name, never by a score | MVP | Non-goal | No "best match first" view on purpose |
| S-6 | Re-run screening after the recruiter edits criteria or claims | Stretch | New | Old result kept in the audit log |

## 6. Shortlist (human gate 1)

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| H-1 | Recruiter confirms a candidate onto the shortlist. Name and time are recorded | MVP | D1 | Nobody gets a proof request before this |
| H-2 | Shortlist a candidate flagged "missing" → **written reason required** | MVP | D2 | Shown on the candidate and in the audit log |
| H-3 | Confirm several candidates at once (each still logged separately) | Stretch | New | |

## 7. Verification (proof of claims)

### 7a. Requests and the candidate upload page

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| V-1 | When shortlisted, the system creates **one proof request per claim type** in the role's verification list, and no others | MVP | E1 | E.g. degree certificate for "First Class Honours" |
| V-2 | Candidate gets an email with a **secure, expiring link** | MVP | E1 | No account needed |
| V-3 | **Candidate upload page:** lists each item requested and **why** ("This role requires a Bachelor's with First Class Honours, as stated on your CV"), accepted file types, size limit, and a privacy note on how long files are kept | MVP | E3 | Answers the candidate user story: "know exactly which documents are requested and why" |
| V-4 | Candidate can upload, replace before review, and see each item's status (requested / received / verified) | MVP | E3 | |
| V-5 | **One reminder** after N days, then the item is marked **"no response"** and flagged for the recruiter | Stretch | E4 | Spec marks this as stretch; it is the core of "no chasing" |

### 7b. Checking (human gate 2)

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| V-6 | **Review queue:** the uploaded document beside the claim it should prove. Recruiter marks it **verified** or **failed**, with a note | MVP | E3 | No item reaches "verified" without a recruiter |
| V-7 | **GitHub check:** profile not found → "failed: not found"; profile exists → "pending human review"; API error or rate limit → "check unavailable, retry" (never "failed") | MVP | E2 | Tested against a fake GitHub API |
| V-8 | **Reference contact form:** candidate gives a referee's name and work email; the referee gets a short form to confirm job title and dates (yes / no / correction); the recruiter reviews the answer | Stretch | **Conflicts with non-goal** | Needs: candidate consent, a referee privacy note, no free-text opinions about the candidate. Update the spec's non-goal before building |
| V-9 | **Interview-ready:** only when every required item is verified by a human. Otherwise needs a recorded override with a reason | MVP | E5 | |
| V-10 | Official degree-check codes (Spanish ministry code, UK HEDD) as an alternative proof | Later | New | From the competitor research |

## 8. Feedback to unsuccessful candidates (human gate 3)

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| F-1 | Recruiter marks a candidate **unsuccessful** at any stage | MVP | F1 | |
| F-2 | System **drafts feedback** that cites only the role's job-related criteria recorded as unmet or unverified. E.g. "This role requires at least 5 years of experience in data engineering; your CV shows 3 years." | MVP | F1 | No mention of other candidates, ranking or protected characteristics |
| F-3 | **Nothing is sent until a recruiter approves it.** Editing before approval is allowed; the approved version is stored | MVP | F2 | |
| F-4 | No recorded unmet criteria (e.g. role filled) → **neutral status message**, no invented reasons | Stretch | F3 | |
| F-5 | **Safety check on every draft:** blocked and flagged if it mentions a protected characteristic or a reason not in the screening record | Stretch | F4 | Deterministic check, tested with fixtures. Strongly recommended, since this is our difference from Lever's automatic feedback |
| F-6 | Approve and send several messages at once (each still logged) | Later | New | |

## 9. Dashboard and insights (totals only)

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| D-1 | **Pipeline per role:** number of candidates at each stage (applied → screened → shortlisted → proof requested → verified → interview-ready; unsuccessful → feedback sent). Counts add up to total applications | MVP | H1 | |
| D-2 | **Most common missing must-haves** per role, with counts | MVP | H2 | Helps HR see if a requirement is unrealistic |
| D-3 | **No individual scores, rankings or protected characteristics** anywhere on the dashboard | MVP | H3 | Test checks the data holds only counts, rates and durations |
| D-4 | Overview across all open roles (applications, shortlisted, interview-ready) | MVP | New | The HR lead's landing page |
| D-5 | Proof response rate and median time from shortlist to interview-ready | Stretch | H4 | The "time saved" story for the buyer |
| D-6 | Hide figures for groups under 5 candidates | Stretch | H5 | |
| D-7 | Feedback stats: share of unsuccessful candidates who received specific feedback | Stretch | New | Shows the candidate-experience benefit |
| D-8 | Export dashboard figures to CSV | Later | New | |

## 10. Privacy, audit and transparency

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| P-1 | **Audit log:** every status change (shortlisted, verified, failed, override, unsuccessful, feedback approved and sent) with who, what and when. Cannot be edited | MVP | G2 | Readable by HR lead and recruiter |
| P-2 | **Retention:** after a role closes and the retention period passes, CVs, documents and extracted personal data are deleted. The audit log keeps only candidate ID, actions, times and users | MVP | G1 | |
| P-3 | Personal details removed before any AI call | MVP | G3 | Same as X-2 |
| P-4 | Notice on the upload page that AI helped flag claims and that a person made every decision | Stretch | New | EU AI Act transparency; idea from Ashby |
| P-5 | Label showing all demo data is synthetic | MVP | Non-goal | |

## 11. Emails

| ID | Feature | Priority | Spec | Notes |
|---|---|---|---|---|
| E-1 | Proof request email with the secure link | MVP | E1 | |
| E-2 | Reminder email | Stretch | E4 | |
| E-3 | Approved feedback email | MVP | F2 | |
| E-4 | Referee form email | Stretch | V-8 | |
| E-5 | Emails go to a fake inbox in the demo and tests, not real addresses | MVP | Contracts | |

---

## Candidate journey (updated state machine)

```text
applied → screened (flags) → shortlisted (human) → proof requested
   → items received → each item verified (human) → interview-ready
                         ↘ failed / no response → recruiter decides (override with reason, or unsuccessful)

unsuccessful (human, any stage) → feedback drafted → safety check → approved (human) → sent
```

Proof items for one candidate: document upload, GitHub check, reference form (stretch). Each item has its own state: requested → received → pending review → verified / failed / no response / check unavailable.

---

## Screens for the mock-up

**Recruiter and HR lead (web app)**

1. **Dashboard:** overview of open roles, pipeline counts, most common missing must-haves (D-1, D-2, D-4)
2. **Roles list:** open, draft and closed roles with counts
3. **Create or edit role:** paste the job description → accept, edit or delete suggested must-haves → verification list (R-1 to R-8)
4. **Add applicants:** CV upload and CSV import with error list (I-1, I-2)
5. **Role pipeline:** candidate list filtered by status, never ranked (S-5)
6. **Candidate detail:** CV beside extracted claims, result per criterion with reason and quote, shortlist / unsuccessful buttons, override reason (X-4, S-1, H-1, H-2)
7. **Verification review queue:** document beside claim, verify / fail with note, GitHub result (V-6, V-7)
8. **Feedback review:** draft, safety-check result, edit, approve and send (F-2, F-3, F-5)
9. **Audit log** (P-1)
10. **Settings** (U-3)

**Candidate and referee (no login)**

11. **Candidate upload page** (V-3, V-4)
12. **Referee confirmation form** (V-8, stretch)

---

## Count and scope check

| Priority | Number of features |
|---|---|
| MVP | 45 |
| Stretch | 15 |
| Later | 5 |

That is more than the spec's ~22 MVP acceptance criteria, because one criterion often needs several screen features. Two new MVP items add real work: **R-2** (paste the job description) and **U-2** (two user types). If time runs short, cut in this order: U-2 (one user type only), D-4, X-5's working shown, then R-2 back to the manual form (R-3).

## Open points before building

1. **Spec update:** change the non-goal "No contacting former employers or universities" to allow the referee form (V-8) with consent, or drop V-8.
2. **Spec update:** add R-2 (paste the job description) and U-2 (HR lead user type) as acceptance criteria.
3. **Language** of the interface: English only, or English and Spanish? (Target customers are in Spain.)
4. **Mock-up format:** clickable HTML prototype, or static screens?
