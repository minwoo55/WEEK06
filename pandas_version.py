import pandas as pd

df = pd.read_csv("scores.csv")

df["score"] = pd.to_numeric(df["score"], errors="coerce")

mean_scores = df.groupby("category")["score"].mean().round(2)

print(mean_scores)
