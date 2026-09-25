# Contributing

Issues and pull requests are welcome.

## Reporting a Problem

Open an issue with:

- the skill (`skill-audit` or `skill-condense`) and the command you ran;
- what it did, and what you expected;
- the report, or the relevant part of it, if one was written;
- your Claude Code version (`claude --version`).

If the problem involves one of your own skills, a trimmed-down copy that still shows the problem is the most useful thing you can attach.

## Changing a Skill

- Keep each change small and focused on one behavior.
- Run `/skill-audit` on the skill you changed before you open the pull request, and say in the pull request what it found.
- Add a line to `CHANGELOG.md`.
- These skills must work in any Claude Code setup. Avoid paths, tools, or conventions that exist only in your own environment.
