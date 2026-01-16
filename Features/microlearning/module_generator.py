from feedback.policy_retriever import PolicyRetriever
from microlearning.genai_module_formatter import GenAIModuleFormatter
from microlearning.module_templates import MICRO_MODULE_STRUCTURE


class MicroLearningGenerator:
    def __init__(self, documents, use_genai=True):
        self.retriever = PolicyRetriever(documents)
        self.use_genai = use_genai
        self.formatter = GenAIModuleFormatter() if use_genai else None

    def generate_module(self, cluster: str):
        # Step 1: Retrieve relevant policy chunks
        policy_chunks = self.retriever.retrieve(cluster, top_k=3)

        if not policy_chunks:
            return {
                "message": "No sufficient policy content found to generate module."
            }

        # Step 2: Combine policy text
        combined_policy_text = "\n\n".join(
            f"(Page {item['page']}): {item['text']}"
            for item in policy_chunks
        )

        # Step 3: Generate module
        if self.use_genai and self.formatter:
            module = self.formatter.format_module(
             MICRO_MODULE_STRUCTURE + "\n\n" + combined_policy_text
            )
        else:
            module = (
                "MICRO-LEARNING MODULE (OFFLINE MODE)\n\n"
                + combined_policy_text
            )


        return {
            "cluster": cluster,
            "module": module,
            "sources": [
                {"pdf": item["source"], "page": item["page"]}
                for item in policy_chunks
            ]
        }
