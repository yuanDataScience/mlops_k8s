import pandas as pd

df = pd.read_csv("data.csv")

# Delete one row (drop row with A == 3)
df = df[df["A"] != 3]

df.to_csv("data.csv", index=False)
print(df)