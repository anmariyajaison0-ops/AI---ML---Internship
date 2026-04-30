arr = np.array([1, 2, 3, 4, 5, 6])

# 1D → 2D
reshaped = arr.reshape(2, 3)
print(reshaped)

# 2D → 1D
flattened = reshaped.reshape(-1)
print(flattened)