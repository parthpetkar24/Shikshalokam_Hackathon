class PolicyFeedbackGenerator:
    def __init__(self, client):
        self.client = client

    def generate(self, issue, cluster, policy_docs):
        if not policy_docs:
            return (
                "The reported issue could not be mapped to sufficient policy context. "
                "Institutional review is required."
            )

        policy_context = "\n\n".join(
            f"Source: {doc['source']}\n{doc['text'][:1200]}"
            for doc in policy_docs
        )

        prompt = f"""
You are a senior academic expert from SCERT/DIET.

Teacher-reported issue:
"{issue}"

Identified issue cluster:
"{cluster}"

Relevant policy excerpts:
{policy_context}

Write professional institutional feedback that:
1. Diagnoses the issue using education policy language
2. Explains the systemic cause of the issue
3. Aligns explicitly with NEP 2020 and CPD intent
4. Prescribes actions at both teacher and DIET level
5. Uses a formal, authoritative tone

Avoid generic advice.
Avoid conversational language.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350
        )

        return response.choices[0].message.content.strip()
