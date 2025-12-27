import pandas as pd

df = pd.read_csv("data/electronics.csv")

df["category"] = "phone"   # 👈 overwrite or create column

df.to_csv("data/electronics1.csv", index=False)
