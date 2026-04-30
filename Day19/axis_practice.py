import numpy as np
arr = np.array([[1, 2],
                [3, 4]])

print("Column-wise sum:", np.sum(arr, axis=0))
print("Row-wise sum:", np.sum(arr, axis=1))