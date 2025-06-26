import random, json
with open("test_data/all_journal_behaviors.txt") as f:
    behaviors = [l.strip() for l in f if l.strip()]
sample = random.sample(behaviors, 10)
def fuzzy(b): return {"behavior": b, "partial": b[:4], "typo": b[:-1] + "z", "synonym": "ALT_" + b.lower()}
with open("test_data/dataset_for_SQA_15092.json", "w") as f: json.dump([fuzzy(b) for b in sample], f, indent=2)
