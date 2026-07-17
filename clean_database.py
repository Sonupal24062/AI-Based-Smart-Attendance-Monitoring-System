import pandas as pd

database = "db.xls"

df = pd.read_excel(database)

# Remove empty rows
df = df.dropna(subset=["Name"])

# Remove wrong entry
df = df[df["Name"] != "python3.13 main.py"]

# Reset serial numbers
df["SN"] = range(1, len(df)+1)

# Save clean database
df.to_excel(
    "db_clean.xlsx",
    index=False
)

print("Database Cleaned Successfully")