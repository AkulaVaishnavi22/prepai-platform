def normalize_text(text):

    return text.strip().lower()


def extract_skills(skill_input):

    skills = [
        normalize_text(skill)
        for skill in skill_input.split(",")
    ]

    unique_skills = list(set(skills))

    return unique_skills