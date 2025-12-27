import pandas as pd

# Absolute safest way to load CSV
DATA_PATH = "../data/electronics1.csv"

# Load CSV ONCE
df = pd.read_csv(DATA_PATH)

# Normalize brand column
if "brand" not in df.columns:
    raise Exception("Column 'brand' not found in CSV")

df["brand"] = df["brand"].astype(str).str.lower().str.strip()

def search_products(brand_key: str):
    brand_key = brand_key.lower().strip()

    # Debug print (IMPORTANT)
    print("SEARCH KEY:", brand_key)

    if brand_key == "":
        print("RETURNING ALL ROWS")
        return df.to_dict(orient="records")

    matched = df[df["brand"].str.contains(brand_key, na=False)]

    print("MATCH COUNT:", len(matched))
    return matched.to_dict(orient="records")
