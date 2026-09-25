---
name: release-notes
description: Draft release notes from merged pull requests since the last tag.
---
# Release Notes

## Steps

1. Find the last tag: `git describe --tags --abbrev=0`.
2. List merged PRs since that tag's date: `gh pr list --state merged --search "merged:>DATE"` (DATE = the tag's date).
3. Group entries under exactly these headings, in this order: Added, Fixed, Changed. Omit a heading with no entries.
4. Never mention internal codenames (e.g. "Falcon", "Bluebird") — customers don't know them.
5. Write each entry as one past-tense sentence starting with a verb, e.g. "Fixed a crash when opening large files."

## Final Check

Re-read the notes and confirm no codename appears. If the release is a security release, stop and ask the user before writing anything — security wording needs review.
