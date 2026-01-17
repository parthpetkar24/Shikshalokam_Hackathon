EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K_KEYWORDS = 5


# Canonical Issue Definitions
CANONICAL_ISSUES = {

    # Cluster A: Student Engagement
    "classroom discipline": {
        "cluster": "A",
        "variants": [
            "classroom discipline",
            "student discipline",
            "student behavior",
            "misbehavior",
            "class control",
            "classroom management",
            "behavior issue"
        ]
    },

    "student absenteeism": {
        "cluster": "A",
        "variants": [
            "student absenteeism",
            "absenteeism",
            "student absence",
            "irregular attendance",
            "low attendance",
            "missing classes",
            "students not attending"
        ]
    },

    "parent engagement": {
        "cluster": "A",
        "variants": [
            "parent engagement",
            "parent involvement",
            "parent cooperation",
            "parents not attending",
            "lack of parental support",
            "parent meetings"
        ]
    },

    # Cluster B: Advanced Academics
    "advanced teaching materials": {
        "cluster": "B",
        "variants": [
            "advanced tlm",
            "teaching learning materials",
            "science tlm",
            "learning resources",
            "lab materials",
            "science models"
        ]
    },

    "experiential science teaching": {
        "cluster": "B",
        "variants": [
            "science experiments",
            "hands-on learning",
            "practical science",
            "activity based science",
            "experiential learning"
        ]
    },

    "higher order learning": {
        "cluster": "B",
        "variants": [
            "critical thinking",
            "problem solving",
            "higher order thinking",
            "conceptual understanding"
        ]
    },

    # Cluster C: Language & Context
    "language barrier": {
        "cluster": "C",
        "variants": [
            "language barrier",
            "medium of instruction",
            "language issue",
            "students not understanding language",
            "translation problem"
        ]
    },

    "local context teaching": {
        "cluster": "C",
        "variants": [
            "local context",
            "tribal context",
            "cultural relevance",
            "local examples",
            "contextual teaching"
        ]
    },

    "multilingual classroom": {
        "cluster": "C",
        "variants": [
            "multilingual classroom",
            "multiple languages",
            "different languages",
            "local dialect",
            "mother tongue"
        ]
    }
}

CLUSTER_METADATA = {
    "A": {
        "name": "Student Engagement & Behaviour",
        "description": "Issues related to attendance, discipline, and parental involvement"
    },
    "B": {
        "name": "Advanced Academics & Pedagogy",
        "description": "Issues related to higher-order learning and advanced teaching resources"
    },
    "C": {
        "name": "Language & Local Context",
        "description": "Issues related to language barriers and contextual teaching"
    }
}
