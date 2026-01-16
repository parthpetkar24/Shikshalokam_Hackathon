# microlearning/policy_loader.py

class PolicyLoader:
    """
    Loads policy text based on cluster
    (Later: PDF parsing, DB, vector store)
    """

    CLUSTER_POLICIES = {
        "A": """
        Cluster A focuses on student absenteeism.
        Teachers need classroom management tools,
        parent engagement strategies, and behaviour tracking.
        NEP 2020 emphasizes community involvement and teacher autonomy.
        """,

        "B": """
        Cluster B has academically strong students.
        Teachers require advanced Teaching Learning Materials (TLMs),
        inquiry-based pedagogy, and higher-order thinking strategies.
        """,

        "C": """
        Cluster C operates in tribal and multilingual areas.
        Teachers need language contextualization,
        culturally relevant pedagogy, and flexible assessment.
        """
    }

    @classmethod
    def load_policy_text(cls, cluster: str) -> str:
        return cls.CLUSTER_POLICIES.get(
            cluster,
            "General NEP 2020 teacher professional development guidance."
        )
