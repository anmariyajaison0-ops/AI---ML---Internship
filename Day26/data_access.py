import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# 1. Access single column
print(df["Name"])

# 2. Access multiple columns
print(df[["Name", "Marks"]])

# 3. Print specific row
print(df.loc[0])