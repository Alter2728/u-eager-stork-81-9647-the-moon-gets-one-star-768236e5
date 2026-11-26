"""Revision note: replaced the generic brightness complaint with Moon-specific grievances (missing cheese, howling wolves, tides) and ended on the sharper punchline that its one star is for stealing sunlight smugly, which reads more like a real petty review."""

import os

TEXT = "★☆☆☆☆ No cheese, wolves won't shut up, tides keep moving my beach. One star for stealing sunlight smugly."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT and "\r" not in TEXT
assert 1 <= len(TEXT) <= 120

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
