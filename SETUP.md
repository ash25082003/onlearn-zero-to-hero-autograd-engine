# Setup Guide

This project works with any coding assistant that can read local files and run shell
commands. The shared tutoring rules live in `TUTORING.md`; tool-specific files are only
adapters that point back to the same guide.

## Common Setup

1. Clone or download this project.
2. Open a terminal in the project directory.
3. Install the test dependency:

   ```bash
   pip install pytest
   ```

4. Open the project with your preferred coding assistant.
5. Say something like:

   ```text
   Hi, please read the project instructions and tutor me through this exercise.
   ```

The assistant should read `progress.md`, start with the Module 0 diagnostic if this is a
fresh session, and reveal only one milestone at a time.

## Claude Code

Claude Code can use the compatibility files included in this repo:

- `CLAUDE.md` points Claude to `TUTORING.md`.
- `.claude/commands/hint.md`, `.claude/commands/check.md`, and `.claude/commands/next.md`
  provide optional slash-command shortcuts.

Suggested start:

```text
Read CLAUDE.md and tutor me through this project.
```

You can use `/hint`, `/check`, and `/next` if your Claude Code environment supports them.
Plain-language requests like "give me a hint", "run the tests", and "move on" should work
the same way.

## Codex

Codex reads `AGENTS.md` for project instructions. `AGENTS.md` points to `TUTORING.md`, which
contains the full tutoring method.

Suggested start:

```text
Read AGENTS.md and tutor me through this project. Do not write engine.py for me.
```

Useful requests:

- "Give me a small hint."
- "Run the tests."
- "Move to the next milestone if I am ready."

## Cursor

Cursor can use the included rule file:

- `.cursor/rules/tutoring.mdc` tells Cursor to follow `TUTORING.md`.

Suggested start in Cursor chat:

```text
Read TUTORING.md and tutor me through this project. I want to write the code myself.
```

If Cursor does not automatically apply the rule, mention `TUTORING.md` directly in your
first message.

## Other Assistants

For any other coding environment, start by asking the assistant to read:

- `AGENTS.md`
- `TUTORING.md`
- `progress.md`
- `CURRICULUM.md`

Then ask it to tutor, not solve. The assistant should only edit `progress.md` during
milestone tracking; the learner writes `engine.py`.
