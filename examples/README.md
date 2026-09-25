# Examples

Real output from both skills, run on small demo skills with deliberate problems.

## skill-audit

`status-note/` is a three-file skill with four planted defects:

- the main file and its format handler give different note lengths;
- the format handler points to a tone file that does not exist;
- a step runs a script that does not exist;
- a signature rule sits in a file that nothing loads.

`status-note/audit-report.md` is the report from `/skill-audit status-note report`. It found all four defects, and it lists what it examined and cleared.

## skill-condense

`release-notes/before.md` is a skill padded with an incident story, a "why" section, and repeated examples. `release-notes/after.md` is the result of `/skill-condense release-notes`: 2,075 bytes down to 824, a 60% cut.

The meaning check confirmed that all six rules survived: the tag lookup, the PR listing, the heading order, the codename ban, the entry format, and the stop on security releases.

Neither the audit nor the condense fixes one issue in this demo. The security-release stop sits in the Final Check, after the notes are already written. That is a sequencing problem in the original, and condensing preserves the original's order. It is the kind of issue `/skill-audit` is for.
