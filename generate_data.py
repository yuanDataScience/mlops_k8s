import pandas as pd

df = pd.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "B": ["x", "y", "z", "w", "v"],
        "C": [0.1, 0.2, 0.3, 0.4, 0.5],
    }
)

df.to_csv("data.csv", index=False)
print(df)