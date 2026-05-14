import pandas as pd

data = pd.Series([10, 20, 30, 40])
print(data)

data2 = pd.Series([85, 90, 78], index=["Math", "Science", "English"])
print(data2)
print(data2["Math"])