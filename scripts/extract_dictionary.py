import re
import json
from pathlib import Path

# Path to your encyclopedia text file in the repo
file_path = Path("The Encyclopedia of Jewish Myth, Magic and Mysticism - 2nd Edition (2016).txt")

# Read file
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Find start (first entry) and end (last entry) of A–Z section
start_index = content.find("Aaron:")
end_index = content.rfind("Zuz")  # last entry under Z

a_to_z_content = content[start_index:end_index].strip()

# Split entries - looks for lines like "Word:"
entries = re.split(r"\n(?=[A-Z][A-Za-z\s\-\(\)]+:)", a_to_z_content)

dictionary = {}
for entry in entries:
    if ":" in entry:
        term, definition = entry.split(":", 1)
        dictionary[term.strip()] = definition.strip()

# Save JSON
output_path = Path("jewish_magic_dictionary.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(dictionary, f, indent=2, ensure_ascii=False)

print(f"✅ Extracted {len(dictionary)} entries")
print(f"📂 Saved to {output_path}")
