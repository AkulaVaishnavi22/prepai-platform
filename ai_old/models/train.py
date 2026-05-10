from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

# Load data
df = pd.read_csv("dataset.csv")

# Combine input
X = df["user_skills"] + " " + df["job_skills"]
y = df["score"]

# Convert text → numbers
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_vec, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model trained and saved!")