import numpy as np
image = np.array([
    [50, 100],
    [150, 200]
])

# Increase brightness
bright = image + 50
print("Brightness Increased:\n", bright)

# Decrease brightness
dark = image - 30
print("Brightness Decreased:\n", dark)

# Normalize
normalized = image / 255
print("Normalized:\n", normalized)