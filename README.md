# claude-skill-cleanup

Two Claude Code skills for maintaining your other skills:

- **`skill-audit`** finds contradictions between a skill's files, rules that nothing ever loads, and pointers to paths, flags, headings, or skills that no longer exist. It then fixes what it finds.
- **`skill-condense`** shrinks a bloated skill, rules file, or `CLAUDE.md`. A separate check proves that no rule was lost.

They also work on `CLAUDE.md` and rules files. Run the audit first, because condensing a wrong rule only makes it shorter.

## Why Skills Need Upkeep

Skills pick up cruft as they are edited. Each fix is made with one file open, so over months:

- `SKILL.md` says one thing and a supporting file says another;
- a rule sits in a file that no step tells Claude to read, so it never fires;
- a pointer names something that has since been renamed;
- every fix adds a story, an example, or a paragraph of rationale, which Claude pays for in tokens on every run and which buries the rule it explains.

Each file still looks fine on its own. The problems show up only when you read the skill as a whole, and a checker can see them only if it did not write the file.

## skill-audit

`/skill-audit <skill>` runs two passes.

1. **Read.** A subagent with a fresh context maps which files the skill actually loads, and when. It compares every rule and default across those files and checks that every path, flag, heading, and skill name still exists. It then writes a report that quotes both sides of each finding by file and line. It changes nothing.
2. **Fix.** Your session re-checks every finding against the files, because a report is a list of leads rather than facts. It fixes what is clear and asks you about anything that turns on your preference. When two files conflict, it favors the one changed more recently, because that is usually the deliberate fix.

```
/skill-audit my-skill          # read, then fix
/skill-audit my-skill report   # read only
/skill-audit my-skill fix      # fix the newest open report
```

For the strongest separation between the two passes, run `report`, start a new session, and then run `fix`. Reports are saved to `.claude/skill-audits/`.

## skill-condense

`/skill-condense` with no argument ranks your instruction files by what they cost. A line in an always-loaded `CLAUDE.md` is paid every session. A line in a skill you run once a month is paid once a month. The ranking weighs those costs against the amount of narration each file carries.

`/skill-condense <skill-or-path>` condenses one file:

1. It sorts every block into one of three treatments: keep verbatim (rules, templates, gates), condense (explanation, restatement), or remove or relocate (stories, dated notes, examples the rules already cover).
2. It writes the rewrite to a scratch copy first.
3. A fresh subagent that never saw the rewriting lists every rule, exception, and "must" or "never" in the original, and confirms that each one survived. It also checks that each surviving rule will still be followed. A rule can survive word for word and still stop firing, for example when it is buried in an unrelated paragraph or stripped of the condition that said when it applies.
4. Every fix is checked again, because a fix can break something too. The original is replaced only after the check passes.

A skill's `description` is never condensed, because it decides when Claude uses the skill.

## Install

As a plugin:

```
/plugin marketplace add AaronHallAttorney/claude-skill-cleanup
/plugin install claude-skill-cleanup@claude-skill-cleanup
```

As a plugin, the skills are invoked as `/claude-skill-cleanup:skill-audit` and `/claude-skill-cleanup:skill-condense`.

Or copy either folder under `skills/` into `~/.claude/skills/` (every project) or into your project's `.claude/skills/` (one project).

## Notes

- Neither skill edits a skill that came from a plugin or another author's repository, because an update would overwrite the edit. Both report what they find so you can send it upstream.
- If your project uses git, review the changes as a diff before you commit them. If it does not, `skill-condense` saves the original beside the rewrite as `<file>.before.md`.
- Both skills use subagents, so they draw on your usage like any other Claude Code task.

## Credits

The three contradiction checks in `skills/skill-audit/audit-prompt.md` are quoted from [skill-stocktake](https://github.com/shimo4228/skill-stocktake) by shimo4228, under the MIT License. skill-stocktake reviews a whole library of skills for overlap and retirement candidates, and it works well alongside these skills.

## Author

I'm [Aaron Hall](https://aaronhall.com), a Minnesota business attorney. I run much of my practice's workflow on Claude Code. I built these skills after my own skills had been edited enough times to start contradicting themselves. Issues and pull requests are welcome.

## License

MIT. See `LICENSE`. Third-party notices are in `THIRD-PARTY-NOTICES.md`.
