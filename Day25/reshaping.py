import numpy as np
arr = np.arange(12)

# 1D to 2D
reshaped = arr.reshape(3, 4)
print(reshaped)

# 2D to 1D
flat = reshaped.flatten()
print(flat)

# Create 3D dataset
data3d = np.arange(24).reshape(2, 3, 4)
print(data3d)