import numpy as np
colors = ["red", "blue", "green"]

# 1. Pick random color
print(np.random.choice(colors))

# 2. Generate multiple choices
print(np.random.choice(colors, size=5))

# 3. Simulate random names
names = ["Anu", "Akhil", "Riya"]
print(np.random.choice(names, size=3))