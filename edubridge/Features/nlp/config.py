EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# nlp/config.py

CLUSTER_METADATA = {
    "A": {
        "name": "Student Engagement & Attendance",
        "description": (
            "Issues related to student absenteeism, classroom discipline, "
            "and lack of parental engagement that affect regular participation "
            "and classroom stability."
        ),
        "focus_areas": [
            "Attendance improvement",
            "Classroom management",
            "Parent–teacher collaboration"
        ]
    },

    "B": {
        "name": "Advanced Pedagogy & Learning Resources",
        "description": (
            "Issues related to availability and use of advanced teaching-learning "
            "materials, experiential science education, and meeting the needs "
            "of high-performing or fast-learning students."
        ),
        "focus_areas": [
            "Experiential learning",
            "Teaching-learning materials (TLMs)",
            "Higher-order and advanced learning"
        ]
    },

    "C": {
        "name": "Language & Contextual Barriers",
        "description": (
            "Issues arising from language barriers, multilingual classrooms, "
            "and lack of locally relevant or culturally contextualized teaching methods."
        ),
        "focus_areas": [
            "Mother tongue / multilingual instruction",
            "Local and cultural context integration",
            "Inclusive classroom communication"
        ]
    }
}


CANONICAL_ISSUES = {

    # -------- Cluster A --------
    "student absenteeism": {
        "key": "student_absenteeism",
        "cluster": "A",
        "variants": [
            "absent", "absence", "absentee", "absenteeism",
            "students absent", "student absent",
            "not attending", "not coming",
            "missing class", "missing classes",
            "low attendance", "poor attendance",
            "irregular attendance",
            "students not coming", "children absent",
            "kids absent", "no attendance",
            "attendance low",
            "dropout", "drop out", "dropouts"
        ]
    },

    "classroom discipline": {
        "key": "classroom_discipline",
        "cluster": "A",
        "variants": [
            "discipline", "indiscipline",
            "misbehavior", "misbehaviour",
            "behavior issue", "behaviour issue",
            "students misbehave", "students noisy",
            "no discipline", "class control",
            "classroom control",
            "students not listening",
            "students out of control"
        ]
    },

    "parent engagement": {
        "key": "parent_engagement",
        "cluster": "A",
        "variants": [
            "parent", "parents",
            "parents not coming",
            "parent issue", "parent problem",
            "no parent support",
            "parents not supportive",
            "no parental support",
            "no parent involvement",
            "parent meeting",
            "parents not attending"
        ]
    },

    # -------- Cluster B --------
    "advanced teaching materials": {
        "key": "advanced_teaching_materials",
        "cluster": "B",
        "variants": [
            "advanced", "advanced tlm",
            "no tlm", "need tlm",
            "learning material",
            "teaching material",
            "no teaching material",
            "no learning material",
            "resources", "no resources",
            "lack of resources",
            "study material"
        ]
    },

    "experiential science teaching": {
        "key": "experiential_science_teaching",
        "cluster": "B",
        "variants": [
            "science", "science practical",
            "no practical", "no lab",
            "laboratory", "lab issue",
            "lab problem",
            "science experiment",
            "no experiment",
            "hands on", "hands-on",
            "activity based",
            "practical science"
        ]
    },

    "higher order learning": {
        "key": "higher_order_learning",
        "cluster": "B",
        "variants": [
            "advanced students",
            "bright students",
            "fast learners",
            "gifted students",
            "high performing",
            "students bored",
            "students finish early",
            "need higher level",
            "need advanced content"
        ]
    },

    # -------- Cluster C --------
    "language barrier": {
        "key": "language_barrier",
        "cluster": "C",
        "variants": [
            "language", "language issue",
            "language problem",
            "language barrier",
            "medium", "medium issue",
            "medium of instruction",
            "students not understanding",
            "children not understanding",
            "cannot understand",
            "english problem",
            "hindi problem"
        ]
    },

    "local context teaching": {
        "key": "local_context_teaching",
        "cluster": "C",
        "variants": [
            "tribal", "tribal area",
            "tribal students",
            "local context",
            "local example",
            "no local example",
            "context", "contextual",
            "contextual teaching",
            "cultural issue",
            "cultural problem"
        ]
    },

    "multilingual classroom": {
        "key": "multilingual_classroom",
        "cluster": "C",
        "variants": [
            "multilingual",
            "many languages",
            "multiple languages",
            "different languages",
            "local language",
            "mother tongue",
            "dialect",
            "local dialect",
            "students speak different language"
        ]
    }
}
