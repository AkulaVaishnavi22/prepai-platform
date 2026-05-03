def compare_skills(user_skills, jd_skills):
    user_set = set(skill.lower() for skill in user_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    matched = list(user_set & jd_set)
    missing = list(jd_set - user_set)
    extra = list(user_set - jd_set)

    score = 0
    if len(jd_set) > 0:
        score = int((len(matched) / len(jd_set)) * 100)

    return matched, missing, extra, score