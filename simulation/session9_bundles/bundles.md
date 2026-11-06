# Feature bundles

The 65 features in [`../../feature-list.md`](../../feature-list.md) grouped into bundles that a recruiter or an
HR lead would recognise as one job done. Built for the DS403 session 9 method ([`../../research/audience-analysis-steps.md`](../../research/audience-analysis-steps.md),
steps 10, 11 and 13): simulated personas **rank** the bundles and say how they would feel with and without
each one (a Kano pair). The ranking sets a **shape**, never a level (step 11): no "x% of recruiters want B4".

As of 2026-11-06, from `feature-list.md` at commit `fa8d7ab`.

## B0 · Foundation (not ranked)

Every other bundle needs these, so personas do not rank them: U-1 named login, U-3 company settings,
P-1 audit log, P-2 retention and deletion, P-3 personal details removed before any AI call, P-5 synthetic-data label.

## The six bundles that are ranked

The script reads the rows of this table (id, name, what you get). Keep one row per bundle.

| Id | Bundle | What you get (as shown to personas) | MVP features | Stretch features | Session 9 variant it serves |
|---|---|---|---|---|---|
| B1 | Role setup from the job description | Paste the job description; the tool suggests must-haves, each with the sentence it came from; you accept, edit or delete each one; criteria about age, nationality or other protected traits are blocked; you choose which claims need proof later. | R-1, R-2, R-3, R-5, R-6, R-7, R-8 | R-4 | all SME variants (entry point) |
| B2 | CV intake and claim reading | Upload CVs or import a CSV from your ATS; the tool reads each CV into claims (degrees, jobs, skills, GitHub) with personal details removed first, shows years of experience with the working, and lets you correct anything. | I-1, I-2, X-1, X-2, X-3, X-4, X-5 | I-3, I-4 | SMEs × trustworthy shortlist |
| B3 | Flags and the shortlist | Each candidate gets meets / missing / needs human review per must-have, with the reason and the CV sentence; the list is filtered, never ranked; a recruiter confirms every shortlist, with a written reason for anyone flagged missing. | S-1, S-2, S-3, S-4, S-5, H-1, H-2 | S-6, H-3 | SMEs × trustworthy shortlist |
| B4 | Proof after shortlisting | Only shortlisted candidates get an email with a secure link asking for proof of specific claims and why; they upload on their phone; you check each document beside the claim; GitHub is checked; a candidate is interview-ready only when a person has verified every item. | V-1, V-2, V-3, V-4, V-6, V-7, V-9, E-1, E-5 | V-5, V-8, E-2, E-4, P-4 | agencies × verify before client submission; SMEs × trustworthy shortlist |
| B5 | Specific feedback for people not taken forward | For each unsuccessful candidate the tool drafts feedback that names only the unmet job criteria and the CV lines behind them; a safety check blocks anything else; nothing is sent until a recruiter approves it. | F-1, F-2, F-3, E-3 | F-4, F-5 | SMEs × specific rejection feedback |
| B6 | Totals dashboard for the HR lead | A separate read-only view for the HR lead: candidates at each stage per role, the most common missing must-haves, proof response rate and time to interview-ready; never names or rankings. | U-2, D-1, D-2, D-3, D-4 | D-5, D-6, D-7 | regulated employers × defensible, audited process |

Later features (U-4, I-5, V-10, F-6, D-8) are left out of every bundle.

## Coverage check (own analysis)

| | MVP | Stretch | Later |
|---|---|---|---|
| In `feature-list.md` | 45 | 15 | 5 |
| In B0–B6 above | 6 + 7 + 7 + 7 + 9 + 4 + 5 = 45 | 1 + 2 + 2 + 5 + 2 + 3 = 15 | 0 (left out on purpose) |

Every MVP and stretch id appears in exactly one bundle (`python rank_bundles.py --check` recounts it from the two files).
