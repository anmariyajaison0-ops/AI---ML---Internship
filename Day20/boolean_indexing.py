import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# 1. Values > 25
print(arr[arr > 25])  

# 2. Values between range
print(arr[(arr > 20) & (arr < 50)])  

# 3. Replace values conditionally
arr[arr > 30] = 0
print(arr)