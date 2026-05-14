import numpy as np
arr = np.array([10, 25, 30, 5, 60, 80])

# Filter > 50
filtered = arr[arr > 50]
print("Filtered:", filtered)

# Replace low values (<20)
arr[arr < 20] = 0
print("Updated:", arr)

# Count filtered values
print("Count:", len(filtered))