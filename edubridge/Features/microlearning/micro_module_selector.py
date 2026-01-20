# microlearning/micro_module_selector.py

from microlearning.micro_module_config import (
    MICRO_MODULES,
    DEFAULT_MICRO_MODULE
)

CONFIDENCE_THRESHOLD = 0.5


class MicroModuleSelector:

    def select(self, cluster_result: dict):
        """
        cluster_result = output of ClusterClassifier (Fix 2)
        """

        if (
            cluster_result["cluster_id"] == "Insufficient data"
            or cluster_result["confidence"] < CONFIDENCE_THRESHOLD
        ):
            return DEFAULT_MICRO_MODULE

        issues = cluster_result.get("issues", [])

        # Pick first matching issue module
        for issue in issues:
            key = issue.get("key")
            if key in MICRO_MODULES:
                return MICRO_MODULES[key]

        # Safe fallback
        return DEFAULT_MICRO_MODULE
