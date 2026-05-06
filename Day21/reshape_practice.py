import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# 1D → 2D
print(arr.reshape(2, 3))
# Output:
# [[1 2 3]
#  [4 5 6]]

# 1D → 3D
print(arr.reshape(1, 2, 3))

# Invalid reshape
print(arr.reshape(3, 2))