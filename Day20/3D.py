import numpy as np
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

# 1. Access layer
print(arr[0])  

# 2. Access row inside layer
print(arr[0][1])  

# 3. Access single element
print(arr[1, 0, 2])  