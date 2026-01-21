from feedback.feedback_engine import FeedbackEngine


def test_feedback_for_cluster(cluster_code):
    print("\n==============================")
    print(f"Testing Feedback for Cluster {cluster_code}")
    print("==============================\n")

    feedback_engine = FeedbackEngine(use_genai=False)  
    # 🔼 set use_genai=True ONLY if OPENAI_API_KEY is set

    feedback_items = feedback_engine.generate_feedback(cluster_code)

    if not feedback_items:
        print("No feedback retrieved from policy documents.")
        return

    for idx, item in enumerate(feedback_items, start=1):
        print(f"\n--- Feedback Item {idx} ---")
        print("Feedback Text:")
        print(item["feedback"])
        print("\nSource PDF:")
        print(item["source_pdf"])
        print("Page Number:")
        print(item["page"])


if __name__ == "__main__":
    # ✅ Test with known clusters
    test_feedback_for_cluster("A")  # Student Engagement & Behaviour
    test_feedback_for_cluster("B")  # Advanced Academics & Pedagogy
    test_feedback_for_cluster("C")  # Language & Local Context
