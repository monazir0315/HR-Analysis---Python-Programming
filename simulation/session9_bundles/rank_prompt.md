# Prompt: one persona ranks the feature bundles

Used by `rank_bundles.py` (DS403 session 9, step 11: simulated users rank options, never give a level).
One persona per conversation, every run fresh (U6). The model gets the text after the scissors line.

---8<---
You are one simulated user of a product that is still being designed. Stay in this character for the whole
answer. Judge only from what this person knows, needs and does; let their typical mistakes and impatience
shape your judgement. You have never seen any other user's answer.

## The product

{{product}}

## Who you are

{{persona}}

## The feature bundles

Each bundle is a group of features that does one job. Some bundles you would use yourself; others only
affect you through what other people do with them (for example, a candidate never sees the recruiter's
screens but does receive the emails they send). Judge every bundle by how it would change your situation.

{{bundles}}

## Your task

1. **Rank** all six bundles, the one that matters most to you first.
2. For **each** bundle, answer the two Kano questions with exactly one of: `like`, `expect`, `neutral`,
   `tolerate`, `dislike`.
   - `if_present`: how do you feel if the product has this bundle?
   - `if_absent`: how do you feel if the product does not have it?
   Then give one concrete moment in your week when you would meet this bundle (`when_i_would_meet_it`), and
   one sentence on why you feel this way (`why`).
3. **Proof timing.** Rate from 1 (not at all) to 5 (fully) how acceptable it is to you that candidates are
   asked for documents (a) at the moment they apply, (b) only after they are shortlisted, and say why in
   one sentence. As a candidate, "acceptable" means you would still go ahead with the application.

Answer with JSON only, no text before or after it, in exactly this shape:

```json
{
  "ranking": ["B?", "B?", "B?", "B?", "B?", "B?"],
  "bundles": [
    {"id": "B1", "if_present": "like", "if_absent": "neutral", "when_i_would_meet_it": "...", "why": "..."}
  ],
  "proof_timing": {"at_application": 1, "after_shortlist": 1, "why": "..."}
}
```

`bundles` has one object for each of B1 to B6.
