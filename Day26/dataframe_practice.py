import pandas as pd

# 1. Create DataFrame using dictionary
data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# 2. Print DataFrame
print(df)

# 3. Add one more column
df["Grade"] = ["A", "A+", "B"]
print(df)