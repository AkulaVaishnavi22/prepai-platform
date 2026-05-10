def generate_roadmap(missing_skills):
    roadmap = []

    day = 1

    for skill in missing_skills:
        roadmap.append(f"Day {day} - Learn {skill.title()}")
        day += 1

    return roadmap