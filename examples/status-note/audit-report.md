# Skill audit: status-note (2026-09-24)

Skill folder: `.claude/skills/status-note/` (3 files, all tracked in git commit `75e3dac init`). Project has no git remote, no LICENSE or NOTICES file, and no `CLAUDE.md`. No script in the project names the skill folder (grep for `status-note` outside the folder: 0 hits).

## Load graph

- `SKILL.md` loads on skill invocation.
  - Step 1 (`SKILL.md:6`) loads `handlers/format.md`.
    - `handlers/format.md:2` tells the reader to see `handlers/tone.md`. That file does not exist (see Finding 2).
  - Step 2 (`SKILL.md:7`) writes the output file `notes/status.md`. This is an output, not a load.
  - Step 3 (`SKILL.md:8`) runs `scripts/publish.sh --channel team`. That script does not exist (see Finding 3).
- No script inserts skill text into a prompt.
- **Outside the graph:** `handlers/legacy.md`. No reachable file names it.

## Findings

1. **Contradiction.** Severity high, confidence high.
   - `.claude/skills/status-note/SKILL.md:7`: "Save the note to `notes/status.md`. Default length: 100 words."
   - `.claude/skills/status-note/handlers/format.md:2`: "Keep every note under 50 words."
   - Last changed: SKILL.md 2026-09-24; format.md 2026-09-24. Both come from the same single commit, so the dates do not show which side is deliberate.
   - Why it matters: Step 1 has the reader follow format.md (under 50 words), and then Step 2 gives a 100-word default. Every note gets two incompatible length rules, and which one wins depends on the reader.
   - Smallest fix: pick one length and state it in one file only. For example, delete "Default length: 100 words." from SKILL.md:7, or change format.md:2 to match it.

2. **Stale pointer.** Severity medium, confidence high.
   - `.claude/skills/status-note/handlers/format.md:2`: "See `handlers/tone.md` for tone."
   - Verified: `handlers/tone.md` does not exist in the skill folder, at the project root, or as `handlers/handlers/tone.md`. `find . -name tone.md` returns nothing.
   - Why it matters: the tone guidance never loads, so tone is left unspecified. A reader may also stall or guess.
   - Smallest fix: create `handlers/tone.md` with the intended tone rules, or remove the sentence from format.md:2.

3. **Stale pointer.** Severity medium, confidence high.
   - `.claude/skills/status-note/SKILL.md:8`: "Run `scripts/publish.sh --channel team` to post it."
   - Verified: no `scripts/` directory exists at the project root or in the skill folder, and `find . -name publish.sh` returns nothing. The `--channel` flag cannot be checked because the script is missing.
   - Why it matters: Step 3 always fails, so the note is never posted.
   - Smallest fix: add the script, or point Step 3 at the real publish mechanism. Confirm that it supports `--channel`.

4. **Unreachable directive.** Severity low, confidence high.
   - `.claude/skills/status-note/handlers/legacy.md:1`: "Always sign the note "The Team"."
   - No reachable file references `legacy.md`. A grep for `legacy` across the project finds no hits outside this report.
   - Why it matters: if a signature is still wanted, it is never applied. If it is not wanted, the dead file could be revived by mistake later.
   - Smallest fix: delete `handlers/legacy.md`, or add a reference from SKILL.md or format.md if the signature rule is still current.

## Not findings

- `notes/status.md` (SKILL.md:7) does not exist. This is expected: it is an output path the skill creates, not a pointer to an existing artifact.
- `handlers/format.md` (SKILL.md:6) exists at the path given, relative to the skill folder.
- One-directional defer, SKILL.md to format.md: format.md has no frontmatter or description, so it cannot trigger alone. The defer causes no load-alone risk.
- Premise conflict or imported origin: there is no LICENSE, notices file, or git remote, and the whole skill came in one local commit. Nothing points to external provenance.
- "Use bullets" (format.md:2) is not contradicted by anything in the other files.
- Scripts that load or name the skill's files: none exist in the project (the `.claude/skills/skill-audit/` files do not name `status-note`).
