# Scenarios: when each feature bundle is used

**Kind: simulated (design scenarios).** These are written stories built from the four fictional personas in
[`../personas.yaml`](../personas.yaml) and the user situations US.01–US.24 in
[`../wave1_structure/structure.md`](../wave1_structure/structure.md). They show *when* and *why* a feature is
used, and where it can go wrong. They are not observations of real users, and no number in them is evidence
(session 9, step 11; A6). Every name and CV is synthetic (A13).

Bundles B0–B6 are defined in [`bundles.md`](bundles.md). Each scenario lists the features (ids from
`feature-list.md`), the user situation (US) and the invariant (I1–I5) it touches. "Wave 1" changes W1–W5 are
the ones already built into the prototype ([`../wave1_structure/wave.md`](../wave1_structure/wave.md)).

## The week at a glance

One data engineer role at a 180-person logistics company, 140 applications (the numbers come from Inés's
persona, not from data).

| Day | Who | What happens | Bundle |
|---|---|---|---|
| Mon 09:10 | Inés | Pastes the job description, confirms the must-haves and the proof list | B1 |
| Mon 11:30 | Inés | Imports 140 CVs from the ATS export, runs screening | B2 |
| Mon 15:00 – Tue | Inés | Works through the flags in 20-minute blocks, shortlists 8 | B3 |
| Tue 10:00 | Inés | Previews and sends 8 proof requests | B4 |
| Wed 07:40 | Priya | Uploads her degree certificate on the bus after a night shift | B4 |
| Wed 14:00 | Inés | Checks documents in the verification queue; first candidate is interview-ready | B4 |
| Thu 09:00 | Inés | Marks 60 candidates unsuccessful, approves feedback drafts | B5 |
| Thu 12:30 | Tomasz | Reads his feedback at lunch and asks for a re-check | B5, B0 |
| Fri 08:45 | Daniel | Opens the dashboard 5 minutes before the CEO meeting | B6 |
| +30 days after close | system | Deletes CVs and documents; the audit log keeps only ids and actions | B0 |

---

## B1 · Role setup from the job description

**S1.1 Happy path: a new role on Monday morning.**
- **When:** Inés has a hiring manager's job description in her inbox and 140 applications arriving in the ATS.
- **Steps:** creates the role (R-1, US.05) → pastes the description → "Suggest must-haves" (R-2) → accepts
  "5 years of experience in data engineering", edits "Python" to "Python and SQL", deletes a soft skill that is
  not on the closed list (R-3, US.06) → ticks degree and GitHub on the verification list (R-5, US.07) → "Save
  and open role" (R-8).
- **She gets:** must-haves she did not retype, each tied to a sentence of the job description.
- **Invariant:** I3, every later flag will cite one of these criteria.

**S1.2 Off path: a protected trait hides in the job description.**
- **When:** the hiring manager wrote "ideal for a young, dynamic team".
- **Steps:** the suggestion is shown as blocked with the reason (R-7, US.06); Inés tries to save with only that
  line left and is stopped because a role needs at least one must-have (R-6).
- **Mistake from the persona:** she clicks through steps quickly. The block is the safeguard, not her attention.
- **Invariant:** I3 (nothing mentions a protected characteristic).

## B2 · CV intake and claim reading

**S2.1 Happy path: importing from the ATS.**
- **When:** Monday 11:30, after the role is open.
- **Steps:** "CSV import" (I-2, US.08) → "Check file" lists 8 rows with no CV text and the reason → imports the
  valid rows → "Run screening". Each CV is read into claims (X-1) after name, email, phone and address are
  removed (X-2; visible with "Show what was sent to the AI", US.10).
- **She gets:** a list she can work through without opening 140 attachments.
- **Invariant:** none directly; B0's P-3 applies.

**S2.2 Off path: a CV the AI cannot read.**
- **When:** one CV is a scanned image with no text.
- **Steps:** extraction fails → candidate marked "needs manual entry" (X-3), never screened out → Inés types the
  three claims next to the CV (X-4, logged).
- **Invariant:** I1 (no candidate drops out without a person seeing it).

**S2.3 Off path: experience that looks short.**
- **When:** a candidate lists two jobs with overlapping dates.
- **Steps:** the working "2019–2022 + 2022–2025 = 6 years" is shown (X-5); Inés sees the overlap and corrects one
  date (X-4).

## B3 · Flags and the shortlist

**S3.1 Happy path: working through the flags between calls.**
- **When:** Monday afternoon to Tuesday, in 20-minute blocks.
- **Steps:** role pipeline filtered to "meets all must-haves" (S-5, US.09) → opens a candidate → each must-have
  shows meets / missing / needs human review, the reason and the CV sentence (S-1, US.10) → "Shortlist" (H-1).
- **She gets:** a shortlist where each decision is hers and has a reason she can repeat to the hiring manager.
- **Invariant:** I1, I2 (list sorted only by date applied or name).

**S3.2 Off path: an unclear claim.**
- **When:** a CV says "5 years in data" for the criterion "5 years of Python development".
- **Steps:** flagged "needs human review" (S-3) rather than meets or missing; Inés reads the jobs and decides.
- **Mistake from the persona:** she trusts a green "meets" without opening the reason. "Needs human review" is
  shown in its own filter so it cannot pass as green.

**S3.3 Off path: shortlisting someone flagged missing.**
- **When:** a candidate lacks the degree but has 8 years of relevant work.
- **Steps:** "Shortlist" asks for a written reason (H-2) → saved on the candidate and in the audit log (P-1).
- **Invariant:** I1, I3.

**S3.4 Check: same claims, same flags.**
- **When:** a test, not a user: two fixture CVs identical except name, age and nationality.
- **Steps:** both get the same results (S-4).
- **Invariant:** I2, I3.

## B4 · Proof after shortlisting

**S4.1 Happy path: sending the requests.**
- **When:** Tuesday 10:00, with 8 shortlisted.
- **Steps:** "Send proof requests" on US.09 opens a preview of the email with the items, why each is asked and
  how long files are kept; Inés confirms (W5, V-1, E-1). One request per claim type on the verification list
  (V-1); emails go to the demo inbox (E-5).
- **Invariant:** I4 (proof only after shortlisting, with the reason), I1 (no message without confirmation).

**S4.2 Happy path: the candidate uploads on her phone.**
- **When:** Wednesday 07:40, Priya on the bus after a night shift.
- **Steps:** opens the email (US.20) → sees the company, the recruiter's name and why her degree is asked for
  (V-3, US.21) → uploads a photo of the certificate → sees "received" (V-4).
- **She gets:** a clear list and a status, so she knows the file arrived.
- **Mistakes from the persona:** she uploads the wrong page; she can replace it before review (V-4). She worries
  it is a scam; the page names the recruiter and says who sees the files and for how long (V-3).

**S4.3 Off path: the link has expired.**
- **When:** Priya opens the email two days after the deadline.
- **Steps:** the expired-link page says nothing is lost, names the recruiter and offers "Request a new link"; Inés
  confirms the reissue (W3).
- **Invariant:** I1, I4.

**S4.4 Happy path: checking proof.**
- **When:** Wednesday 14:00.
- **Steps:** verification queue (V-6, US.12): certificate beside the claim "Bachelor's, First Class Honours" →
  "Mark verified" with a note. GitHub check returns "pending human review" (V-7) → she opens the profile and
  verifies it. Every item verified → interview-ready (V-9).
- **She gets:** the value moment from session 9 step 10: the first candidate interview-ready with no chasing.

**S4.5 Off path: GitHub is down, or a claim fails.**
- **When:** the GitHub API rate-limits.
- **Steps:** "check unavailable, retry" (V-7), never "failed"; later a second candidate's degree does not match
  the CV → "Mark failed" with a note → Inés decides: override with a reason (V-9) or unsuccessful (B5).
- **Invariant:** I1 (no item reaches verified without a person).

## B5 · Specific feedback for people not taken forward

**S5.1 Happy path: approving feedback in a batch of drafts.**
- **When:** Thursday 09:00, after the shortlist is final.
- **Steps:** "Mark unsuccessful" (F-1, US.10) → draft cites the unmet criterion and the CV lines behind it,
  "This role requires at least 5 years of experience in data engineering; your CV shows 3 years
  (2022–2025)" (F-2, W2) → Inés edits one word → "Approve and send" (F-3, E-3).
- **Invariant:** I1, I3.

**S5.2 Off path: a draft that would break the rules.**
- **When:** Inés adds "we went with a stronger candidate" to a draft.
- **Steps:** the safety check blocks it because it mentions another candidate (F-5, US.13); she removes the sentence.
- **Invariant:** I3 (nothing mentions another candidate or a ranking).

**S5.3 Off path: the angry reader.**
- **When:** Thursday 12:30, Tomasz reads the email (US.23) at lunch, sure an AI rejected him because of his age.
- **Steps:** the email opens with "A recruiter, Inés, reviewed your CV and confirmed this decision" (W1) and
  quotes the CV lines behind each unmet criterion (W2). He clicks "Disagree? Ask Inés to re-check"; the request
  is logged (W1, P-1).
- **Mistakes from the persona:** he reads one sentence and replies; the first sentence is the one that names a
  person. He assumes nobody read his CV; the audit log shows who did and when.
- **Invariant:** I1, I3.

**S5.4 Off path: no reason on record.**
- **When:** the role is filled before a candidate was screened.
- **Steps:** a neutral status message instead of invented reasons (F-4).

## B6 · Totals dashboard for the HR lead

**S6.1 Happy path: five minutes before the CEO meeting.**
- **When:** Friday 08:45, Daniel on his laptop.
- **Steps:** dashboard (D-4, US.03): applications, shortlisted and interview-ready per open role; stage counts
  that add up to total applications (D-1); "most common missing must-haves" shows the degree requirement
  excluded the most applicants (D-2); median days from shortlist to interview-ready (D-5).
- **He gets:** one screen of totals for the CEO, and a reason to ask whether the degree requirement is realistic.
- **Invariant:** I5 (counts, rates and durations, never individuals).

**S6.2 Off path: "show me the top three".**
- **When:** the CEO asks Daniel for the best three candidates.
- **Steps:** there is no ranking; the dashboard line "We do not rank candidates" links to the filter "Meets all
  must-haves + proof verified", sorted by date applied (W4, S-5); Daniel cannot edit candidates (U-2).
- **Mistakes from the persona:** he reads stage counts as quality and asks for a fit score. The label and the
  filter answer the need (who is ready for interview) without a ranking.
- **Invariant:** I2, I5.

**S6.3 Off path: a small group.**
- **When:** a role has 3 candidates at "verified".
- **Steps:** the figure is hidden for groups under 5 (D-6), so no one can be identified from a total.

## B0 · Foundation, used in every scenario

**S0.1 A complaint arrives.** Tomasz's re-check request (S5.3) reaches Inés; the audit log (P-1, US.14) shows who
screened, who decided and when, and cannot be edited.

**S0.2 Retention ends.** 30 days after the role closes (U-3), CVs, documents and extracted personal data are
deleted; the audit log keeps only candidate id, actions, times and users (P-2).

**S0.3 A new recruiter joins.** Inés creates an account in settings; the new recruiter sets a password from the
invitation link (U-1, US.02, US.15), so every later confirmation carries a name.

---

## Where the value shows first, per segment (speculation, to test)

Session 9 step 10 asks which segment sees the value most and soonest. This is a guess by the author of
this file from the scenarios above, not a finding. Interviews (step 6) decide it.

| Segment | Bundle that pays off first | Why (speculation) |
|---|---|---|
| A · SME in-house HR (our customer) | B3 then B4 | the shortlist is the weekly pain; proof is the new part |
| B · Recruitment agencies | B4 | a false claim found by the client costs the agency the client |
| C · Regulated employers | B0 (audit log) and B4 | they must show a defensible process |
| D · Tech employers | B4 (GitHub check) | claims are mostly skills and code |
