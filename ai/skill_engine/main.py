from extractor import extract_skills
from matcher import match_skills
from scorer import calculate_readiness
from role_mapper import ROLE_SKILLS
from utils import print_section


def run_skill_analysis():

    print_section("PrepAI Skill Intelligence Engine")

    skills_input = input(
        "Enter your skills (comma separated): "
    )

    user_skills = extract_skills(skills_input)

    print("\nAvailable Roles:\n")

    for role in ROLE_SKILLS.keys():
        print("-", role)

    target_role = input(
        "\nEnter target role exactly: "
    )

    result = match_skills(
        user_skills,
        target_role
    )

    matched = result["matched"]
    missing = result["missing"]
    extra = result["extra"]
    required = result["required"]

    readiness_score = calculate_readiness(
        len(matched),
        len(required)
    )

    print_section("ANALYSIS RESULT")

    print("\n✅ Matched Skills:")
    for skill in matched:
        print("-", skill)

    print("\n❌ Missing Skills:")
    for skill in missing:
        print("-", skill)

    print("\n⭐ Extra Skills:")
    for skill in extra:
        print("-", skill)

    print(f"\n🎯 Readiness Score: {readiness_score}%")


if __name__ == "__main__":
    run_skill_analysis()