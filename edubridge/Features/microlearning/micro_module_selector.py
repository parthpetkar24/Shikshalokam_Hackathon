from Features.microlearning.micro_module_config import (
    MICRO_MODULE_POLICY_MAP,
    DEFAULT_MICRO_MODULE
)
from Features.microlearning.module_generator import ModuleGenerator

class MicroModuleSelector:
    def select(self, topic_key: str):
        config = MICRO_MODULE_POLICY_MAP.get(topic_key)
        if not config:
            return DEFAULT_MICRO_MODULE

        generator = ModuleGenerator(
            pdf_path=config["pdf"],
            policy_intent=config.get("policy_intent", "")
        )
        return generator.generate()
