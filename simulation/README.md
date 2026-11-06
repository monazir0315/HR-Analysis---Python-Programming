# Simulated-user-driven development (SUDD)

How this project uses the loop from DS403 session 10: simulated users critique the product in **waves**,
and a fixed **directive** decides which of their requests get built. Rules: [`../rules/USER_SIMULATION.md`](../rules/USER_SIMULATION.md) (U1–U13).

```text
directive (fixed) → personas → critique (each persona, twice) → triage (≤ 5 changes) → build → walk again → 3–5 real people
```

## The files

| File | What it is |
|---|---|
| [`directive.md`](directive.md) | What the product is for, and invariants I1–I5 that no wave may break. **Draft: the product owner edits and commits it** (U1, U2) |
| [`personas.yaml`](personas.yaml) | Four fictional personas that disagree: a recruiter (laptop), the HR lead (non-cooperative, asks for rankings), a shortlisted candidate (phone, wary of scams), an unsuccessful candidate (angry). Each has typical mistakes (U3, U4) |
| [`simulate_wave.py`](simulate_wave.py) | The course script: one wave = critiques + triage → `findings.json` and `wave.md` |
| [`ux_critic.md`](ux_critic.md) · [`wave_triage.md`](wave_triage.md) | The two prompts the script sends |
| `wave1_structure/` | Wave 1, on the written structure (stage 2): input [`structure.md`](wave1_structure/structure.md), the 9 saved prompts in `prompts/` |
| `session9_bundles/` | Session 9, steps 10, 11 and 13: features grouped into 6 bundles ([`bundles.md`](session9_bundles/bundles.md)), usage scenarios per bundle ([`scenarios.md`](session9_bundles/scenarios.md)), and personas ranking the bundles with a Kano pair (`rank_bundles.py`, 8 saved prompts). Shape only, never a level |

## The three passes, cheapest first

| Pass | What the personas see | Status |
|---|---|---|
| 1 · Mockups | Screenshots of `mockup/prototype.html` | To do after wave 1: screenshots listed below |
| 2 · Structure | `wave1_structure/structure.md`: brief, journey, user situations US.01–US.24, what the product does not do | **Wave 1 done 2026-11-05:** 60 findings, 5 accepted / 25 deferred / 3 rejected ([wave.md](wave1_structure/wave.md)); the 5 accepted changes are built in the prototype |
| 3 · Built product | Screenshots of the real Python app, phone and laptop | After the build |

Wave 1 starts at the structure (pass 2) because no model or browser automation is set up on this machine
yet; a missing situation found now costs a paragraph, not a rebuild.

## Run wave 1

All commands from this folder (`simulation/`).

**With an API key** (`pip install anthropic`, `ANTHROPIC_API_KEY` set): one command does everything.

```bash
python simulate_wave.py --directive directive.md --personas personas.yaml \
    --text wave1_structure/structure.md --runs 2 --out wave1_structure
```

**Without a key (by hand), as on 2026-11-05.** The prompts are already saved:

1. For each of the 8 files `wave1_structure/prompts/critique_<persona>_run<N>.md`: open a **new** chat
   (Claude or ChatGPT), paste the whole file, and save the JSON reply as
   `wave1_structure/responses/critique_<persona>_run<N>.json`. One chat per file: never two personas, or two
   runs, in one chat (U6).
2. Run the command above with `--dry-run` added. It reads the 8 answers, writes `findings.json`, and saves
   `prompts/triage.md` with every finding filled in.
3. Paste `prompts/triage.md` into a new chat, ideally a different model from the critics. Save the reply as
   `responses/triage.json`.
4. Run the command once more (without `--dry-run` is fine: saved answers are reused, nothing is called).
   It writes `wave.md`: at most 5 accepted changes, the deferred list, what must not change and the steps
   to walk again.

Then build the accepted changes in `mockup/prototype.html`, commit, and run the next wave (U12).

## How wave 1 was run (U13)

2026-11-05. No API key, so the script's by-hand route, with fresh agents doing the pasting: each of the 8
critique prompts was answered by its own agent on Claude Sonnet that read only that prompt file; the triage
by one agent on Claude Opus that read only `prompts/triage.md`. 9 model calls. The JSON shape was checked after
the fact (all valid; every finding F01–F60 lands in exactly one change) instead of being enforced by the API.
The directive was the unedited draft.

Commands, from this folder:

```bash
python simulate_wave.py --directive directive.md --personas personas.yaml \
    --text wave1_structure/structure.md --runs 2 --out wave1_structure --dry-run   # writes prompts
# … answers saved to wave1_structure/responses/ …
python simulate_wave.py --directive directive.md --personas personas.yaml \
    --text wave1_structure/structure.md --runs 2 --out wave1_structure             # writes wave.md
```

**Built** in `mockup/prototype.html` (W1–W5) and checked in headless Edge with a scripted walk: 37 checks, 37 passed,
including the invariant checks (no candidate names on the dashboard, proof only for shortlisted candidates,
uncited feedback reasons blocked). One change of behaviour to note in the spec: shortlisting no longer sends
the proof request; the recruiter previews and confirms it (W5).

**Next:** walk again (U12) with the same personas on screenshots of the "Walk again" steps in `wave.md`,
then 3–5 real people.

## How the session 9 bundle ranking was run (U13)

2026-11-06. No API key, so the by-hand route: each of the 8 prompts in `session9_bundles/prompts/` was answered
by its own fresh agent on Claude Sonnet (`claude-sonnet-5-5`) that read only that prompt file. 8 model calls.
Then, from `session9_bundles/`: `python rank_bundles.py --check` (coverage) and `python rank_bundles.py`
(validates the 8 answers and writes [`ranking.md`](session9_bundles/ranking.md)). Result is `simulated`: a shape, not a level.

## Pass 1 later: screenshots of the prototype

Take them in the browser (phone width 390 px in DevTools for Priya and Tomasz, laptop for Inés and Daniel),
save them in `wave2_mockups/`, then run with `--screens` instead of `--text`:

| Persona | Screens |
|---|---|
| Inés (recruiter) | Create role steps 1–2, role pipeline, candidate detail, verification queue, feedback |
| Daniel (HR lead) | Dashboard, audit log |
| Priya (candidate) | Proof request email (outbox), candidate upload page |
| Tomasz (unsuccessful) | Feedback email (outbox) |

The script sends the same screens to every persona, so either pass all of them, or run one wave per group
with its own `--personas` file.

## What to write in the journal

Your directive; wave 1 with its numbers (findings, accepted, deferred, rejected); one rejected change and the
directive line that rejected it; the journey steps you will walk again.

## Limits (U8)

These are simulated users: their findings are hypotheses to check, never rates. Do not write "N% of users"
from them. Two runs of one persona often disagree on half of what they find, so read the spread in `wave.md`.
Simulated users are too cooperative, which is why Daniel and Tomasz are written as difficult on purpose.
Every wave ends with 3–5 real people walking one journey each.
