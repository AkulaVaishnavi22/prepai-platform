import pandas as pd


def load_skill_database():
    df = pd.read_csv("skills.csv")
    return df["skill_name"].dropna().tolist()


def parse_user_skills(skill_text):
    skills = [skill.strip() for skill in skill_text.split(",")]
    return [s for s in skills if s]


def normalize_skills(user_skills):
    db_skills = load_skill_database()

    normalized = []

    for user_skill in user_skills:
        for db_skill in db_skills:
            if user_skill.lower() == db_skill.lower():
                normalized.append(db_skill)

    return list(set(normalized))