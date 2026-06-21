# Module 0 — Prerequisites (taught inline)

Before micrograd, the learner needs two things. Run a quick **diagnostic** at the very
first session, then teach only the warm-ups they actually need. A confident learner can
skip straight to Milestone 1.

## The diagnostic (ask conversationally, don't make it feel like a test)

Find out, in a friendly back-and-forth:

1. **Python classes** — are they comfortable writing a `class` with `__init__` and methods?
2. **Derivatives / chain rule** — do they remember what a derivative is, and roughly what
   the chain rule does?

Based on their answers, route them:
- Solid on both → go straight to Milestone 1.
- Shaky on one → do just that warm-up, then continue.
- New to both → do both warm-ups first.

## Warm-up A — Python objects (only if needed)
Goal: they can write a small class that stores data and has a method. Have them write a
tiny `class` (e.g. a `Counter` with an `increment` method). This is the muscle they'll use
for the `Value` class. Keep it to one small exercise.

## Warm-up B — Derivative & chain rule intuition (only if needed)
Goal: intuition, not rigor. A derivative = "how much does the output change if I nudge the
input." Chain rule = "to get the effect through two steps, multiply the two local effects."
Use one concrete number example. No formal proofs. This is the single idea backprop rests on.

When the needed warm-ups are done (or skipped), continue into the main CURRICULUM.md.
