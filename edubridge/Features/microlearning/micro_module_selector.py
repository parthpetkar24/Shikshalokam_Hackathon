from Features.microlearning.micro_module_config import MICRO_MODULE_POLICY_MAP
from Features.microlearning.module_generator import ModuleGenerator

class MicroModuleSelector:
    def select(self, topic_key: str):
        config = MICRO_MODULE_POLICY_MAP.get(topic_key)

        if not config:
            raise ValueError("Invalid micro-module topic")

        generator = ModuleGenerator(
            pdf_path=config["pdf"],
            policy_keywords=config["policy_keywords"],
            policy_intent=config["policy_intent"],
            title=config["title"]
        )

        return generator.generate()
