from pybtex.database import parse_file
from pathlib import Path
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

bib = parse_file("export.bib")

output_dir = Path("content/publications")
output_dir.mkdir(parents=True, exist_ok=True)

for key, entry in bib.entries.items():
    title = entry.fields.get("title", "Untitled")
    year = entry.fields.get("year", "")
    journal = entry.fields.get("journal", entry.fields.get("booktitle", ""))
    doi = entry.fields.get("doi", "")
    abstract = entry.fields.get("abstract", "")

    authors = []
    for person in entry.persons.get("author", []):
        authors.append(" ".join(person.first_names + person.middle_names + person.last_names))

    slug = slugify(title)
    filepath = output_dir / f"{slug}.md"

    content = f"""---
title: "{title}"
authors:
"""
    for a in authors:
        content += f"  - {a}\n"

    content += f"""publication: "*{journal}*"
date: {year}-01-01
doi: "{doi}"
abstract: "{abstract[:500]}"
draft: false
---
"""

    filepath.write_text(content, encoding="utf-8")

print("Done.")