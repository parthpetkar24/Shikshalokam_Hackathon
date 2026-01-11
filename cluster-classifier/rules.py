def metadata_rules(metadata: dict):
    """
    metadata example:
    {
        "school_type": "tribal",
        "subject": "science",
        "language": "local",
        "infrastructure": "poor"
    }
    """
    rules = []

    if metadata.get("school_type") == "tribal":
        rules.append({"cluster": "C", "weight": 0.4, "reason": "tribal_school"})

    if metadata.get("subject") == "science" and metadata.get("infrastructure") == "poor":
        rules.append({"cluster": "B", "weight": 0.3, "reason": "science_no_lab"})

    if metadata.get("language") != "state_language":
        rules.append({"cluster": "C", "weight": 0.3, "reason": "language_mismatch"})

    return rules
