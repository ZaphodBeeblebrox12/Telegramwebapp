#!/usr/bin/env python3
"""Rebuild small campaign artwork assets from their checked-in base64 source."""
from __future__ import annotations

import base64
import binascii
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PARTS = sorted(ASSETS.glob("barrel-run-expedition.webp.b64.part*"))
OUTPUT = ASSETS / "barrel-run-expedition.webp"


def main() -> None:
    if not PARTS:
        raise SystemExit("Campaign artwork base64 parts not found in assets/")
    encoded = "".join("".join(part.read_text(encoding="ascii").split()) for part in PARTS)
    try:
        content = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise SystemExit(f"Campaign artwork source is invalid: {exc}") from exc
    if not content.startswith(b"RIFF") or content[8:12] != b"WEBP":
        raise SystemExit("Campaign artwork payload is not a valid WebP file")
    OUTPUT.write_bytes(content)
    print(f"Prepared {OUTPUT.relative_to(ROOT)} ({len(content):,} bytes)")


if __name__ == "__main__":
    main()
