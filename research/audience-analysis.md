# Audience Analysis: Pre-Interview Screening and Verification Pipeline

> Course project research document. Everything below is reasoning from how hiring works, not searched market data. Treat it as hypotheses to validate. Numbers such as company sizes and prices are deliberately left out for that reason.

## 1. Three groups to separate

| Role | Who | What they care about |
|---|---|---|
| **Buyer** (pays) | Head of HR / People, Talent Acquisition lead, or the owner in a small company | Cost per hire, time to hire, legal risk, reputation |
| **Daily user** | Recruiters, HR generalists | Less manual checking, no chasing documents, less admin |
| **Affected party** | Candidates | Fairness, minimal data requests, getting real feedback |

Hiring managers are a fourth, smaller group. They consume the output (interview-ready candidates) but rarely use the tool directly.

## 2. Candidate customer segments

**Segment A: Small and mid-sized employers (roughly 50 to 500 staff) with a small HR team and high application volume**

- Pain: one or two recruiters drowning in CVs, verification done late or not at all.
- Buying: fast decisions, little procurement, price-sensitive.
- Weakness: may already use a simple ATS and consider verification a luxury.

**Segment B: Recruitment and staffing agencies**

- Pain: volume is their business, and a bad placement damages their reputation.
- Buying: they pay for anything that saves recruiter hours.
- Weakness: many have their own tools and relationships with background-check providers.

**Segment C: Regulated or credential-heavy employers (healthcare, education, finance, public sector, engineering)**

- Pain: credentials genuinely matter and are audited, so false claims carry real consequences.
- Buying: the strongest reason to pay, but slower sales and stricter compliance demands.
- Weakness: may require certified providers, which a new lightweight tool can't be.

**Segment D: Tech hiring teams (GitHub checking is the hook)**

- Pain: portfolio and repo claims are hard to check at scale.
- Weakness: they often use technical assessments instead of document verification.

**Suggested primary segment: A or B.** They have the clearest pain, the shortest sales cycle, and are easiest to interview before session 10. Segment C is the best long-term story but the hardest to prove in two weeks.

## 3. Jobs to be done

- "Get me to a trustworthy shortlist without me checking every claim myself."
- "Stop me finding out at offer stage that something was false."
- "Let me reject people politely and specifically without spending an hour per email."
- "Help me show a regulator or a candidate that the process was fair."

## 4. Pains and what the product relieves

| Pain | Who feels it | Your feature |
|---|---|---|
| Late discovery of false claims | Recruiter, hiring manager | Verification before interview |
| Chasing candidates for documents | Recruiter | Automated proof requests and reminders |
| No time for rejection feedback | Recruiter | Drafted, approved feedback |
| Candidates asked for too much too early | Candidate | Requests only after shortlist |
| Defending a decision | HR lead | Audit trail and human confirmations |
| No overview of where hiring slows down | HR lead | Dashboard of stage counts, common unmet criteria and response times |

## 5. The candidate audience matters too

Candidates aren't paying, but they decide whether the tool works. If asking for documents makes good applicants drop out, buyers will drop the tool. The shortlist-only timing and "why we're asking" explanations are a product advantage and worth stating explicitly in the spec.

## 6. Competitive context (to verify)

- Background-check and ID providers (HireRight, Sterling, Checkr, Veriff) handle verification but often sit outside the screening workflow.
- ATS platforms (Greenhouse, Ashby and similar) handle screening and workflow but typically hand verification to partners.
- **Possible gap, if it holds:** one lightweight flow joining screening, verification tracking and feedback, with human gates built in. This claim needs checking against current products, which is the purpose of the competitor analysis task.

## 7. What to validate before session 10

Talk to 3 to 5 people: a recruiter, an HR generalist, an agency recruiter, and ideally one hiring manager. Ask:

1. When in your process do you verify claims, and how?
2. What happened the last time a claim turned out false?
3. How much time per hire goes on checking and chasing documents?
4. What tools do you use now, and what do you pay?
5. Do you send rejection feedback? Why or why not?
6. Who would approve buying a tool like this?

Also ask 2 or 3 recent job seekers how they would feel about uploading certificates after shortlisting versus at application.

**What counts as evidence of demand:** someone describes a specific recent incident, names the time or money it cost, and already pays for or uses a workaround. Polite interest ("sounds useful") is not evidence.

## 8. Risks specific to this audience

- Recruiters may not want another tool, so it must plug into what they already use (even just via CSV import or an ATS stub).
- Buyers may see verification as the background-check provider's job.
- Candidates and regulators are sensitive to automated decisions, so the human-gates message has to be visible, not buried.

## 9. Where it goes in your repo

Save as `research/audience-analysis.md` on its own branch, and add interview notes to `research/interviews.md` once done, so the spec cites real evidence instead of assumptions.
