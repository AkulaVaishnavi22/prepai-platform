import json

from resource_mapper import get_resources
from practice_mapper import get_practice


with open("role_skills.json", "r") as f:
    ROLE_SKILLS = json.load(f)

with open("skill_graph.json", "r") as f:
    SKILL_GRAPH = json.load(f)


def generate_roadmap(user_skills, target_role):

    target_role = target_role.strip().lower()

    selected_role = None

    for role in ROLE_SKILLS.keys():

        if role.lower() == target_role:
            selected_role = role
            break

    if not selected_role:
        return []

    required_skills = ROLE_SKILLS[selected_role]

    missing_skills = []

    for skill in required_skills:

        if skill not in user_skills:
            missing_skills.append(skill)

    roadmap = []

    visited = set()

    def add_skill(skill):

        if skill in visited:
            return

        prerequisites = SKILL_GRAPH.get(skill, [])

        for pre in prerequisites:
            add_skill(pre)

        visited.add(skill)

        roadmap.append({
            "skill": skill,
            "resources": get_resources(skill),
            "practice": get_practice(skill)
        })

    for skill in missing_skills:
        add_skill(skill)

    return roadmap