import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# 1. Extract sub-array
print(arr[1:4])  

# 2. Step slicing
print(arr[::2])  

# 3. 2D slicing
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr2[:, 1:3])  