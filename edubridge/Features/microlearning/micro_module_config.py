from django.conf import settings
from pathlib import Path

DATA_DIR = Path(settings.DATA_DIR)

MICRO_MODULE_POLICY_MAP = {

    "cpd_overview": {
        "title": "Understanding 50 Hours CPD Framework",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_intent": (
            "Teachers must complete 50 hours of continuous professional development "
            "every year through structured and meaningful learning activities."
        ),
        "classroom_focus": "planning professional learning"
    },

    "cpd_peer_learning": {
        "title": "Peer Learning and Professional Collaboration",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_intent": (
            "Teachers are encouraged to learn collaboratively through peer discussions, "
            "shared reflection, and communities of practice."
        ),
        "classroom_focus": "collaborative teaching improvement"
    },

    "cpd_inclusive_practices": {
        "title": "Inclusive Teaching Practices as CPD",
        "pdf": DATA_DIR / "Guidelines50HoursCpd.pdf",
        "policy_intent": (
            "CPD includes training on inclusive practices to support diverse and "
            "disadvantaged learners in classrooms."
        ),
        "classroom_focus": "inclusive classroom strategies"
    },

    "experiential_pedagogy": {
        "title": "Experiential Pedagogy in Schools",
        "pdf": DATA_DIR / "NEP_Final_English_0.pdf",
        "policy_intent": (
            "Teaching should focus on experiential, activity-based, and competency-based "
            "learning rather than rote methods."
        ),
        "classroom_focus": "activity-based learning"
    }
}
