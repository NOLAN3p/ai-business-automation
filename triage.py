import csv
import json
import sys

RULES = {"billing": ("invoice", "refund", "payment"), "technical": ("error", "login", "crash"), "onboarding": ("setup", "training", "start")}

def classify(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = set(text.lower().split())
    matches = [name for name, terms in RULES.items() if words.intersection(terms)]
    return {"queue": matches[0] if len(matches)==1 else "review", "requires_review": len(matches)!=1, "matched": matches}

def process(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["ticket_id","text"]:
            raise ValueError("Expected ticket_id,text header")
        seen = set()
        for row in reader:
            ticket = row["ticket_id"]
            if not ticket or ticket in seen or row["text"] is None or None in row:
                raise ValueError("Invalid or duplicate ticket")
            seen.add(ticket)
            yield {"ticket_id":ticket, **classify(row["text"])}

if __name__ == "__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python triage.py sample.csv")
    print(json.dumps(list(process(sys.argv[1])), indent=2))
