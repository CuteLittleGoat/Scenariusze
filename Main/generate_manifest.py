#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

SECTION_CONFIG = [
    {"id": "analizy", "title": "Analizy", "segments": ["Analizy"]},
    {"id": "notatki", "title": "Warhammer40k/Notatki", "segments": ["Warhammer40k", "Notatki"]},
    {"id": "gilead", "title": "Warhammer40k/Gilead", "segments": ["Warhammer40k", "Gilead"]},
    {"id": "oko", "title": "Warhammer40k/Scenariusz_Oko", "segments": ["Warhammer40k", "Scenariusz_Oko"]},
    {"id": "rico", "title": "Warhammer40k/Scenariusz_Rico", "segments": ["Warhammer40k", "Scenariusz_Rico"]},
    {"id": "epilog", "title": "Warhammer40k/Scenariusz_Epilog", "segments": ["Warhammer40k", "Scenariusz_Epilog"]},
]

ALLOWED_EXTENSIONS = {".html", ".md", ".txt", ".png"}


def scan_directory(root: Path, segments: list[str]) -> list[str]:
    directory = root.joinpath(*segments)
    if not directory.exists() or not directory.is_dir():
        return []

    files = [
        path.name
        for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() in ALLOWED_EXTENSIONS
    ]
    return sorted(files, key=lambda item: item.casefold())


def build_manifest(repo_root: Path) -> dict:
    sections = []
    for section in SECTION_CONFIG:
        sections.append(
            {
                "id": section["id"],
                "title": section["title"],
                "segments": section["segments"],
                "files": scan_directory(repo_root, section["segments"]),
            }
        )

    return {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sections": sections,
    }


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    output_path = script_dir / "files-manifest.json"

    manifest = build_manifest(repo_root)
    output_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Manifest wygenerowany: {output_path}")


if __name__ == "__main__":
    main()
