import pandas as pd

# Read CSV file
df = pd.read_csv(r"C:\Users\ANMARIYA\students_new.csv")

# Print full dataset
print("Full Dataset:")
print(df)

# Task 3: Column Selection
print("\nSingle Column:")
print(df["Name"])

print("\nMultiple Columns:")
print(df[["Name", "Marks"]])

print("\nSpecific Column Values:")
print(df["City"])

# Task 4: Row Selection
print("\nUsing loc:")
print(df.loc[0])

print("\nUsing iloc:")
print(df.iloc[1])

print("\nSlice Rows:")
print(df[0:2])

# Task 5: Filtering
print("\nMarks > 80:")
print(df[df["Marks"] > 80])

print("\nCity = Kochi:")
print(df[df["City"] == "Kochi"])

print("\nCombined Condition:")
print(df[(df["Marks"] > 80) & (df["City"] == "Kochi")])

# Bonus
print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nShape:")
print(df.shape)