from classifier import ClusterClassifier

if __name__ == "__main__":
    classifier = ClusterClassifier()

    test_cases = [
        {
            "text": "We need advanced experiments and lab activities for science students",
            "metadata": {
                "school_type": "urban",
                "subject": "science",
                "language": "state_language",
                "infrastructure": "poor"
            }
        },
        {
            "text": "Students are irregular in attendance and parents are not supportive",
            "metadata": {
                "school_type": "rural",
                "subject": "math",
                "language": "state_language",
                "infrastructure": "basic"
            }
        },
        
        {
            "text": "Students struggle because the language and dialect are different",
            "metadata": {
                "school_type": "tribal",
                "subject": "primary",
                "language": "local",
                "infrastructure": "basic"
            }
        }
    ]

    for i, case in enumerate(test_cases, 1):
        result = classifier.classify(case["text"], case["metadata"])
        print(f"\nTest Case {i}")
        print("Result:", result)
