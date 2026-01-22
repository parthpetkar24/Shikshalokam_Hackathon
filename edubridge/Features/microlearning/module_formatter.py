class MicroModuleFormatter:
    @staticmethod
    def format(module: dict) -> dict:
        return {
            "CPD Micro-Learning Module": module["module_title"],
            "Source Document": module["policy_source"],
            "Learning Objectives": module["learning_objectives"],
            "Policy Summary": module["summary"],
            "Estimated Duration": module["duration"]
        }
