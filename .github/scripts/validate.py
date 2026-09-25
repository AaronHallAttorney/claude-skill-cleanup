"""Checks the plugin manifests, the changelog version, and each skill's frontmatter and file pointers."""
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parents[2]
errors = []

plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
entry = next((p for p in market["plugins"] if p["name"] == plugin["name"]), None)
if entry is None:
    errors.append("marketplace.json has no entry for plugin " + plugin["name"])
elif entry.get("version") != plugin["version"]:
    errors.append(f"version mismatch: plugin.json {plugin['version']}, marketplace.json {entry.get('version')}")

changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
top = re.search(r"^## (\S+)", changelog, re.M)
if not top or top.group(1) != plugin["version"]:
    errors.append(f"CHANGELOG.md top entry is not version {plugin['version']}")

for skill_md in sorted((root / "skills").glob("*/SKILL.md")):
    folder = skill_md.parent
    text = skill_md.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        errors.append(f"{skill_md}: missing frontmatter")
        continue
    name = re.search(r"^name:\s*(\S+)", fm.group(1), re.M)
    if not name or name.group(1) != folder.name:
        errors.append(f"{skill_md}: name does not match folder {folder.name}")
    if not re.search(r"^description:\s*\S", fm.group(1), re.M):
        errors.append(f"{skill_md}: missing description")
    for ref in set(re.findall(r"`([a-z0-9-]+\.md)`", text)):
        if not (folder / ref).exists():
            errors.append(f"{skill_md}: points to {ref}, which is not in {folder.name}/")

for e in errors:
    print("ERROR:", e)
print("OK" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
