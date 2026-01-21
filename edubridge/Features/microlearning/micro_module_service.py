from pathlib import Path
from django.conf import settings
from Features.microlearning.module_generator import ModuleGenerator

PDF_MAP = {
    "Continuous Professional Development (CPD)": settings.DATA_DIR / "Guidelines50HoursCpd.pdf",
    "Pedagogical Shift (NEP 2020)": settings.DATA_DIR / "NEP_Final_English_0.pdf",
    "Inclusive Classrooms": settings.DATA_DIR / "background_note_teacher_education.pdf",
    "Student Engagement": settings.DATA_DIR / "NEP_Final_English_0.pdf",
}


def generate_micro_module(topic: str):
    pdf_path = PDF_MAP.get(topic)
    if not pdf_path:
        raise ValueError("Invalid topic")

    generator = ModuleGenerator(pdf_path)
    return generator.generate()
