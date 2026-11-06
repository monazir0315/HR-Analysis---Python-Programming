# critique_daniel_run1 → claude-sonnet-5-5

## System

You are a real person trying to use a product, not an assistant and not a designer. Stay in character:
your goal, your device, what you know and the mistakes you typically make are described below.

The product, as it was described to you: A web app for HR teams that reads CVs against the must-haves of a job, asks shortlisted candidates for proof of what they claimed (a degree certificate, a GitHub profile, a referee), and writes feedback to the people who are not taken forward. Candidates only see an email and an upload page.

Who you are:

id: daniel
name: Daniel (HR lead, not cooperative)
who: 48, head of people at the same company; signs off the tool's budget; looks at it once a week.
goal: show the CEO that hiring got faster and ask the tool for the best three candidates for the data role.
device: laptop in meetings, sometimes his phone
time: 5 minutes, wants one screen
knows: HR law in outline; little about how screening works; expects rankings because other tools have them.
language: native English
mistakes: reads stage counts as a quality ranking; asks for features that do not exist (a top-10 list, a fit score); assumes he can edit candidates.
patience: impatient; says no to any screen that needs explaining; stops using it if he cannot get an answer for the CEO.

You are shown either screens (in order) or, before anything is built, the product's written structure
(its maps, situations and task specs). Walk it as yourself:

1. Say what you would try first on each screen to reach your goal, and what you think would happen.
2. Report what went wrong or slowed you down: something you could not find, misread, could not undo, had
   to remember from another screen, did not trust, or that took too many steps for your situation. With
   the written structure, report a situation you are in that it does not cover, or covers in a way you
   would not follow.
3. Be specific: name the screen (file name, or the situation id) and the words or control on it. Do not
   invent controls you cannot see. If something works well for you, do not report it.
4. Prefer 4–8 findings that matter to you over a long list. Severity: 1 cosmetic, 2 minor (slows me),
   3 major (I fail or give up sometimes), 4 blocker (I cannot do what I came for).
5. Name the one Nielsen heuristic each finding breaks, by its name: Visibility of system status · Match
   between system and the real world · User control and freedom · Consistency and standards · Error
   prevention · Recognition rather than recall · Flexibility and efficiency of use · Aesthetic and
   minimalist design · Help users recognize, diagnose, and recover from errors · Help and documentation.
6. Suggest one concrete change in your own words: what you wish were there instead.

Reply with JSON only, in this shape:

{"findings": [{"screen": "file name or situation id",
               "what_i_tried": "first person, one sentence",
               "what_happened": "what the screen did or showed",
               "problem": "why that is a problem for me",
               "severity": 1-4,
               "heuristic": "one of the ten names above",
               "suggestion": "one concrete change"}]}

## User


What you are shown (no screens yet — the product's maps, situations and specs):

# Structure of the product, as of 2026-11-05 (wave 1 input)

What simulated users read in wave 1 (stage 2, "structure", U5): the brief, the candidate journey and the
user situations (a screen and its actions). Built from `README.md`, `feature-list.md` and the clickable
prototype `mockup/prototype.html` at this commit. All data in the product is synthetic.

## 1. Brief

A web app for in-house HR at companies of 50 to 500 staff. It screens applicants against the role's
must-haves, asks shortlisted candidates for proof of their claims, drafts feedback for unsuccessful
candidates, and shows a dashboard of totals per role. It works on its own or next to an existing ATS
(CSV import). The AI flags and drafts; a recruiter confirms every shortlist, every verified document and
every rejection message. Two signed-in user types: **Recruiter** (does everything) and **HR lead**
(dashboard, audit log, read-only on candidates). Candidates and referees never sign in: they get an email
with a link.

## 2. Candidate journey

```text
applied → screened (flags) → shortlisted (recruiter) → proof requested
   → items received → each item verified (recruiter) → interview-ready
                         ↘ failed / no response → recruiter decides (override with reason, or unsuccessful)
unsuccessful (recruiter, any stage) → feedback drafted → safety check → approved (recruiter) → sent
```

Each proof item has its own state: requested → received → pending review → verified / failed /
no response / check unavailable. One reminder is sent after 3 days; after that the item is marked
"no response".

## 3. User situations

Ids are stable (D2). "Shows" is what is on the screen; "Actions" is what the user can do there.

### Signed-in users

- **US.01 Sign in.** Shows: email and password fields, "Sign in", "Forgot password?". Actions: sign in;
  a wrong password shows an error; an account still waiting for its password says to use the invitation link.
- **US.02 Set your password (invitation link).** Shows: name, email, account type, link expiry date, two
  password fields and four rules that tick as you type (10+ characters, a letter and a number, not your name
  or email, both match). Actions: "Set password and activate account" (disabled until all rules pass), then
  "Go to sign in". An expired link says to ask a recruiter for a new one.
- **US.03 Dashboard.** Shows: open roles with applications, shortlisted and interview-ready counts;
  "Open roles by stage" (counts per stage, adding up to total applications); "Most common missing
  must-haves" with counts; "Process figures" per role (proof response rate, median days from shortlist to
  interview-ready). No names of candidates. Actions: open a role's pipeline; "Open verification queue".
- **US.04 Roles list.** Shows: draft, open and closed roles with candidate counts. Actions: "Create role",
  open a role.
- **US.05 Create role, step 1: job description.** Shows: role details (title, department, location, closing
  date) and a box to paste the job description. Actions: "Suggest must-haves".
- **US.06 Create role, step 2: must-haves.** Shows: each suggested must-have with its type (years of
  experience, degree level, required skill, certification, language), its value and the sentence of the job
  description it came from. Sentences about age, nationality or other protected characteristics are shown as
  blocked, with the reason. Actions: "Accept", "Edit", "Delete" on each; "Add" one by hand; "Suggest again".
  A role cannot be saved with zero must-haves.
- **US.07 Create role, step 3: proof needed after shortlisting.** Shows: the verification list (degree,
  certification, employment, GitHub, reference), pre-filled from the must-haves. Actions: tick or untick;
  "Save and open role".
- **US.08 Add applicants.** Shows: "Upload CV files" (PDF, DOCX or text) and "CSV import" (name, email, CV
  text). Actions: "Choose files"; "Check file", which lists rows with missing columns and the reason;
  "Import" only the valid rows; "Run screening".
- **US.09 Role pipeline.** Shows: the candidates of one role, filtered by status (all, meets all, missing,
  needs human review, shortlisted, proof requested, interview-ready, unsuccessful), sorted by date applied or
  name only. Each row shows the overall result: "meets all must-haves", "missing: [criterion]" or "needs
  human review". Actions: "Open candidate".
- **US.10 Candidate detail.** Shows: "Claims found in the CV" next to the CV text; a toggle "Show what was
  sent to the AI" that shows the CV with name, email, phone and address removed; "Screening against
  must-haves": for each must-have, meets / missing / needs human review, a one-line reason and the CV
  sentence it relied on; years of experience with the working ("2019–2022 + 2022–2025 = 6 years");
  "History". Actions: "Correct claims" (logged); "Shortlist" (a candidate flagged "missing" needs a written
  reason); "Mark unsuccessful"; "Undo".
- **US.11 Proof of claims (on the candidate).** Shows: one item per claim type in the role's verification
  list with its state. Actions: open the item in the verification queue; "Mark interview-ready (override)",
  which needs a written reason when an item is not verified.
- **US.12 Verification queue.** Shows: the uploaded document beside the claim it should prove; the GitHub
  check result ("failed: not found", "pending human review" or "check unavailable, retry"); the referee's
  answer. Actions: "Mark verified" or "Mark failed", with a note; "Retry check"; demo button "Simulate
  3 days passing" to see the reminder and the "no response" state.
- **US.13 Feedback for an unsuccessful candidate.** Shows: a draft that cites only the role's criteria
  recorded as unmet or unverified, e.g. "This role requires at least 5 years of experience in data
  engineering; your CV shows 3 years."; the safety-check result (blocked if it mentions a protected
  characteristic or a reason not in the screening record); a neutral message when no unmet criteria are
  recorded. Actions: edit the draft; "Reset draft"; "Approve and send" (nothing is sent before this).
- **US.14 Audit log.** Shows: every status change with who, what and when; it cannot be edited.
  Actions: read and filter.
- **US.15 Company settings.** Shows: retention period (30 days), reminder delay (3 days), sender name and
  email; "User accounts" with status (Active / Invited, password not set / Invitation expired).
  Actions: "Save settings"; "Create account" (recruiters only: company email domain, sends an invitation);
  "Resend invitation".

### Candidates and referees (no sign-in)

- **US.20 Proof request email.** Shows: who is asking (company and recruiter's name), that the candidate was
  shortlisted, the list of items requested, a secure link and its expiry date.
- **US.21 Candidate upload page ("Proof for your application").** Shows: each item requested and why
  ("This role requires a Bachelor's with First Class Honours, as stated on your CV"), accepted file types,
  size limit, a privacy note on who sees the files and how long they are kept, and each item's status
  (requested / received / verified). Actions: "Upload" a file per item; "Replace file" before review; for
  a reference, give the referee's name and work email.
- **US.22 Reminder email.** Sent once, 3 days after the request, for items still missing.
- **US.23 Feedback email.** Shows: the text the recruiter approved, naming the unmet criteria of the role.
  Sent from the company's sender address.
- **US.24 Referee form ("Confirm employment details").** Shows: the candidate's stated job title and dates
  at the referee's company. Actions: "Are these details correct?" yes / no / correction; "Send answer".
  No free-text opinion about the candidate.

## 4. What the product deliberately does not do

- No score, rank or "best match" view of candidates.
- No automatic rejection and no message sent without a recruiter's approval.
- No public apply form or job-board posting (it works next to the company's ATS).
- No candidate accounts.
- No detection of forged documents: a recruiter looks at every document.


Run 1. Walk it as Daniel (HR lead, not cooperative) and report.