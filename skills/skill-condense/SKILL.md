---
name: skill-condense
description: 'Shrink a bloated skill, rules file, or CLAUDE.md without losing any instruction. Run bare to rank which instruction files cost the most context for the least value; pass a skill name or path to condense one. Each rewrite is checked by a fresh-context reader that confirms every rule survived and will still be followed. Use for "/skill-condense", "this skill is too long", or "trim my CLAUDE.md". Not for finding contradictions or broken pointers (use /skill-audit first).'
argument-hint: '[skill-name | path]'
---

# Skill Condense

Instruction files grow. Each fix adds a sentence, a war story, an example, or a paragraph on why the rule exists. Claude pays for every one of those tokens on every run, and a rule buried in narration is less likely to be followed. This skill rewrites a file down to what the model actually needs: each rule, stated once, plus a pointer to wherever the detail lives. It then proves that no rule was lost.

If the skill might also contain contradictions or stale pointers, run `/skill-audit` on it first. Condensing text that is wrong only makes it shorter and still wrong.

## Who the Rewrite Is For

Write for the model and effort level that actually run the file day to day, not the strongest one available. A terse pointer that a top model expands correctly can be too thin for a smaller model or a lower effort setting. A new model release is not by itself a reason to condense; the reason is visible bloat.

## Mode A: Triage (`/skill-condense` with no argument)

Read-only. Consider `CLAUDE.md` files, `.claude/rules/*.md`, and every `SKILL.md` under the project's `.claude/skills/` and `~/.claude/skills/`.

1. **Load cost comes first.** It sets how often the saved tokens are paid:
   - **Always loaded** (CLAUDE.md files and rules without a `paths:` scope) are paid every session.
   - **Frequently used skills** are paid on each of their runs.
   - **Rarely used skills** are paid only on those rare runs.

   One line cut from an always-loaded file is worth many lines cut from a rarely used skill. If you cannot tell how often a skill runs, ask the user which skills they use most.
2. **Bloat signals:**
   - dated notes and incident stories ("on March 3 this broke…");
   - "Why this exists" sections;
   - worked examples;
   - the same rule restated in several places;
   - long prose wrapped around a short rule.
3. **Verdict per file:**
   - **CONDENSE:** real savings are available.
   - **MARGINAL:** a rarely used file where the savings would take too long to matter.
   - **AT-FLOOR:** already lean, or mostly exact content (tables, templates, required parameters) that must stay verbatim. A skill that has already moved its rarely needed sections into separate files, and has little narration left, is usually at floor.

Output a table with these columns: file, load cost, size, verdict, top signal, estimated savings weighted by load cost, and one line of reasoning. List always-loaded files first. Make no edits.

## Mode B: Condense One File (`/skill-condense <skill-name | path>`)

1. **Resolve the target.** A bare name means `.claude/skills/<name>/SKILL.md` in the project, else `~/.claude/skills/<name>/SKILL.md`. If the file came from a plugin or another author's repository, stop: an update would overwrite the edit, so suggest the change upstream instead.
2. **Classify every block** into one of the buckets in `classification.md`, which is in this skill's folder.
3. **Write the rewrite to a scratch copy,** never over the original yet.
   - Keep every rule.
   - Compress explanation to the rule plus a pointer.
   - Remove or relocate stories and examples as the classification says.
   - A pointer must target a file that exists and actually carries the detail.
   - Before renaming or removing a heading, search the project for other files that point to it. Either keep the heading as written or fix every pointer in the same change.
   - "This duplicates X" is a claim to verify: open X and confirm it says the same thing at the same depth before cutting. If the block is the only thing that makes a promise elsewhere in the skill work, it stays.
4. **Run the meaning check.**
   - Launch a fresh subagent (Agent tool, general-purpose type) with the prompt in `meaning-check.md` (in this skill's folder), the ORIGINAL text, the REWRITE text, and the paths of any files the rewrite points to.
   - Give it nothing else from this conversation.
   - If the user's everyday model differs from this session's, pass that model to the subagent. A stronger verifier approves text that only a stronger model can follow.
5. **Fix and re-check.** Fix every item the check returns, then run the check again on the fixed rewrite. A fix is an edit like any other and can break something new. Repeat until the check returns PASS.
6. **Apply.**
   - If the project is not under git, first save the original as `<file>.before.md` beside it so the change can be undone.
   - Replace the original with the rewrite.
   - Report the before and after sizes (lines and bytes), the PASS verdict, and any judgment calls the checker flagged.
   - Condense one file per run, so each change can be reviewed or reverted on its own.

## Guardrails

- Never condense a skill's frontmatter (`name`, `description`, `argument-hint`). The description decides when Claude uses the skill. A shorter one can pass the meaning check and still make the skill stop firing on requests it used to catch.
- Never soften a rule while compressing around it: must stays must, never stays never.
- Never reword exact content: templates, required parameters, safety rules, and anything a script parses.
