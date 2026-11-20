import json

for name in ("volume_previews", "scenario_examples"):
    with open(f"data/{name}.jsonl", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    print(f"{name}: {len(rows)} records")
    for r in rows[:2]:
        print(" -", r.get("title") or r.get("source_volume"))
