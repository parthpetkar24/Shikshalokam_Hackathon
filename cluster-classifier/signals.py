import re

KEYWORD_SIGNALS = {
    "attendance_issue": {
        "keywords": ["absent", "attendance", "irregular", "dropout"],
        "cluster": "A",
        "weight": 0.4
    },
    "engagement_issue": {
        "keywords": ["engagement", "interest", "attention", "behavior"],
        "cluster": "A",
        "weight": 0.3
    },
    "advanced_learning": {
        "keywords": ["advanced", "experiment", "lab", "project", "olympiad"],
        "cluster": "B",
        "weight": 0.5
    },
    "resource_gap": {
        "keywords": ["no lab", "no material", "lack of resources"],
        "cluster": "B",
        "weight": 0.4
    },
    "language_barrier": {
        "keywords": ["language", "dialect", "tribal", "mother tongue"],
        "cluster": "C",
        "weight": 0.6
    }
}

def extract_keyword_signals(text: str):
    text = text.lower()
    signals = []

    for signal, data in KEYWORD_SIGNALS.items():
        for kw in data["keywords"]:
            if re.search(rf"\b{kw}\b", text):
                signals.append({
                    "signal": signal,
                    "cluster": data["cluster"],
                    "weight": data["weight"]
                })
                break

    return signals
