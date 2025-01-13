import pandas as pd

# Load dataset from dataIn
df = pd.read_excel("../dataIn/employment_dataset_raw.xlsx", sheet_name="Sheet1")

# Rename columns for clarity
df.columns = [
    "Region",
    "Work_Accidents",
    "Libraries",
    "Avg_Salary",
    "Num_Employees",
    "Workforce",
    "Education_Units"
]

# Convert Workforce to numeric
df["Workforce"] = df["Workforce"].astype(str).str.replace(",", ".").astype(float)

# Save cleaned data to dataOut
df.to_csv("../dataOut/employment_data_cleaned.csv", index=False)
print("✅ Data cleaned and saved in dataOUT/")
