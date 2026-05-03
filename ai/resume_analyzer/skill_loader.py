import pandas as pd

def load_skills():
    df = pd.read_csv("data/skills.csv")
    return df["skill_name"].dropna().tolist()