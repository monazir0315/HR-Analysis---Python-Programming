# AGENTS.md

Standing instructions for every coding agent in this repository: Claude Code, Codex, Cursor, Copilot, ChatGPT.
The full rules are in `rules/`. When you apply a rule, cite its id, e.g. "(D8)".

## Product directive (owned by the human)

The pipeline helps in-house recruiters at companies of 50 to 500 staff get from a pile of applications to
interview-ready candidates whose claims have been checked: it flags each CV against the role's must-haves, asks
only shortlisted candidates for proof, and drafts specific feedback for the people not taken forward. A named
recruiter decides every shortlist, verified item and message; the HR lead sees totals, never ranked individuals.
"Done" this term: the MVP features in `feature-list.md` work on synthetic data, with tests, by the course deadline.

**Must not change without the human** (full text: `simulation/directive.md`):
I1 a person decides · I2 flags, not scores · I3 every reason is job-related and traceable ·
I4 proof only after shortlisting, always with the reason · I5 totals, not people, on the dashboard.

The agent never edits this section or `simulation/directive.md`. To change them, it proposes new text and the human commits it (U2).

## Always on

1. Requirements and user situations before code; plan in tasks of 20–30 minutes (D1, D3).
2. Run the tests yourself before "done"; fix the code, never weaken a test (D7).
3. No claim without the command and the output that show it (D8).
4. Every number has a source, an as-of date and a kind, and code that reproduces it (A3, A12).
5. Keep sourced fact, your analysis and speculation apart, and label each (A6).
6. When unsure, write the question with its default, apply it, log it, continue; stop only before
   anything irreversible or public (D10).
7. Commit each working step, stage only your own files, push before you stop (D11, D13).
8. No personal data, no real person as a persona, no keys in files or prompts; all CVs are synthetic (A13).

## Read when

| When you are about to … | Read first |
|---|---|
| collect data, compute a number, write a finding or a recommendation | `rules/ANALYTICS_RULES.md` |
| publish a slide, a post or a summary of results | `rules/ANALYTICS_RULES.md`, A14 |
| write requirements, plan, code, test or commit | `rules/DEVELOPMENT_RULES.md` |
| let simulated users critique a screen, or triage their findings into a wave | `rules/USER_SIMULATION.md`, then `simulation/README.md` |
| call a user-facing feature done | `rules/USER_SIMULATION.md`, then D9 |
| work while other agents or teammates change the same repo | `rules/DEVELOPMENT_RULES.md`, D13 and D14 |
| end a session or hand over to someone | `rules/DEVELOPMENT_RULES.md`, D15 |

## Project facts

- Run the tests: not set up yet (no app code yet)
- Run the app: open `mockup/prototype.html` in a browser (clickable prototype on fixtures)
- Run a simulated-user wave: see `simulation/README.md`
- Spec: `Python Programming - HR Analysis.docx` · features and ids: `feature-list.md` · research: `research/`
- Directive and personas: `simulation/directive.md`, `simulation/personas.yaml`
