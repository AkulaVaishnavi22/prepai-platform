from extractor import parse_user_skills, normalize_skills
from matcher import compare_skills
from recommender import generate_roadmap


print("====== PrepAI Skill Analyzer ======")

user_input = input("Enter your known skills (comma separated): ")
jd_input = input("Enter required job skills (comma separated): ")


user_skills = parse_user_skills(user_input)
jd_skills = parse_user_skills(jd_input)


user_skills = normalize_skills(user_skills)
jd_skills = normalize_skills(jd_skills)


matched, missing, extra, score = compare_skills(user_skills, jd_skills)


roadmap = generate_roadmap(missing)


print("\n====== Analysis Result ======")
print("Your Skills:", user_skills)
print("Job Skills:", jd_skills)
print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Extra Skills:", extra)
print("Match Score:", str(score) + "%")


print("\n====== Suggested Roadmap ======")
for item in roadmap:
    print(item)