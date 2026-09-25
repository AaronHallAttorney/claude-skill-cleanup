# Meaning Check Prompt

Give the subagent this prompt, followed by the ORIGINAL text, the REWRITE text, and the paths of any files the rewrite points to.

```
You are verifying that a condensed rewrite changed NOTHING about meaning. You did
not write it and must not trust it. Inputs: ORIGINAL and REWRITE (+ any pointer
targets named in the rewrite).

Enumerate every directive, constraint, exception, enumerated case, cross-reference,
and modal (MUST/NEVER/always/never) in ORIGINAL. For each, confirm it survives in
REWRITE or in a file the rewrite explicitly points to. Read each pointer target
before counting a directive as preserved there. Hunt specifically for: dropped
exceptions, softened modals (MUST->should, NEVER->avoid), orphaned or broken
references, lost enumerated cases, and punctuation changes that alter scope (a
dash or colon that turns one item of a list into a condition on the others).

Then re-read REWRITE alone, as its operator would. For each surviving directive, ask
whether it is still as likely to FIRE. A directive loses salience, even with its text
intact, when it is demoted from its own heading into a sub-clause, folded into a
paragraph carrying unrelated content, stripped of the trigger condition that told the
operator when it applies, or moved behind a pointer the operator has no reason to
follow at that step.

Check the frontmatter separately: the whole block between the opening and closing
--- lines must be byte-identical to ORIGINAL.

Return PASS only if every item survives AND none lost salience AND the frontmatter
is unchanged. Otherwise return two numbered lists, DROPPED/WEAKENED and SALIENCE,
each quoting the ORIGINAL text. Ignore style and length; judge only whether meaning
survives and whether it still fires.
```
