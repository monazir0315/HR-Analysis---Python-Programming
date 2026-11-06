# Directive — Pre-Interview Screening and Verification Pipeline

<!--
DRAFT proposed by Claude on 2026-11-05 from the spec, README.md and feature-list.md (U2, D10).
The directive belongs to the product owner: edit it, then commit it yourself as its own commit,
outside any wave. Once the first wave has run, do not change it until the loop ends (U1).
-->

## Directive

The pipeline helps in-house recruiters at small and mid-sized companies get from a pile of applications to
interview-ready candidates whose claims have been checked, by flagging each CV against the role's must-haves,
asking only shortlisted candidates for proof, and drafting specific feedback for the people who are not taken
forward. Every flag and every feedback sentence names the job-related criterion behind it and the CV text or
record it rests on. A named recruiter decides every shortlist, every verified item and every message sent;
candidates always know what is asked of them and why; the HR lead sees totals, never individuals ranked.

## Invariants (what no wave may break)

- **I1 — A person decides.** No candidate is shortlisted, no proof item is marked verified and no message
  reaches a candidate without a named recruiter's confirmation, recorded in the audit log.
- **I2 — Flags, not scores.** No screen ranks, scores or orders candidates by fit; candidate lists sort only
  by date applied or name, and results read "meets", "missing" or "needs human review", never "rejected".
- **I3 — Every reason is job-related and traceable.** Every flag and every feedback sentence cites a criterion
  of the role and the CV text or record it rests on; nothing mentions a protected characteristic, another
  candidate or a ranking.
- **I4 — Proof only after shortlisting, and always with the reason.** Proof is requested only from shortlisted
  candidates, only for claim types in the role's verification list, and the candidate sees why each item is
  asked for and how long it is kept.
- **I5 — Totals, not people, on the dashboard.** The dashboard shows counts, rates and durations for groups;
  it never shows an individual candidate's data, and personal data is deleted when the retention period ends.
