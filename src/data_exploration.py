import pandas as pd

# Load the dataset
df = pd.read_csv("data/student_performance.csv")

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Dataset information
print("\n========== DATASET INFO ==========")
print(df.info())

# Statistical summary
print("\n========== SUMMARY ==========")
print(df.describe())

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Column names
print("\n========== COLUMNS ==========")
print(df.columns)