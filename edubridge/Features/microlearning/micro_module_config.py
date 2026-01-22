# microlearning/micro_module_config.py

from django.conf import settings
from pathlib import Path

DATA_DIR = Path(settings.DATA_DIR)

MICRO_MODULE_POLICY_MAP = {


    # CPD CORE MODULES
    "cpd_overview": {
        "cluster": "Teacher Professional Development",
        "title": "Understanding 50 Hours CPD Framework",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "50 hours",
            "continuous professional development",
            "annual requirement",
            "teacher development"
        ],
        "policy_intent": (
            "The CPD framework mandates structured, continuous learning "
            "for teachers to improve pedagogical and professional competencies."
        ),
        "expected_duration_minutes": 8
    },

    "cpd_self_directed_learning": {
        "cluster": "Teacher Professional Development",
        "title": "Self-Directed Learning under CPD",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "self-directed",
            "自主 learning",
            "teacher initiative",
            "individual learning plan"
        ],
        "policy_intent": (
            "Teachers are encouraged to take ownership of their CPD "
            "through self-directed and interest-driven learning."
        ),
        "expected_duration_minutes": 10
    },

    "cpd_peer_learning": {
        "cluster": "Teacher Professional Development",
        "title": "Peer Learning and Professional Collaboration",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "peer learning",
            "collaborative learning",
            "communities of practice",
            "teacher collaboration"
        ],
        "policy_intent": (
            "CPD emphasizes collaborative and peer-based learning "
            "to promote collective professional growth."
        ),
        "expected_duration_minutes": 12
    },

    "cpd_reflective_practice": {
        "cluster": "Teacher Professional Development",
        "title": "Reflective Practice as CPD",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "reflective practice",
            "self-reflection",
            "professional growth"
        ],
        "policy_intent": (
            "Reflection on classroom experiences is recognized "
            "as a valid and essential CPD activity."
        ),
        "expected_duration_minutes": 8
    },

    "cpd_classroom_based_learning": {
        "cluster": "Teacher Professional Development",
        "title": "Classroom-Based Professional Learning",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "classroom based learning",
            "on-the-job learning",
            "practice based"
        ],
        "policy_intent": (
            "CPD acknowledges learning that occurs directly "
            "through classroom practice and experimentation."
        ),
        "expected_duration_minutes": 10
    },

    "cpd_action_research": {
        "cluster": "Teacher Professional Development",
        "title": "Action Research for Teachers",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "action research",
            "classroom research",
            "evidence based practice"
        ],
        "policy_intent": (
            "Teachers are encouraged to engage in small-scale "
            "action research to improve teaching practices."
        ),
        "expected_duration_minutes": 15
    },

    "cpd_digital_learning": {
        "cluster": "Teacher Professional Development",
        "title": "Digital and Online Learning for CPD",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "online learning",
            "digital platforms",
            "technology enabled CPD"
        ],
        "policy_intent": (
            "Digital platforms and online modules are recognized "
            "as valid modes for fulfilling CPD requirements."
        ),
        "expected_duration_minutes": 12
    },

    "cpd_assessment_literacy": {
        "cluster": "Teacher Professional Development",
        "title": "Assessment Literacy for Teachers",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "assessment",
            "student evaluation",
            "formative assessment"
        ],
        "policy_intent": (
            "Teachers must develop assessment literacy "
            "to support learner-centered evaluation practices."
        ),
        "expected_duration_minutes": 10
    },

    "cpd_inclusive_practices": {
        "cluster": "Teacher Professional Development",
        "title": "Inclusive Teaching Practices as CPD",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_keywords": [
            "inclusive education",
            "equity",
            "diverse learners"
        ],
        "policy_intent": (
            "CPD includes training on inclusive practices "
            "to support diverse and disadvantaged learners."
        ),
        "expected_duration_minutes": 12
    },

    # SUPPORTING NEP-ALIGNED MODULES (SECONDARY
    "language_in_classroom": {
        "cluster": "Inclusive Education",
        "title": "Using Mother Tongue in Classroom Instruction",
        "pdf": DATA_DIR / "NEP_Final_English_0.pdf",
        "policy_keywords": [
            "mother tongue",
            "home language",
            "multilingual classroom"
        ],
        "policy_intent": (
            "NEP 2020 promotes mother tongue-based instruction "
            "to improve comprehension in early grades."
        ),
        "expected_duration_minutes": 10
    },

    "experiential_pedagogy": {
        "cluster": "Pedagogical Practices",
        "title": "Experiential Pedagogy in Schools",
        "pdf": DATA_DIR / "NEP_Final_English_0.pdf",
        "policy_keywords": [
            "experiential learning",
            "competency based",
            "hands on"
        ],
        "policy_intent": (
            "NEP 2020 encourages experiential and competency-based pedagogy."
        ),
        "expected_duration_minutes": 12
    }
}


# SAFE FALLBACK
DEFAULT_MICRO_MODULE = {
    "module_title": "CPD Micro-Learning Module",
    "policy_source": "Guidelines50HoursCpd.pdf",
    "policy_summary": (
        "This micro-learning module is derived from official CPD guidelines. "
        "It supports reflective and continuous professional development aligned "
        "with national policy."
    ),
    "duration": "10–15 minutes"
}

