import pickle

# Load model
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def predict_score(user_skills, job_skills):
    text = user_skills + " " + job_skills
    X = vectorizer.transform([text])

    score = model.predict(X)[0]
    return int(score)