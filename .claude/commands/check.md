Run the test suite and react like a teacher, not a CI bot.

1. Run: `python -m pytest -q`
2. If tests pass for the current milestone: celebrate briefly (one line), update
   `progress.md`, and ask if they want to go to `/next`.
3. If they fail: do NOT show the full traceback or fix it for them. Read the failure,
   then give the smallest hint that points them toward the problem. Keep it to a
   sentence or two. Let them try again.
