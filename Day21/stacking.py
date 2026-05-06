import numpy as np
a = np.array([1, 2])
b = np.array([3, 4])

# Vertical stack
print(np.vstack((a, b)))
# [[1 2]
#  [3 4]]

# Horizontal stack
print(np.hstack((a, b)))
# [1 2 3 4]