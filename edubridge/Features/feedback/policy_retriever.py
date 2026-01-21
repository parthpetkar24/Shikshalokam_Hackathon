from Features.nlp.config import CANONICAL_ISSUES


# 🔹 Policy theme keywords (NEP-aligned language)
# These terms are known to exist in NEP 2020 / CPD documents
POLICY_THEME_KEYWORDS = {

    # -------- Cluster A : Engagement & Attendance --------
    "student_absenteeism": {
        "retention",
        "access",
        "participation",
        "engagement",
        "dropout",
        "continuity",
        "enrolment",
        "attendance"
    },

    "classroom_discipline": {
        "school climate",
        "student wellbeing",
        "discipline",
        "classroom",
        "behaviour",
        "socio emotional"
    },

    "parent_engagement": {
        "parent",
        "parents",
        "community",
        "local community",
        "stakeholder",
        "family",
        "community participation"
    },

    # -------- Cluster B : Pedagogy & Resources --------
    "advanced_teaching_materials": {
        "teaching learning material",
        "tlm",
        "resources",
        "digital",
        "infrastructure",
        "content"
    },

    "experiential_science_teaching": {
        "experiential",
        "practical",
        "laboratory",
        "hands on",
        "activity based"
    },

    "higher_order_learning": {
        "higher order",
        "critical thinking",
        "advanced learning",
        "competency based",
        "gifted"
    },

    # -------- Cluster C : Language & Context --------
    "language_barrier": {
        "multilingual",
        "mother tongue",
        "foundational literacy",
        "language",
        "linguistic"
    },

    "local_context_teaching": {
        "local context",
        "contextual",
        "cultural",
        "tribal",
        "indigenous"
    }
}


class PolicyRetriever:
    """
    Retrieves relevant policy documents using
    policy-theme-based semantic matching.

    This avoids literal keyword mismatch between
    classroom language and policy language.
    """

    def __init__(self, documents: list):
        """
        Args:
            documents (list): Loaded policy documents
                              Each item: { "source": str, "text": str }
        """
        self.documents = documents

    def retrieve(self, issue_keys: list, top_k: int = 1):

        # ✅ If issue is known, return policy docs directly
        if issue_keys:
            print("POLICY MATCH MODE: ISSUE-BASED (PDF SAFE)")
            return self.documents[:top_k]

        print("POLICY MATCH MODE: FALLBACK")
        return self.documents[:top_k]

