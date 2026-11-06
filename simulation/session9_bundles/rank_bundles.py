#!/usr/bin/env python3
"""Simulated personas rank the feature bundles (DS403 session 9, step 11: shape only, never a level).

    python rank_bundles.py --check            # every MVP and stretch feature is in exactly one bundle
    python rank_bundles.py --dry-run          # write prompts/rank_<persona>_run<N>.md, call nothing
    python rank_bundles.py                    # read responses/*.json (or call the API), write ranking.md

By hand (no API key): paste each prompt file into a NEW chat, one per file (U6), and save the JSON reply as
responses/rank_<persona>_run<N>.json. Saved answers are reused, so a re-run costs nothing (U13).
Run from this folder or anywhere: paths are relative to this file.
"""
import argparse, datetime, json, os, pathlib, re, sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from simulate_wave import load_personas, dump_persona  # noqa: E402  (same persona reader as wave 1)

UTF8 = {"encoding": "utf-8"}
MODEL = "claude-sonnet-5-5"
ANSWERS = ["like", "expect", "neutral", "tolerate", "dislike"]
# Kano evaluation table: rows = if_present, columns = if_absent.
# A attractive, O one-dimensional (performance), M must-be, I indifferent, R reverse, Q questionable.
KANO = {
    "like":     ["Q", "A", "A", "A", "O"],
    "expect":   ["R", "I", "I", "I", "M"],
    "neutral":  ["R", "I", "I", "I", "M"],
    "tolerate": ["R", "I", "I", "I", "M"],
    "dislike":  ["R", "R", "R", "R", "Q"],
}
KANO_NAME = {"A": "attractive", "O": "performance", "M": "must-be", "I": "indifferent", "R": "reverse", "Q": "questionable"}
FEATURE_ID = r"\b[A-Z]-\d+\b"


def read_bundles(path=HERE / "bundles.md"):
    """Rows of the bundles table: | B1 | name | what you get | MVP | stretch | variant |."""
    bundles = []
    for line in path.read_text(**UTF8).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"B[1-9]", cells[0]):
            bundles.append({"id": cells[0], "name": cells[1], "what": cells[2],
                            "mvp": re.findall(FEATURE_ID, cells[3]), "stretch": re.findall(FEATURE_ID, cells[4])})
    return bundles


def foundation_ids(path=HERE / "bundles.md"):
    text = path.read_text(**UTF8)
    section = text.split("## B0", 1)[1].split("\n## ", 1)[0]
    return re.findall(FEATURE_ID, section)


def feature_priorities(path=HERE.parent.parent / "feature-list.md"):
    """{id: priority} from the feature tables: | ID | Feature | Priority | ..."""
    out = {}
    for line in path.read_text(**UTF8).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and re.fullmatch(r"[A-Z]-\d+", cells[0]) and cells[2] in ("MVP", "Stretch", "Later"):
            out[cells[0]] = cells[2]
    return out


def check():
    """Every MVP and stretch feature sits in exactly one bundle (B0 included); no Later feature does."""
    prio, bundles = feature_priorities(), read_bundles()
    placed = foundation_ids() + [f for b in bundles for f in b["mvp"] + b["stretch"]]
    problems = [f"{f} is in {placed.count(f)} bundles" for f in sorted(set(placed)) if placed.count(f) > 1]
    problems += [f"{f} is not in feature-list.md" for f in placed if f not in prio]
    problems += [f"{f} ({p}) is in no bundle" for f, p in prio.items() if p != "Later" and f not in placed]
    problems += [f"{f} is Later but in a bundle" for f in placed if prio.get(f) == "Later"]
    for b in bundles:
        problems += [f"{f} listed as MVP in {b['id']} but is {prio.get(f)}" for f in b["mvp"] if prio.get(f) != "MVP"]
        problems += [f"{f} listed as stretch in {b['id']} but is {prio.get(f)}" for f in b["stretch"] if prio.get(f) != "Stretch"]
    counts = {p: sum(1 for f in set(placed) if prio.get(f) == p) for p in ("MVP", "Stretch", "Later")}
    total = {p: sum(1 for v in prio.values() if v == p) for p in ("MVP", "Stretch", "Later")}
    print(f"features in feature-list.md: {total}")
    print(f"features placed in B0-B{len(bundles)}: {counts}")
    for p in problems:
        print("PROBLEM:", p)
    print("check passed" if not problems else f"check failed: {len(problems)} problem(s)")
    return not problems


def build_prompt(cast, persona, bundles):
    template = (HERE / "rank_prompt.md").read_text(**UTF8).rsplit("---8<---", 1)[-1].strip()
    table = "\n".join(f"- **{b['id']} · {b['name']}.** {b['what']}" for b in bundles)
    fill = {"product": cast["product"], "persona": dump_persona(persona), "bundles": table}
    for k, v in fill.items():
        template = template.replace("{{" + k + "}}", v.strip())
    return template


def call_api(prompt):
    """Only when a key is set and the anthropic package is installed; otherwise None (by-hand route)."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic
    except ImportError:
        return None
    msg = anthropic.Anthropic().messages.create(model=MODEL, max_tokens=4000,
                                                messages=[{"role": "user", "content": prompt}])
    text = "".join(block.text for block in msg.content if block.type == "text")
    return json.loads(text[text.find("{"): text.rfind("}") + 1])


def validate(answer, ids):
    errors = []
    if sorted(answer.get("ranking", [])) != sorted(ids):
        errors.append(f"ranking must list {ids} once each, got {answer.get('ranking')}")
    got = {b.get("id"): b for b in answer.get("bundles", [])}
    for i in ids:
        b = got.get(i)
        if not b:
            errors.append(f"no Kano answer for {i}")
        elif b.get("if_present") not in ANSWERS or b.get("if_absent") not in ANSWERS:
            errors.append(f"{i}: Kano answers must be one of {ANSWERS}")
    pt = answer.get("proof_timing", {})
    if not all(isinstance(pt.get(k), int) and 1 <= pt[k] <= 5 for k in ("at_application", "after_shortlist")):
        errors.append("proof_timing needs at_application and after_shortlist as integers 1-5")
    return errors


def spearman(r1, r2):
    n = len(r1)
    pos2 = {b: i for i, b in enumerate(r2)}
    d2 = sum((i - pos2[b]) ** 2 for i, b in enumerate(r1))
    return 1 - 6 * d2 / (n * (n * n - 1))


def kano(b):
    return KANO[b["if_present"]][ANSWERS.index(b["if_absent"])]


def write_report(cast, bundles, answers, runs, out):
    ids = [b["id"] for b in bundles]
    names = {b["id"]: b["name"] for b in bundles}
    people = [p for p in cast["personas"] if all((p["id"], r) in answers for r in range(1, runs + 1))]
    ranks = {i: [] for i in ids}
    for (pid, r), a in answers.items():
        for pos, i in enumerate(a["ranking"], 1):
            ranks[i].append(pos)
    order = sorted(ids, key=lambda i: sum(ranks[i]) / len(ranks[i]))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = [f"# Bundle ranking by simulated personas",
         "",
         f"**Kind: simulated.** {len(people)} personas × {runs} runs = {len(answers)} answers, generated {now} "
         f"by `rank_bundles.py` from `responses/`. Session 9, step 11: this ranks the bundles (a shape); it says "
         f"nothing about how many real recruiters or candidates want them (U8, A6). Do not hand-edit (A12).",
         "",
         "## 1. Overall order (mean rank over all answers, 1 = most important)",
         "",
         "| Order | Bundle | Mean rank | Best–worst | Ranks (all answers) |",
         "|---|---|---|---|---|"]
    for n, i in enumerate(order, 1):
        rs = ranks[i]
        L.append(f"| {n} | {i} · {names[i]} | {sum(rs) / len(rs):.2f} | {min(rs)}–{max(rs)} | {', '.join(map(str, rs))} |")
    L += ["", "## 2. Each persona, each run", "",
          "| Persona | " + " | ".join(f"Run {r}" for r in range(1, runs + 1)) + " | Agreement between runs (Spearman ρ) |",
          "|---|" + "---|" * runs + "---|"]
    for p in people:
        rk = [answers[(p["id"], r)]["ranking"] for r in range(1, runs + 1)]
        rho = [spearman(rk[0], x) for x in rk[1:]]
        L.append(f"| {p['name']} | " + " | ".join(" > ".join(x) for x in rk) + f" | {', '.join(f'{v:.2f}' for v in rho)} |")
    L += ["", "ρ = 1: both runs gave the same order; ρ near 0: the order is not stable for that persona (U7).",
          "", "## 3. Kano category per persona and bundle", "",
          "A attractive (delighter) · O performance · M must-be · I indifferent · R reverse (they would rather not have it) "
          "· Q questionable. Runs are separated by `/`; a single letter means all runs agree.", "",
          "| Persona | " + " | ".join(ids) + " |", "|---|" + "---|" * len(ids)]
    agree = total = 0
    for p in people:
        row = []
        for i in ids:
            cats = [kano(next(b for b in answers[(p["id"], r)]["bundles"] if b["id"] == i)) for r in range(1, runs + 1)]
            agree += len(set(cats)) == 1
            total += 1
            row.append(cats[0] if len(set(cats)) == 1 else "/".join(cats))
        L.append(f"| {p['name']} | " + " | ".join(row) + " |")
    L += ["", f"Kano categories that agree across runs: {agree} of {total} persona–bundle pairs.",
          "", "## 4. Proof timing (session 9, step 11: the relative drop, not a rate)", "",
          "| Persona | At application (1–5, per run) | After shortlist (1–5, per run) | Why (run 1) |",
          "|---|---|---|---|"]
    for p in people:
        pts = [answers[(p["id"], r)]["proof_timing"] for r in range(1, runs + 1)]
        L.append(f"| {p['name']} | {', '.join(str(x['at_application']) for x in pts)} | "
                 f"{', '.join(str(x['after_shortlist']) for x in pts)} | {pts[0].get('why', '')} |")
    L += ["", "## 5. When each persona would meet each bundle (run 1, their words)", ""]
    for i in ids:
        L.append(f"**{i} · {names[i]}**")
        L.append("")
        for p in people:
            b = next(b for b in answers[(p["id"], 1)]["bundles"] if b["id"] == i)
            L.append(f"- *{p['name']}* ({KANO_NAME[kano(b)]}): {b.get('when_i_would_meet_it', '')} {b.get('why', '')}")
        L.append("")
    (out / "ranking.md").write_text("\n".join(L) + "\n", **UTF8)
    print(f"wrote {out / 'ranking.md'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--personas", default=str(HERE.parent / "personas.yaml"))
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--out", type=pathlib.Path, default=HERE)
    ap.add_argument("--dry-run", action="store_true", help="write the prompts only")
    ap.add_argument("--check", action="store_true", help="check bundles.md against feature-list.md and stop")
    args = ap.parse_args()
    if args.check:
        sys.exit(0 if check() else 1)

    cast, bundles = load_personas(args.personas), read_bundles()
    ids = [b["id"] for b in bundles]
    (args.out / "prompts").mkdir(parents=True, exist_ok=True)
    (args.out / "responses").mkdir(parents=True, exist_ok=True)
    answers, missing = {}, []
    for p in cast["personas"]:
        prompt = build_prompt(cast, p, bundles)
        for r in range(1, args.runs + 1):
            name = f"rank_{p['id']}_run{r}"
            (args.out / "prompts" / f"{name}.md").write_text(prompt + "\n", **UTF8)
            resp = args.out / "responses" / f"{name}.json"
            if not resp.exists() and not args.dry_run:
                got = call_api(prompt)
                if got is not None:
                    resp.write_text(json.dumps(got, indent=2, ensure_ascii=False) + "\n", **UTF8)
            if not resp.exists():
                missing.append(name)
                continue
            answer = json.loads(resp.read_text(**UTF8))
            errors = validate(answer, ids)
            if errors:
                sys.exit(f"{resp.name}: " + "; ".join(errors))
            answers[(p["id"], r)] = answer
    print(f"prompts: {len(cast['personas']) * args.runs} in {args.out / 'prompts'}")
    if args.dry_run or missing:
        if missing:
            print(f"waiting for {len(missing)} answer(s) in responses/: " + ", ".join(missing))
        return
    write_report(cast, bundles, answers, args.runs, args.out)


if __name__ == "__main__":
    main()
