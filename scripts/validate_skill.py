"""Validate the portable CCU Assistant skill repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FILES = (
    "README.md",
    "SKILL.md",
    "SECURITY.md",
    "LICENSE",
    "start-chrome.bat",
    "start-chrome.sh",
    "references/ccu-ecourse2-dom.md",
    "references/ccu-iccu.md",
    "references/dashboard-template.md",
    "references/output-format.md",
)

FORBIDDEN_PHRASES = (
    "給我帳密",
    "幫你填帳密",
    "provide credentials",
    "use them only for the immediate `fill` action",
)

LOCAL_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")


def _frontmatter(skill_text: str) -> dict[str, str]:
    if not skill_text.startswith("---\n"):
        return {}

    _, raw_frontmatter, _ = skill_text.split("---", maxsplit=2)
    values: dict[str, str] = {}
    current_key: str | None = None

    for line in raw_frontmatter.splitlines():
        if line.startswith((" ", "\t")) and current_key:
            values[current_key] = f"{values[current_key]} {line.strip()}".strip()
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", maxsplit=1)
        current_key = key.strip()
        values[current_key] = value.strip()

    return values


def validate_repository(root: Path) -> list[str]:
    """Return validation errors for a repository root."""
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return errors

    skill_text = skill_path.read_text(encoding="utf-8")
    metadata = _frontmatter(skill_text)
    if metadata.get("name") != "ccu":
        errors.append("SKILL.md frontmatter must define name: ccu")
    if not metadata.get("description"):
        errors.append("SKILL.md frontmatter must include a description")

    searchable_text = skill_text
    readme_path = root / "README.md"
    if readme_path.is_file():
        searchable_text += "\n" + readme_path.read_text(encoding="utf-8")

    lowered_text = searchable_text.casefold()
    for phrase in FORBIDDEN_PHRASES:
        if phrase.casefold() in lowered_text:
            errors.append(f"Unsafe credential instruction found: {phrase}")

    for markdown_path in (skill_path, readme_path):
        if not markdown_path.is_file():
            continue
        markdown_text = markdown_path.read_text(encoding="utf-8")
        for link in LOCAL_LINK_PATTERN.findall(markdown_text):
            target = link.split("#", maxsplit=1)[0]
            if target and not (root / target).exists():
                errors.append(f"Broken local link in {markdown_path.name}: {link}")

    for script_name in ("start-chrome.bat", "start-chrome.sh"):
        script_path = root / script_name
        if not script_path.is_file():
            continue
        script_text = script_path.read_text(encoding="utf-8")
        if "--remote-debugging-address=127.0.0.1" not in script_text:
            errors.append(f"{script_name} must bind debugging to 127.0.0.1")

    return errors


def main() -> int:
    """Validate the repository containing this script."""
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("CCU Assistant validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
