import pandas as pd

# Create data
data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

# 1. First 5 rows
print(df.head())

# 2. Last rows
print(df.tail())

# 3. Info
print(df.info())