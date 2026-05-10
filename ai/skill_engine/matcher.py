from role_mapper import ROLE_SKILLS


def match_skills(user_skills, target_role):

    # Normalize target role
    target_role = target_role.strip().lower()

    # Find matching role
    selected_role = None

    for role in ROLE_SKILLS.keys():

        if role.lower() == target_role:
            selected_role = role
            break

    if not selected_role:
        return {
            "matched": [],
            "missing": [],
            "extra": user_skills,
            "required": []
        }

    required_skills = [
        skill.lower()
        for skill in ROLE_SKILLS[selected_role]
    ]

    matched = []
    missing = []
    extra = []

    for skill in required_skills:

        if skill in user_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    for skill in user_skills:

        if skill not in required_skills:
            extra.append(skill)

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra,
        "required": required_skills
    }