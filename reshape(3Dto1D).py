import numpy as np

# Create a 3D array with shape (2, 3, 4)
arr = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])

print("3D Array:\n", arr)
print("Shape:", arr.shape)
res=arr.reshape(-1)
print("Reshaped Array:\n", res)