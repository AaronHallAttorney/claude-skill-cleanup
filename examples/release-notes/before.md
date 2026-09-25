---
name: release-notes
description: Draft release notes from merged pull requests since the last tag.
---
# Release Notes

## Background

We started writing release notes by hand in 2023, and it went badly. On March 3, 2024 a release shipped with notes that mentioned an internal codename, and a customer asked about it on Twitter. After that incident we decided that Claude should draft the notes. This section explains the history so you understand why the rules below exist. It is important to understand that release notes are read by customers, so they matter a great deal.

## Steps

1. Find the last tag with `git describe --tags --abbrev=0`. This is important because the tag marks the previous release. We use tags for every release, and have done so since the project began.
2. List the merged pull requests since that tag. You can do this with `gh pr list --state merged --search "merged:>DATE"`, where DATE is the date of the tag. Remember that the date must be the tag's date.
3. Group the changes under three headings: Added, Fixed, Changed. Always use exactly these three headings, in this order. If a heading has no entries, omit it.
4. Never mention internal codenames. (This is the rule that came from the March 2024 incident. Codenames are names like "Falcon" or "Bluebird" that we use internally. Customers do not know them. So do not mention them.)
5. Write each entry in one sentence, in the past tense, starting with a verb. For example: "Fixed a crash when opening large files." Another example: "Added dark mode." A third example: "Changed the default timeout to 30 seconds."

## Why We Group Changes

Grouping changes helps customers find what matters to them. Research shows that people scan rather than read. We tried other groupings in the past, like by component, but customers found them confusing.

## Final Check

Before finishing, re-read the notes and make sure no codename appears. Codenames must never appear. If the notes are for a security release, stop and ask the user before writing anything, because security wording needs review.
