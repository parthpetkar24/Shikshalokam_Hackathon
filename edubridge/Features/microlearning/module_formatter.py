class MicroModuleFormatter:
    @staticmethod
    def format(summary: str, source: str) -> dict:
        return {
            "module_title": "CPD Micro-Learning Module",
            "policy_source": source,
            "policy_summary": summary,
            "duration": "10–15 minutes"
        }
