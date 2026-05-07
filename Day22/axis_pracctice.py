import numpy as np
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Row-wise Sum:", np.sum(arr2, axis=1))
print("Column-wise Sum:", np.sum(arr2, axis=0))

print("Row-wise Mean:", np.mean(arr2, axis=1))
print("Column-wise Mean:", np.mean(arr2, axis=0))