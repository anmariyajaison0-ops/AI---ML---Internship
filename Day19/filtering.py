import numpy as np
arr = np.array([10, 20, 30, 40, 15])

# Values > 20
print("Greater than 20:", arr[arr > 20])

# Even numbers
print("Even numbers:", arr[arr % 2 == 0])