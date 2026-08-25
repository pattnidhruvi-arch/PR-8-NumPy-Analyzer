import numpy as np

# PR-8: NumPy Analyzer
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original Array:\n", arr)

print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std Dev:", np.std(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Sum:", np.sum(arr))

# Reshape and Transpose
print("\nTranspose:\n", arr.T)
print("\nReshaped (1x9):\n", arr.reshape(1, 9))
