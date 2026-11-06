# Bundle ranking by simulated personas

**Kind: simulated.** 4 personas × 2 runs = 8 answers, generated 2026-11-06 11:47 by `rank_bundles.py` from `responses/`. Session 9, step 11: this ranks the bundles (a shape); it says nothing about how many real recruiters or candidates want them (U8, A6). Do not hand-edit (A12).

## 1. Overall order (mean rank over all answers, 1 = most important)

| Order | Bundle | Mean rank | Best–worst | Ranks (all answers) |
|---|---|---|---|---|
| 1 | B3 · Flags and the shortlist | 2.00 | 1–3 | 1, 1, 2, 2, 3, 3, 2, 2 |
| 2 | B5 · Specific feedback for people not taken forward | 2.88 | 1–5 | 5, 5, 3, 4, 2, 2, 1, 1 |
| 3 | B4 · Proof after shortlisting | 3.12 | 1–5 | 4, 4, 4, 3, 1, 1, 5, 3 |
| 4 | B2 · CV intake and claim reading | 3.88 | 3–5 | 3, 3, 5, 5, 4, 4, 3, 4 |
| 5 | B1 · Role setup from the job description | 4.38 | 2–6 | 2, 2, 6, 6, 5, 5, 4, 5 |
| 6 | B6 · Totals dashboard for the HR lead | 4.75 | 1–6 | 6, 6, 1, 1, 6, 6, 6, 6 |

## 2. Each persona, each run

| Persona | Run 1 | Run 2 | Agreement between runs (Spearman ρ) |
|---|---|---|---|
| Inés (in-house recruiter, laptop) | B3 > B1 > B2 > B4 > B5 > B6 | B3 > B1 > B2 > B4 > B5 > B6 | 1.00 |
| Daniel (HR lead, not cooperative) | B6 > B3 > B5 > B4 > B2 > B1 | B6 > B3 > B4 > B5 > B2 > B1 | 0.94 |
| Priya (shortlisted candidate, phone) | B4 > B5 > B3 > B2 > B1 > B6 | B4 > B5 > B3 > B2 > B1 > B6 | 1.00 |
| Tomasz (unsuccessful candidate, angry) | B5 > B3 > B2 > B1 > B4 > B6 | B5 > B3 > B4 > B2 > B1 > B6 | 0.83 |

ρ = 1: both runs gave the same order; ρ near 0: the order is not stable for that persona (U7).

## 3. Kano category per persona and bundle

A attractive (delighter) · O performance · M must-be · I indifferent · R reverse (they would rather not have it) · Q questionable. Runs are separated by `/`; a single letter means all runs agree.

| Persona | B1 | B2 | B3 | B4 | B5 | B6 |
|---|---|---|---|---|---|---|
| Inés (in-house recruiter, laptop) | A | M/O | O | A | A | I |
| Daniel (HR lead, not cooperative) | I | I | O/A | A | O/A | O |
| Priya (shortlisted candidate, phone) | I | I | A | O | A | I |
| Tomasz (unsuccessful candidate, angry) | I | O/A | O | I | O | I |

Kano categories that agree across runs: 20 of 24 persona–bundle pairs.

## 4. Proof timing (session 9, step 11: the relative drop, not a rate)

| Persona | At application (1–5, per run) | After shortlist (1–5, per run) | Why (run 1) |
|---|---|---|---|
| Inés (in-house recruiter, laptop) | 2, 2 | 5, 5 | Asking for documents at application would scare off candidates and give me 140 piles of paperwork to handle, while asking only the shortlisted few is reasonable and manageable. |
| Daniel (HR lead, not cooperative) | 2, 2 | 5, 5 | Asking everyone for documents upfront would put off good candidates and raise data-protection questions, whereas asking only shortlisted people with a stated reason is fair and defensible. |
| Priya (shortlisted candidate, phone) | 2, 1 | 5, 5 | Sending degree papers to a company I know nothing about before they even want me feels risky and like a scam, but after being shortlisted with a stated reason I would go ahead. |
| Tomasz (unsuccessful candidate, angry) | 2, 2 | 5, 5 | Uploading degree certificates and referees for every application is a lot of effort and personal data for a job I may not get, so I would probably skip it; after shortlisting, with the reason stated, it is fair. |

## 5. When each persona would meet each bundle (run 1, their words)

**B1 · Role setup from the job description**

- *Inés (in-house recruiter, laptop)* (attractive): Monday morning, pasting the data engineer job description before the 140 applications get processed. I hate retyping what is already in the job description, so suggested must-haves save me time, but I could still write them by hand.
- *Daniel (HR lead, not cooperative)* (indifferent): I would not; a recruiter sets up the role before I ever look at the numbers, maybe I hear about it in a weekly catch-up. Setup is the recruiters' job and I only care that the protected-traits block keeps us legal.
- *Priya (shortlisted candidate, phone)* (indifferent): I would never see it; at most the proof request I get mentions a reason that came from the job description. It is the recruiter's setup screen, so it only matters to me if it makes the requests for proof sensible.
- *Tomasz (unsuccessful candidate, angry)* (indifferent): I never see it; I only wonder, in the lunch break while reading the rejection, whether the must-haves were fair and not about my age. The blocking of age criteria sounds good, but I cannot see it, so I only care if the reason in my email matches a real requirement.

**B2 · CV intake and claim reading**

- *Inés (in-house recruiter, laptop)* (must-be): Tuesday, uploading the CV batch or importing the CSV from my ATS between two interviews. Without CVs read automatically I would be typing claims by hand for 140 people, which makes the tool pointless.
- *Daniel (HR lead, not cooperative)* (indifferent): Only indirectly, when a recruiter tells me CVs are processed faster than before. I assume any hiring tool reads CVs; I do not want to see how it does it.
- *Priya (shortlisted candidate, phone)* (indifferent): The night I upload my CV and hope nobody reads the wrong dates or my name wrongly. I care that my CV is read correctly and personal details are protected, but I do not see this part.
- *Tomasz (unsuccessful candidate, angry)* (performance): When I read the rejection and see whether it quotes my 12 years of experience correctly, or got my jobs wrong. If a machine misread my CV and nobody can correct it, that is exactly the unfairness I suspect; showing the working and allowing correction matters.

**B3 · Flags and the shortlist**

- *Inés (in-house recruiter, laptop)* (performance): Wednesday in a 20-minute block, going through the flagged list to confirm the shortlist for the interviews. This is the core of my problem, cutting 140 applications to a shortlist quickly, and I need to find my place again after phone calls.
- *Daniel (HR lead, not cooperative)* (performance): Monday before the CEO meeting, when I ask what the shortlist for the data role looks like and who the best three are. This is the closest thing to the answer I need, though I would be annoyed it is filtered not ranked, so I want a clear answer for the CEO.
- *Priya (shortlisted candidate, phone)* (attractive): Waiting a few days after applying to hear if I got shortlisted or not. A person confirming and giving reasons feels fairer to me than a machine rejecting me quietly.
- *Tomasz (unsuccessful candidate, angry)* (performance): At lunch, when I open the email and want to know which requirement I supposedly missed and whether a human confirmed it. A named person confirming a written reason for 'missing' is the only thing that answers my fear that AI rejected me for my age.

**B4 · Proof after shortlisting**

- *Inés (in-house recruiter, laptop)* (attractive): Thursday, sending proof requests to the shortlisted people before Friday and checking uploaded documents. It is useful and saves email chasing, but I can ask for certificates by email myself if I have to.
- *Daniel (HR lead, not cooperative)* (attractive): When a recruiter says someone is interview-ready or a candidate complains about being asked for documents. Checked claims protect us from bad hires and legal trouble, but it is the recruiters' work, not mine.
- *Priya (shortlisted candidate, phone)* (performance): On the bus after a night shift, opening the email on my phone to upload my degree and GitHub link. I need a clear, safe-looking page that says who sees my documents and why, and confirms the file was sent, or I will think it is a scam.
- *Tomasz (unsuccessful candidate, angry)* (indifferent): Only if I were shortlisted; as a rejected candidate I never meet it. It does not affect me now, as I was turned down, and asking for proof only from shortlisted people seems reasonable.

**B5 · Specific feedback for people not taken forward**

- *Inés (in-house recruiter, laptop)* (attractive): Friday afternoon, approving feedback drafts for rejected candidates instead of writing dozens of emails. It is a nice time saver and good for employer image, but today I mostly send short generic rejections or nothing, so it is not essential.
- *Daniel (HR lead, not cooperative)* (performance): When a rejected candidate complains or threatens a claim and I need to know what we told them. As head of people I worry about discrimination claims, so specific, approved feedback is real protection.
- *Priya (shortlisted candidate, phone)* (attractive): Getting a reply about another job I applied for and was not chosen for. Specific feedback tells me what to improve, but I would still apply if it were missing.
- *Tomasz (unsuccessful candidate, angry)* (performance): On my phone at lunch, reading the email, in the first sentence, deciding in 3 minutes whether to reply with a complaint. A specific reason with my own CV lines that I can check as true or false is the only thing that stops me going public; a generic reason makes me complain.

**B6 · Totals dashboard for the HR lead**

- *Inés (in-house recruiter, laptop)* (indifferent): Only when my HR lead asks for numbers in a monthly meeting; I would not open it myself. It is for the HR lead and does not change my daily work much.
- *Daniel (HR lead, not cooperative)* (performance): Once a week on my laptop, five minutes before the CEO meeting, to show that hiring got faster. It is the only screen I use myself and it gives me the time-to-interview-ready number for the CEO; I would want it to show a top three but accept it will not.
- *Priya (shortlisted candidate, phone)* (indifferent): I would not meet it at all. It is only for the HR lead and does not touch my application, though I like that it does not name people.
- *Tomasz (unsuccessful candidate, angry)* (indifferent): Never; it is only for the HR lead. Totals without names do not help me, though it is good that it does not rank individuals.

