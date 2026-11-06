# Wave — wave1_structure

60 findings from 4 personas × 2 runs on: structure.md.

Critique: `claude-sonnet-5-5` · triage: `claude-opus-5-5` · 2026-11-05 12:03

## Accepted into this wave (5)

| # | Change | Who asked | Findings | Why |
|---|---|---|---|---|
| W1 | Show at the top of the US.23 feedback email (and in the US.13 draft preview) the sentence 'A recruiter, [name], reviewed your CV and confirmed this decision', and show at its end a link 'Disagree? Ask [name] to re-check' that opens a reply to the named recruiter's monitored address with the stated reply time (e.g. within 5 working days); log each request in the audit log. | Tomasz (unsuccessful candidate, angry) | F48, F49, F54, F55 | Makes visible what I1 already requires ('A named recruiter decides ... every message sent') and gives a human re-check route; sev 4 in both runs, cheap template change. |
| W2 | Show under each unmet criterion in the US.13 draft and the US.23 email the CV lines it rests on, quoted, plus the working for counted claims (e.g. '2019–2022 + 2022–2025 = 6 years'); block 'Approve and send' on US.13 for any sentence without a cited CV line or record. | Tomasz (unsuccessful candidate, angry) | F47, F56 | I3: 'every feedback sentence cites a criterion of the role and the CV text or record it rests on'; sev 4, both runs. |
| W3 | Show a candidate-facing expired-link page when a US.20/US.22 link has expired: 'This link ended on [date]; nothing you uploaded is lost', the recruiter's name and email, and a 'Request a new link' button that notifies the recruiter (the recruiter confirms the reissue). | Priya (shortlisted candidate, phone) | F35, F43 | Directive: 'candidates always know what is asked of them and why'; reissue stays with the recruiter (I1); sev 4, both runs. |
| W4 | Show on the US.03 dashboard and on the US.09 pipeline a line 'We do not rank candidates. See the candidates who passed every check for this role' linking to a new US.09 filter 'Meets all must-haves + proof verified', sorted only by date applied or name. | Daniel (HR lead, not cooperative) | F17, F26 | Explains I2 ('No screen ranks, scores or orders candidates by fit') and answers the HR lead's question with a status filter, while the dashboard keeps totals only (I5); sev 4, both runs. |
| W5 | Show a 'Send proof requests' action on US.09 for shortlisted candidates only, with a preview of the US.20 email (items, why each is asked, retention) and a recruiter confirm step, and show a 'Proof status' tab on US.09 listing shortlisted candidates with each item's state and days since request. | Inés (in-house recruiter, laptop) | F08, F16 | I4 ('Proof only after shortlisting, and always with the reason') and I1 (message needs recruiter confirmation); the list is a recruiter view, not the dashboard (I5); sev 4. |

## Deferred (25)

| # | Change | Who asked | Findings | Why |
|---|---|---|---|---|
| W6 | Show checkboxes on US.09 rows and a 'Shortlist selected' action that opens a confirm screen listing every selected name with its result and reason, recorded per candidate in the audit log under the recruiter's name; remember the last opened candidate and a 'reviewed' mark per row. | Inés (in-house recruiter, laptop) | F01, F09 | Compatible if each shortlist is confirmed by the named recruiter (I1), but the confirm design needs care; outside this wave's cap of 5. |
| W7 | Show the one-line reason and the cited CV sentence under each result on US.09 rows. | Inés (in-house recruiter, laptop) | F02, F10 | Supports I3 ('cites ... the CV text or record it rests on') in the list; outside the cap, next candidate after W6. |
| W8 | Read title, location and closing date from the pasted job description on US.05, add 'Copy a previous role', and add 'Accept all' on US.06 that still shows every must-have on one review screen. | Inés (in-house recruiter, laptop) | F03, F12 | Compatible with the directive (recruiter still confirms the role's must-haves); efficiency gain, outside the cap. |
| W9 | Show on US.06, before saving, for each must-have the count of already imported candidates it would mark 'missing'. | Inés (in-house recruiter, laptop) | F04 | Counts only, no individual ranking (I2); raised once, outside the cap. |
| W10 | Show on US.08 a progress line ('132 of 140 imported, 8 need fixing'; '62 of 140 screened'), let the recruiter fix or download rejected rows and re-import, and say screening continues if the tab is closed with a notification when done. | Inés (in-house recruiter, laptop) | F05, F13 | Compatible with every invariant; sev 2, outside the cap. |
| W11 | Show the result and reasons first on US.10 with CV text, AI toggle and history collapsed; show next to Undo what it undoes and until when ('until you approve and send feedback'); make 'Mark unsuccessful' open a confirm step saying a feedback draft will be created. | Inés (in-house recruiter, laptop), Daniel (HR lead, not cooperative) | F06, F11, F28 | Supports I1 (recruiter confirms each decision) and keeps reasons visible (I3); outside the cap. |
| W12 | Show on US.13 the exact phrase that triggered a blocked draft with a suggested fix, and add a per-role message language setting (e.g. Spanish) for feedback drafts. | Inés (in-house recruiter, laptop) | F15 | Compatible with I3 (safety check stays) and I1 (each draft still approved); outside the cap. |
| W14 | Show a plain-language note beside each result on US.06/US.10 explaining what 'needs human review' and 'missing' mean and what the system looked for, with a Spanish option. | Inés (in-house recruiter, laptop) | F14 | Supports I2 wording ('meets', 'missing', 'needs human review'); raised once at sev 2. |
| W15 | Show at the top of US.03 one headline: median days from application to interview-ready across all roles, this quarter vs last quarter. | Daniel (HR lead, not cooperative) | F18, F24 | Compatible with I5 ('counts, rates and durations for groups'); first in line for next wave, outside this cap. |
| W16 | Show under the 'Open roles by stage' chart on US.03 the label 'Counts where candidates are in the process, not a measure of quality'. | Daniel (HR lead, not cooperative) | F19, F25 | Reinforces I2 (no fit reading); sev 2, outside the cap. |
| W17 | Show on US.09 and US.10 for HR lead accounts a banner 'View only: ask a recruiter to change this' and grey out Shortlist, Mark unsuccessful and Correct claims. | Daniel (HR lead, not cooperative) | F20, F27 | Supports I1 ('a named recruiter decides'); outside the cap. |
| W19 | Show one summary card per role at the top of US.03 with detail blocks collapsed, make it readable at phone width, and add 'Export summary (PDF)' containing totals only. | Daniel (HR lead, not cooperative) | F22, F23, F30 | Compatible with I5 if the export holds group totals only; outside the cap. |
| W20 | Show on the US.01 expired-invitation message a button 'Ask a recruiter for a new invitation' that sends the request. | Daniel (HR lead, not cooperative) | F31 | Compatible with the directive; raised once at sev 2. |
| W21 | Show in the US.20 proof request email the job title, the line 'Your files are seen only by [recruiter] at [company] and deleted after [N] days', 'We never ask for documents by reply or for bank details', and a named contact. | Priya (shortlisted candidate, phone) | F32, F39 | Supports I4 ('the candidate sees why each item is asked for and how long it is kept'); strong next-wave candidate, outside this cap (W5 preview will show the email). |
| W22 | Show on US.21 a preview after choosing a file ('Is this the right page?' with Use / Choose another) and state when replacing stops being possible. | Priya (shortlisted candidate, phone) | F33, F41 | Compatible with I4; outside the cap. |
| W23 | Show on US.21 'Received [time], thank you' with the file name after each upload and send a confirmation email listing received and missing items. | Priya (shortlisted candidate, phone) | F34, F42 | Supports 'candidates always know what is asked of them'; sev 2, outside the cap. |
| W24 | Show next to the referee fields on US.21: 'We will email your referee to confirm only your job title and dates.' | Priya (shortlisted candidate, phone) | F36, F46 | Supports I4 ('the candidate sees why each item is asked for'); sev 2. |
| W25 | Show the deadline and 'X of Y items done' at the top of US.21, one short reason sentence per item with file rules behind 'More info' (reason and retention stay visible), and allow direct camera capture with resizing. | Priya (shortlisted candidate, phone) | F37, F45 | Compatible if each item's reason and retention stay visible (I4); sev 2. |
| W26 | Show the privacy note in two lines at the top of US.21, and give link-type items (e.g. GitHub) a URL field instead of a file upload. | Priya (shortlisted candidate, phone) | F40 | Supports I4 (retention visible); raised once. |
| W27 | State the exact deadline in US.20 and US.22, list only still-missing items in the reminder, and send a second warning before an item is marked 'no response'. | Priya (shortlisted candidate, phone) | F38, F44 | Supports 'candidates always know what is asked of them'; outside the cap. |
| W28 | Show the decision and the single main unmet criterion in the first two lines of US.23, details below in short paragraphs. | Tomasz (unsuccessful candidate, angry) | F50, F59 | Compatible with I3; sev 2, can follow W1/W2 next wave. |
| W29 | Block 'Approve and send' on US.13 for the neutral message when the candidate was screened, until the recruiter adds a concrete reason citing a role criterion and CV text. | Tomasz (unsuccessful candidate, angry) | F51 | Supports I3 ('every feedback sentence cites a criterion of the role'); partly covered by W2's cite check, outside the cap. |
| W31 | Keep the candidate's secure link working after a decision to show the final status, criteria, cited CV text and a 'flag a mistake' action. | Tomasz (unsuccessful candidate, angry) | F52, F60 | Compatible (candidate sees only their own data, not the dashboard; I5) but a larger build; the dispute need is met now by ACCEPT W1 and W2. |
| W32 | Show in US.23 one line: 'AI flagged items from your CV; a recruiter made the decision. Your data is kept [N] days; ask [contact] to see or delete it.' | Tomasz (unsuccessful candidate, angry) | F53, F58 | Supports I5 retention ('personal data is deleted when the retention period ends') and I1; partly covered by W1, outside the cap. |
| W33 | Show on US.03 a 'Waiting on proof' count per role with median days waited, linked to the verification queue (no names). | Daniel (HR lead, not cooperative) | F29 | Compatible with I5 only as group counts and durations, never who is stuck; outside the cap. |

## Rejected (3)

| # | Change | Who asked | Findings | Why |
|---|---|---|---|---|
| W13 | Add 'Approve all similar drafts' on US.13 after reading one example and a recipient list. | Inés (in-house recruiter, laptop) | F07 | Breaks I1 ('no message reaches a candidate without a named recruiter's confirmation') and I3 (each sentence specific to that CV) by approving unread drafts; the language and blocked-draft parts are kept in DEFER W12. |
| W18 | Add a 'Sort by best fit' or 'Shortlist for the CEO' top-three view on US.09. | Daniel (HR lead, not cooperative) | F21 | Breaks I2 ('No screen ranks, scores or orders candidates by fit'); the need to find who passed every check is solved by ACCEPT W4's filter and explanation. |
| W30 | Let the neutral message say 'other candidates matched more of the must-haves'. | Tomasz (unsuccessful candidate, angry) | F57 | Breaks I3 ('nothing mentions ... another candidate or a ranking'); the need for a true, specific reason is solved by DEFER W29 and ACCEPT W2. |

## What must not change

- I1: No shortlist, verified proof item or candidate message happens without a named recruiter's confirmation recorded in the audit log.
- I2: No screen ranks, scores or orders candidates by fit; lists sort only by date applied or name, and results read 'meets', 'missing' or 'needs human review', never 'rejected'.
- I3: Every flag and feedback sentence cites a role criterion and the CV text or record it rests on, and never mentions a protected characteristic, another candidate or a ranking.
- I4: Proof is requested only from shortlisted candidates, only for claim types in the role's verification list, and each item shows why it is asked and how long it is kept.
- I5: The dashboard shows only group counts, rates and durations, never an individual candidate's data, and personal data is deleted when the retention period ends.

## Walk again after the wave

1. Tomasz reads the US.23 feedback email on a phone: recruiter name at top, quoted CV lines with working, and the 'Ask [name] to re-check' link (W1, W2).
2. Recruiter tries to approve a US.13 draft containing a sentence without a cited CV line and is blocked (W2).
3. Priya opens an expired US.20 link and requests a new one; recruiter confirms the reissue (W3).
4. Daniel looks for the top three on US.03 and US.09, reads the no-ranking line and uses the 'Meets all must-haves + proof verified' filter (W4).
5. Ines sends proof requests from US.09 with preview and confirm, then checks the Proof status tab (W5).
6. Invariant check: on US.09 the new filter and Proof status tab sort only by date applied or name, and US.03 shows no candidate names (I2, I5); 'Send proof requests' is unavailable for non-shortlisted candidates (I4).

## Spread between runs

| Persona | Findings per run | Agreement (screen + heuristic) |
|---|---|---|
| Inés (in-house recruiter, laptop) | [8, 8] | 0.23 |
| Daniel (HR lead, not cooperative) | [7, 8] | 0.25 |
| Priya (shortlisted candidate, phone) | [7, 8] | 0.5 |
| Tomasz (unsuccessful candidate, angry) | [7, 7] | 0.27 |
