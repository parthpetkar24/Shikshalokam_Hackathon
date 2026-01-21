# microlearning/module_generator.py

from microlearning.genai_module_formatter import GenAIModuleFormatter
from microlearning.policy_loader import PolicyLoader

MICRO_MODULE_STRUCTURE = """
You are designing a microlearning module for teachers.
The module must be:
- Short (5–10 minutes)
- Practical
- Classroom ready
- Aligned with NEP 2020
"""

class ModuleGenerator:
    """
    Core Microlearning Generator
    """

    def __init__(self, use_genai=False):
        self.formatter = GenAIModuleFormatter(use_genai=use_genai)

    def generate_module(self, cluster: str):
        policy_text = PolicyLoader.load_policy_text(cluster)

        combined_text = (
            MICRO_MODULE_STRUCTURE
            + "\n\n"
            + f"TARGET CLUSTER: {cluster}\n\n"
            + policy_text
        )

        return self.formatter.format_module(combined_text)
