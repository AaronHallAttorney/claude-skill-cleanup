# Classification

Sort every block of the target file into one bucket before rewriting.

| Bucket | What belongs here | Action |
|---|---|---|
| **Keep verbatim** | Hard rules (must, never, stop), safety and permission gates, required parameter sets, templates meant to be pasted exactly, reference tables, text a script parses, live pointers to other files | Leave untouched. Strip narration around them, never the rule itself. |
| **Keep verbatim: frontmatter** | The whole frontmatter block: a skill's `name`, `description`, `argument-hint`; a rules file's `paths:` | Never change. It decides when the file loads and when the skill fires. |
| **Condense** | Explanation, restatement of a rule already given, multi-sentence rationale | Reduce to the rule in one line, plus a pointer if the detail lives elsewhere. |
| **Remove or relocate** | Incident stories, dated notes, "why this exists" sections, worked examples the rules already cover | Remove it. If the text is still useful to a human reader, move it to a separate notes file the skill never loads. If a step needs it only in a rare mode, move it to a supporting file and leave a one-line pointer saying when to read it. |

## Judgment Calls

- **A story usually produced a rule.** Keep the rule and drop the story.
- **FAQ sections.** A question and answer that encodes a rule ("Where does X go? In Y.") becomes a plain rule. A pure "why" answer can go.
- **Examples.** Keep examples that mark the boundary of when a rule applies, meaning which cases are in scope and which are not. Illustrative examples of an already-clear rule can go.
- **The same rule in two places.** Keep the fuller statement where it fires. Reduce the other copy to a pointer.
- **Rarely used modes.** In a long, frequently used skill, the largest savings usually come from moving rarely used sections into their own file. Leave behind a stub that says when to read that file and what to do if it is missing. Prose trimming alone often saves only a few percent.
- **The rule's trigger stays.** When you move a conditional step into a separate file, keep the condition that decides whether the step runs in the main file. Only the mechanics move.
