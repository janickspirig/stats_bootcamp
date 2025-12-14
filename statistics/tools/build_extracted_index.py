#!/usr/bin/env python3
"""
Build index files for extracted lecture artifacts.

Outputs:
- extracted/index.json (machine-readable)
- extracted/index.md (human-readable)
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path("/Users/Janick_Spirig/git_local/stats_bootcamp")
EXTRACTED_DIR = ROOT / "extracted"
LECTURE_SLIDE_DIR = ROOT / "lecture_slide"


@dataclass(frozen=True)
class LectureEntry:
    lecture_number: int
    lecture_id: str  # e.g. Lecture_3_STAT
    pdf_path: str
    extracted_dir: str
    manifest_path: str
    notes_path: str
    pages_dir: str
    embedded_dir: str
    total_pages: int
    total_embedded_images: int


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _lecture_number_from_id(lecture_id: str) -> int:
    # Expected: Lecture_{n}_STAT
    try:
        parts = lecture_id.split("_")
        return int(parts[1])
    except Exception as e:  # pragma: no cover
        raise ValueError(f"Unrecognized lecture folder name: {lecture_id}") from e


def _build_entry(lecture_folder: Path) -> LectureEntry:
    lecture_id = lecture_folder.name
    lecture_number = _lecture_number_from_id(lecture_id)

    manifest_path = lecture_folder / "manifest.json"
    manifest = _read_json(manifest_path)

    total_pages = int(manifest.get("total_pages", 0))
    total_embedded = 0
    for p in manifest.get("pages", []):
        total_embedded += int(p.get("embedded_count", 0))

    # Canonical paths (absolute, as requested in your workspace preferences)
    pdf_path = str(LECTURE_SLIDE_DIR / f"{lecture_id}.pdf")
    notes_path = str(lecture_folder / f"{lecture_id}_notes.txt")

    return LectureEntry(
        lecture_number=lecture_number,
        lecture_id=lecture_id,
        pdf_path=pdf_path,
        extracted_dir=str(lecture_folder),
        manifest_path=str(manifest_path),
        notes_path=notes_path,
        pages_dir=str(lecture_folder / "pages"),
        embedded_dir=str(lecture_folder / "embedded"),
        total_pages=total_pages,
        total_embedded_images=total_embedded,
    )


def build_index() -> tuple[list[LectureEntry], dict[str, Any]]:
    lecture_folders = [
        p for p in EXTRACTED_DIR.iterdir() if p.is_dir() and p.name.startswith("Lecture_")
    ]
    entries = sorted((_build_entry(p) for p in lecture_folders), key=lambda e: e.lecture_number)

    now = datetime.now(timezone.utc).isoformat()
    index: dict[str, Any] = {
        "generated_at_utc": now,
        "root": str(ROOT),
        "source_pdfs_dir": str(LECTURE_SLIDE_DIR),
        "extracted_dir": str(EXTRACTED_DIR),
        "lectures": [
            {
                "lecture_number": e.lecture_number,
                "lecture_id": e.lecture_id,
                "pdf_path": e.pdf_path,
                "extracted_dir": e.extracted_dir,
                "manifest_path": e.manifest_path,
                "notes_path": e.notes_path,
                "pages_dir": e.pages_dir,
                "embedded_dir": e.embedded_dir,
                "total_pages": e.total_pages,
                "total_embedded_images": e.total_embedded_images,
            }
            for e in entries
        ],
    }
    return entries, index


def write_index_files(entries: list[LectureEntry], index: dict[str, Any]) -> None:
    index_json_path = EXTRACTED_DIR / "index.json"
    index_md_path = EXTRACTED_DIR / "index.md"

    index_json_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Human-friendly summary
    lines: list[str] = []
    lines.append("# Extracted Lecture Index")
    lines.append("")
    lines.append(f"- Generated (UTC): `{index['generated_at_utc']}`")
    lines.append(f"- Source PDFs: `{index['source_pdfs_dir']}`")
    lines.append(f"- Extracted artifacts: `{index['extracted_dir']}`")
    lines.append("")
    lines.append("| Lecture | Slides | Embedded images | Extracted dir | Notes | Manifest |")
    lines.append("|---:|---:|---:|---|---|---|")
    for e in entries:
        lines.append(
            f"| {e.lecture_number} | {e.total_pages} | {e.total_embedded_images} | `{e.extracted_dir}` | `{e.notes_path}` | `{e.manifest_path}` |"
        )
    lines.append("")
    index_md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not EXTRACTED_DIR.exists():
        raise SystemExit(f"Missing extracted dir: {EXTRACTED_DIR}")

    entries, index = build_index()
    write_index_files(entries, index)

    print(f"Wrote: {EXTRACTED_DIR / 'index.json'}")
    print(f"Wrote: {EXTRACTED_DIR / 'index.md'}")


if __name__ == "__main__":
    main()


