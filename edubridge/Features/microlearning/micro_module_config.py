# microlearning/micro_module_config.py

MICRO_MODULES = {

    # -------- Cluster A --------
    "student_absenteeism": {
        "module_id": "MM_A_01",
        "title": "Improving Student Attendance",
        "duration_minutes": 10,
        "objectives": [
            "Understand causes of absenteeism",
            "Apply classroom-level attendance strategies"
        ]
    },

    "parent_engagement": {
        "module_id": "MM_A_02",
        "title": "Strengthening Parent Involvement",
        "duration_minutes": 8,
        "objectives": [
            "Improve parent–teacher communication",
            "Increase parental participation"
        ]
    },

    "classroom_discipline": {
        "module_id": "MM_A_03",
        "title": "Managing Classroom Discipline",
        "duration_minutes": 12,
        "objectives": [
            "Handle disruptive behavior",
            "Maintain positive classroom climate"
        ]
    },

    # -------- Cluster B --------
    "advanced_teaching_materials": {
        "module_id": "MM_B_01",
        "title": "Using Advanced Teaching–Learning Materials",
        "duration_minutes": 15,
        "objectives": [
            "Design low-cost TLMs",
            "Enhance conceptual understanding"
        ]
    },

    "experiential_science_teaching": {
        "module_id": "MM_B_02",
        "title": "Experiential Science Teaching",
        "duration_minutes": 12,
        "objectives": [
            "Plan hands-on experiments",
            "Promote inquiry-based learning"
        ]
    },

    # -------- Cluster C --------
    "language_barrier": {
        "module_id": "MM_C_01",
        "title": "Addressing Language Barriers",
        "duration_minutes": 10,
        "objectives": [
            "Use mother tongue strategically",
            "Support language transition"
        ]
    },

    "multilingual_classroom": {
        "module_id": "MM_C_02",
        "title": "Teaching in Multilingual Classrooms",
        "duration_minutes": 14,
        "objectives": [
            "Manage multiple languages",
            "Improve comprehension"
        ]
    }
}

# Fallback module (never fails)
DEFAULT_MICRO_MODULE = {
    "module_id": "MM_GEN_01",
    "title": "Reflective Teaching Practices",
    "duration_minutes": 7,
    "objectives": [
        "Reflect on classroom challenges",
        "Plan small improvements"
    ]
}
