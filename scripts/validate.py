#!/usr/bin/env python3
"""Validate article index and linked HTML files without external dependencies."""
import json
from pathlib import Path
from datetime import date

root = Path(__file__).resolve().parent.parent
errors = []
index = root / "index.html"
data_file = root / "data" / "pages.json"
if not index.is_file():
    errors.append("Missing index.html")
try:
    entries = json.loads(data_file.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    entries = []
    errors.append(f"Cannot read pages.json: {exc}")
if not isinstance(entries, list):
    errors.append("pages.json must contain a JSON array")
    entries = []
seen = set()
for n, entry in enumerate(entries, 1):
    if not isinstance(entry, dict):
        errors.append(f"Entry {n}: must be an object")
        continue
    required = ("title", "category", "summary", "date", "url")
    for key in required:
        if not isinstance(entry.get(key), str) or not entry[key].strip():
            errors.append(f"Entry {n}: missing or invalid {key}")
    url = entry.get("url")
    if not isinstance(url, str):
        continue
    parts = Path(url).parts
    if (not url.startswith("pages/") or url.startswith("/") or
            ".." in parts or "\\" in url or "?" in url or "#" in url or
            not url.endswith(".html")):
        errors.append(f"Entry {n}: invalid article path {url}")
        continue
    if url in seen:
        errors.append(f"Entry {n}: duplicate URL {url}")
    seen.add(url)
    page = root / url
    if not page.is_file():
        errors.append(f"Entry {n}: missing file {url}")
    else:
        content = page.read_text(encoding="utf-8")
        if "../index.html" not in content:
            errors.append(f"Entry {n}: no return-home link in {url}")
    try:
        date.fromisoformat(entry.get("date", ""))
    except (ValueError, TypeError):
        errors.append(f"Entry {n}: invalid ISO date")
if errors:
    print("Validation failed:")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)
print(f"Validation passed: {len(entries)} article(s), all indexed paths exist.")
