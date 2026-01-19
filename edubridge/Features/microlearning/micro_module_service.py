from pathlib import Path
from Features.microlearning.module_generator import ModuleGenerator

NEP_PDF = Path("data/NEP_Final_English_0.pdf")
CPD_PDF = Path("data/Guidelines50HoursCpd.pdf")
TEACHER_EDU_PDF = Path("data/background_note_teacher_education.pdf")

PDF_MAP = {
    "Continuous Professional Development (CPD)": CPD_PDF,
    "Pedagogical Shift (NEP 2020)": NEP_PDF,
    "Inclusive Classrooms": TEACHER_EDU_PDF,
    "Student Engagement": NEP_PDF
}


def generate_micro_module(topic: str):
    pdf_path = PDF_MAP.get(topic)
    if not pdf_path:
        raise ValueError("Invalid topic")

    generator = ModuleGenerator(pdf_path)
    return generator.generate()
