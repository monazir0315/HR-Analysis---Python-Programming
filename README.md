# HR-Analysis---Python-Programming

A lightweight web app for recruiters, built in Python, that:

1. **Screens** applicants against the role's must-have criteria from the job description, and flags what each candidate is missing (for example, "missing: at least 5 years of experience").
2. **Verifies** the claims of shortlisted candidates before interview, by requesting proof only after shortlisting (for example, a degree certificate for "First Class Honours") and sending reminders automatically.
3. **Drafts feedback** for unsuccessful candidates that cites the specific, job-related criteria they did not meet.
4. **Shows a dashboard** of totals per role: candidates at each stage, the most common unmet criteria, and proof response times.

It works on its own, or alongside an existing ATS by importing applicants from a CSV export.

Every consequential decision stays with a human. The AI flags and drafts; a recruiter confirms every shortlist, every verified document and every rejection message. The system never ranks or scores candidates.

- Spec: `Python Programming - HR Analysis.docx`
- Research: [`research/`](research/)
