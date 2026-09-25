# Changelog

## 1.0.1 (2026-09-24)

These fixes came from running `skill-audit` on both skills in this repository.

- **skill-audit, `report` mode:** the read pass no longer skips to the fix pass when a report from the same day already exists.
- **skill-audit, undated contradictions:** when either side of a contradiction is undated or has uncommitted changes, the fix pass asks you instead of defaulting to the newer side.
- **Plugin-installed skills:** both skills now say plainly that these are out of scope, and they name the signs that a skill came from another author.
- **skill-condense, backups:** in a project without git, the backup of the original is saved as `<file>.bak`, so Claude Code never loads it as a second rules file.
- **skill-condense, frontmatter:** frontmatter is never changed, including a rules file's `paths:`.
- **skill-condense, new files:** a new supporting file that a rewrite points to is created in the same step as the rewrite.
- **Examples:** added an example audit report and an example condense before and after.

## 1.0.0 (2026-09-24)

- Initial release of `skill-audit` and `skill-condense`.
