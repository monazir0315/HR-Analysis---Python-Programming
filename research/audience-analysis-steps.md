# Audience analysis: the steps

Pre-Interview Screening and Verification Pipeline, sized with the method from DS403 Session 9, "Finding a niche with data and agents" (29 Oct 2026).

This file turns the session's thirteen-step cheat sheet into steps for our product. It builds on `Audience Analysis Pre-Interview Screening and Verification Pipeline.docx` (the three roles, segments A to D, jobs, pains, interview questions) and does not repeat it. That document gives hypotheses. These steps turn them into an estimate we can defend line by line, and they tell us what to research next.

## What changes when the buyer is a company

The session sized a consumer product: people × rates × price. Our buyer is an employer, so three things change:

| Session 9 (Ritmo Coach) | Our pipeline |
|---|---|
| unit = a person in an age band | unit = an **employer** in a segment (A to D) × size band |
| value = € per month per person | value = € per seat, per hire or per verified candidate; we have to choose one (step 11) |
| one audience pays and uses | buyer, daily user and affected party are **different people** (HR lead, recruiter, candidate) |
| P(pay) from the app's own funnel | no funnel yet: interviews and a fake door give the first rates |

A niche is still **who × which job × at what price × through which channel**. For example: "recruitment agencies × verify claims before sending a candidate to the client × per verified candidate × through an ATS marketplace".

## The five rules we follow

1. **Every number carries its source, date and kind**: `open`, `partial`, `research`, `assumption` or `simulated`.
2. **Intervals, not points**: Beta posteriors for rates, Monte Carlo for sizes.
3. **Two independent routes**, bottom-up and top-down, agree within about 3×. An observed total is a ceiling that rules out impossible numbers.
4. **Simulated data sets a shape, never a level.** LLM personas of recruiters or candidates can rank options but cannot say how many will buy.
5. **The answer names the next input to research**: the one that moves the result most.

---

## Step 1 · Brief

File: `research/niche_brief.md`.

- The product in two sentences, taken from the README.
- 3 to 5 niches as **who × job**, from segments A to D and the jobs to be done in the audience docx.
- **The decision**: which segment we build the MVP's story and demo for. **Its date**: before session 10.
- **What would stop us**: for example, interviews show that verification is already handled by the background-check provider for every segment.

Every agent prompt (`analyst_agent.md`, `competitor_scan.md`, `deep_research_prompt.md`) gets the brief first.

## Step 2 · Ledger first

Every number goes through one function and one table, `research/ledger.csv`:

```python
fact(name, low, high, unit, kind, source)
# kind ∈ {"open", "partial", "research", "assumption", "simulated"}
```

Starting rows. Values are left empty on purpose: the audience docx deliberately has no numbers, and we do not invent them.

| name | unit | kind (planned) | where it comes from |
|---|---|---|---|
| `employers_50_499_ES` | enterprises | open | INE DIRCE (enterprises by employee band) or Eurostat SBS by size class |
| `staffing_agencies_ES` | enterprises | open | INE DIRCE / Eurostat SBS, NACE N78 (employment activities) |
| `regulated_employers_ES` | enterprises | open | same, NACE K, O, P, Q (finance, public, education, health) |
| `tech_employers_ES` | enterprises | open | same, NACE J62 to J63 |
| `hires_per_employer_year` | hires | open / research | Eurostat job vacancy statistics, LFS job changers; per size band |
| `share_with_ats` | share of employers | research | ATS vendor reports, surveys; two sources opened by us |
| `share_using_ai_hr` | share of employers | open | Eurostat ICT usage in enterprises (AI use, by size class) |
| `share_false_claim_found` | share of hires | research | screening-provider discrepancy reports (paid reports quoted on secondary pages: record what we saw) |
| `problem_rate_a` | share of employers | assumption → partial | interviews (step 6) |
| `pay_rate` | share of qualified employers | assumption → partial | fake door (step 13) |
| `price` | € / unit | assumption | competitor prices (step 7) |
| `reach_year1` | share of SAM | assumption | channel plan (step 11) |

Check every Eurostat and INE table code against the live API before quoting it, and put the query URL in the `source` column.

## Step 3 · Population N(x)

How many employers there are in each cell x = segment × size band × country.

- Start with **Spain**, the same geography as the session. Widen to the EU only once the Spanish numbers pass the checks.
- Eurostat answers without a key (`ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/<code>`). INE has a Tempus3 JSON API.
- Also record **hires per year** per cell. If we price per hire or per verified candidate, hires are the volume that matters, not headcount.
- Date every number. Business statistics lag 1 to 2 years.

## Step 4 · Budget b(x)

The share of employers in a cell who already pay for something in this space: an ATS, background checks or HR software.

- Open: Eurostat ICT usage in enterprises (software and AI use by size class).
- Research: ATS penetration by company size. Vendor-published figures are biased upwards, so mark them `research` and open two sources ourselves.
- A cheap proxy from interviews: "What tools do you use now, and what do you pay?" (question 4 in the audience docx).

## Step 5 · Problem a(x)

The share of employers who feel the pain: false claims found late, chasing candidates for documents, no time for rejection feedback.

- **Shape** (which segment feels it most) comes from conversations and reviews (step 8).
- **Level** (how many) comes only from interviews, a survey or a bridge (step 9). Conversations never set it.
- Count as evidence only a specific recent incident with a cost, or a workaround already in use. "Sounds useful" does not count. This is the rule from section 7 of the audience docx, and it maps onto the labeling functions in step 12.

## Step 6 · Our own data, and how far it can speak

Our own data is the 3 to 5 professional interviews and the 2 to 3 job-seeker interviews from section 7 of the audience docx. Notes go in `research/interviews.md`.

- Turn each yes/no answer into a **Beta posterior**: k of n interviewees → `Beta(1 + k, 1 + n − k)`. With n = 5 the interval is very wide. That is the honest answer, so quote the interval.
- **Coverage check**: list the cells (segment × size band) the interviewees come from. The uncovered share is
  `u = Σ N_c / N` over the cells with no interviewee.
  If u > 5%, either restrict the claim to the covered cells ("agencies in Barcelona with 10 to 50 recruiters") or interview in the missing cells. Reweighting cannot cover a cell nobody was asked in.
- If we later get a larger sample (a survey or a waitlist), post-stratify it to N(x) from step 3, and report `n_eff = (Σw)² / Σw²` and the largest weight relative to the median. Collect more if n_eff < 30. Trim if max/median > 10.
- Ask the questions in the same words every time, or the answers cannot be compared.

## Step 7 · Competitors and features

Prompt: `competitor_scan.md` in a chat with web search. Output: `research/competitors.csv`, one row per product with its pricing URL and the date seen.

- **Who**: background-check and ID providers (HireRight, Sterling, Checkr, Veriff), ATSs (Greenhouse, Ashby, Workable, Teamtailor, and Personio for EU SMEs), and the agencies' own tools.
- **Map** them on two axes of the job: *integration into the screening workflow* × *depth of claim verification*. Then add a third flag: *drafts specific candidate feedback*. The corner the audience docx guesses is empty is "inside the workflow + verification tracking + feedback, with human gates". An empty corner is a candidate, not proof of demand.
- **Features from reviews**: public reviews of these products (G2, Capterra, Trustpilot, app stores where they exist) → `feature_extraction.md` or a keyword lexicon → for each feature, how many reviews mention it and the **rating gap** (mean stars of reviews mentioning it minus the overall mean).
  - Kano reading: a negative gap means a must-be (users punish its absence or its failures). A positive gap means a delighter.
  - Watch the "AI" row. In the session, reviews mentioning AI rated 1.5 stars lower. "AI screening" may hurt us, while "human-confirmed verification" may help. Check this, don't assume it.
- **Lift per segment**: P(feature | segment) / P(feature), from reviews that name the writer's context ("our agency", "our hospital", "as a recruiter"). Groups will be small, so report intervals.

## Step 8 · Conversations: what people say about the job

Prompt: `social_listening.md` over an export. Exact quotes only, never attributed to a person.

- **Recruiter side**: the Hacker News Algolia API (open, no key) for "background check", "fake degree", "lied on resume", "rejection feedback", "ATS"; exports from Reddit's r/recruiting and r/humanresources.
- **Candidate side**: r/recruitinghell and r/cscareerquestions on document requests, ghosting and feedback. This tests the risk that asking for documents makes good applicants drop out.
- Topics with TF-IDF + NMF offline, or BERTopic or an LLM for the labels.
- **Share of voice per segment**: segment cue words (agency, client, hospital, licence, GitHub, startup) next to pain words (found out, after offer, chasing, no response, never heard back).
- **Who is missing**: HR in small Spanish companies, people writing in Spanish, and regulated-sector HR (they rarely post in public). Say so in the write-up. Do not let route B split the market by voice share for segments that do not post (that is the session's "health 55+" failure).

## Step 9 · Overlap: problem and budget in the same employer

What we need per cell is q(x) = P(problem ∧ budget | x), not a(x) × b(x).

```text
q(x) = P(A | x) · P(B | A, x)
qualified employers = Σ_x N(x) · q(x)
no overlap data → Fréchet bounds: max(0, a + b − 1) ≤ q ≤ min(a, b)
```

- Report the **bounds** first. Independence (q = a·b) is an assumption and must be labelled as one.
- The **bridge** is the interviews: ask the problem questions and the budget question of the same person. That estimates P(budget | problem). Check it lies inside the bounds. If it doesn't, the definitions differ (for example "pays for background checks" vs "pays for an ATS"), so align them first.

## Step 10 · The key user journey, per segment

Prompt: `journey_simulator.md` in a chat. It follows the spec's state machine:

```text
role set up → applications in → screened (flags) → shortlisted (human)
  → proof requested → candidate responds?  ← candidate drop-out risk
  → verified (human) → interview-ready      ← value moment
side branch: unsuccessful (human) → feedback drafted → approved (human) → sent
```

- **Value moment for the buyer**: the first shortlisted candidate who reaches "interview-ready" with no manual chasing, or the first false claim caught before an interview.
- **Value moment for the candidate**: a specific, job-related rejection instead of silence.
- Simulate per segment (agency vs SME vs regulated). The volume of hires and the share of claims that need proof differ by segment.
- The output is a **ranking** (in which segment the value shows most and soonest), not a conversion level. Step-to-step rates are assumptions until interviews or a pilot replace them.

## Step 11 · Simulated users: shape only

`persona_simulator.md`: recruiter and candidate personas, several runs with varied details, the spread reported, every row marked `simulated`.

Allowed uses:
- ranking segments by perceived pain;
- ranking price models (per seat vs per hire vs per verified candidate);
- the *relative* drop in candidate willingness when documents are asked at application vs after shortlist.

Not allowed: "x% of recruiters would buy". LLM personas lean towards liking and towards finishing every flow (NN/g; AgentA/B, CHI EA '26). The estimate code refuses a `simulated` row used as a level: `assert row.kind != "simulated"`.

## Step 12 · Two routes, an interval, and what moves it

**Route A, bottom-up**

```text
SAM_A = Σ_x N(x) · P(budget | x) · P(problem | budget, x) · P(pay | ·) · price · volume(x)
```

`volume(x)` is seats, hires or verified candidates per year, depending on the price model.

**Route B, top-down**

```text
SAM_B = market report (pre-employment screening, or recruitment software)
        × share Spain × share of our segment
```

- Market reports will disagree, as the session's habit-app reports did by 20×. Record what we saw, with provider, year and definition. Use an observed total as the **ceiling**: no "screening for SMEs" figure can exceed the whole background-screening market.
- **Check**: ⅓ ≤ SAM_A / SAM_B ≤ 3. If a segment fails, the check tells us which evidence to replace.
- **Year one**: SOM = SAM_A × P(reach), with 20,000 Monte Carlo draws from the ledger ranges. Report P10, P50 and P90.
- **Sensitivity**: rank the inputs by |rank correlation| with SOM. Expect reach and the pay rate at the top, both of which start as assumptions. The top input is what we research in step 13.

## Step 13 · Variants, synthesis and steering

**Variants (who × job × price × channel)**, ranked by **P10** (the pessimistic case), not by the mean. For example:

| Variant | Price model | Channel |
|---|---|---|
| agencies × verify before client submission | per verified candidate | direct / LinkedIn to agency owners |
| SMEs 50 to 250 × trustworthy shortlist without manual checks | per recruiter seat / month | ATS marketplace (Personio, Teamtailor) |
| SMEs × specific rejection feedback | per role | ATS marketplace |
| regulated employers × defensible, audited process | per seat + compliance tier | partnership with a screening provider |

Flag every variant that relies on simulation (for example, a price never observed).

**Combine the signals** (Part 7 of the session):

- *Weak supervision*: labeling functions over reviews and conversations. Each one marks texts that support a claim:
  - `need_recurring` ("found out after the offer", "fake degree") → a need exists;
  - `pays_workaround` ("we pay for background checks but…") → spending already exists;
  - `switching` ("alternative to …") → interest in switching;
  - `asks_feature` → offer demand;
  - `praise_only` → 0 (attention, not intent).

  Report each function's coverage, overlap and conflict. These labels describe texts, not the market.
- *Triangulation*: one question, e.g. "Are agencies ahead of SMEs?", answered by sources whose **biases differ**:

  | Source | Its main bias |
  |---|---|
  | conversations (HN, Reddit) | tech-heavy, English-speaking, vocal |
  | product reviews | extremes; users of existing tools |
  | interviews | tiny n; our own network |
  | open business statistics | definition (NACE codes ≠ our segments) |
  | journey simulation | our assumptions |

  When one source disagrees, ask why before averaging it away.
- *Belief vs ignorance*: for "segment X is viable", keep "evidence against" apart from "not enough evidence". With five interviews, "we do not know yet" is a valid answer, as long as it names the evidence that would change it.

**Steer**:

1. Sensitivity → the top input.
2. Research it:
   - a **desk-research** input (for example ATS penetration or the false-claim rate): `deep_research_prompt.md` in Perplexity, ChatGPT, Gemini or Claude, then open two sources ourselves before the figure enters the ledger as `research`;
   - a **behaviour** input (the pay rate): a **fake door**. A landing page, "Verify your shortlist before the interview", shown to recruiters through the variant's channel. Count demo requests or sign-ups out of visits → `Beta(1 + k, 1 + n − k)`.
3. Re-run steps 12 to 13. The ranking may change, and the level probably will. In the session, the level fell 8× after the fake door while the ranking held.
4. Write the steer into `niche_brief.md`.

## Checks and thresholds

| Check | Threshold |
|---|---|
| two routes agree | within 3× |
| uncovered population u | ≤ 5%, else narrow the target |
| effective sample n_eff | ≥ 30 per number we report |
| largest weight | ≤ 10 × the median, else trim |
| simulated evidence | ranks options, never a level |
| an agent's number | recomputed by us before it enters the ledger |
| a deep-research figure | two sources opened by us |
| an interview "yes" | a specific incident or a workaround, not polite interest |

## Files this produces

| File | Step |
|---|---|
| `research/niche_brief.md` | 1, 13 |
| `research/ledger.csv` | 2 to 5, 12 |
| `research/interviews.md` | 6, 9 |
| `research/competitors.csv` | 7 |
| `research/conversations/` (exports and topic tables) | 8, 13 |
| `research/estimate.ipynb` (routes, Monte Carlo, sensitivity) | 12, 13 |

## Order of work before session 10

1. Brief and ledger skeleton (steps 1 to 2).
2. Book the interviews **now**, because they take the longest (step 6).
3. Open data and competitors in parallel (steps 3, 4, 7).
4. Conversations and reviews (steps 5, 8).
5. Overlap, journey and both routes once the interviews are in (steps 9 to 12).
6. One steering loop, a fake door or desk research, and a journal entry: the top variant by P10, the input that moves it most, how and by when we research it (step 13).
