"""
Test for Task 4: Micro-Learning Generator
Run from project root:
python -m tests.test_microlearning
"""

from feedback.policy_loader import PolicyLoader
from microlearning.module_generator import MicroLearningGenerator

PDF_PATHS = [
    "data/NEP_Final_English_0.pdf",
    "data/Guidelines50HoursCpd.pdf",
    "data/background_note_teacher_education.pdf",
    "data/EmpoweringEducatorsTeacherTrainingandProfessionalDevelopmentinNEP2020India_e1xn0wSl.pdf"
]

if __name__ == "__main__":
    loader = PolicyLoader(PDF_PATHS)
    documents = loader.load_documents()

    generator = MicroLearningGenerator(
        documents=documents,
        use_genai=True   # set False if no API key
    )

    result = generator.generate_module(cluster="A")

print("\n===== MICRO-LEARNING MODULE =====\n")

if "module" in result:
    print(result["module"])
else:
    print("Module not generated.")
    print("Reason:", result.get("message"))

print("\n===== SOURCES =====")

if "sources" in result:
    for src in result["sources"]:
        print(src)
else:
    print("No sources available (insufficient policy match).")

generator = MicroLearningGenerator(
    documents=documents,
    use_genai=False   # 🔥 IMPORTANT
)
