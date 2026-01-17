# tests/test_microlearning.py

from microlearning.module_generator import ModuleGenerator

def test_microlearning_cluster_A():
    print("\n==============================")
    print("Testing Microlearning Generator (Cluster A)")
    print("==============================")

    generator = ModuleGenerator(use_genai=False)  # 🔥 IMPORTANT
    result = generator.generate_module(cluster="A")

    print("\n--- GENERATED MODULE ---")
    for key, value in result.items():
        print(f"\n{key.upper()}:\n{value}")

    assert result is not None
    assert "content" in result

if __name__ == "__main__":
    test_microlearning_cluster_A()