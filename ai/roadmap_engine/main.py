from roadmap_generator import generate_roadmap


print("\n====== PrepAI Roadmap Engine ======\n")

skills_input = input(
    "Enter your skills (comma separated): "
)

user_skills = [
    skill.strip().lower()
    for skill in skills_input.split(",")
]

print("\nAvailable Roles:")
print("- Frontend Developer")
print("- Backend Developer")
print("- AI Engineer")
print("- Full Stack Developer")

target_role = input(
    "\nEnter target role: "
)

roadmap = generate_roadmap(
    user_skills,
    target_role
)

print("\n====== YOUR PERSONALIZED ROADMAP ======\n")

for index, item in enumerate(roadmap, start=1):

    print(f"{index}. Learn: {item['skill']}")

    print("\nResources:")

    for resource in item["resources"]:
        print("-", resource)

    print("\nPractice:")

    for practice in item["practice"]:
        print("-", practice)

    print("\n----------------------------")