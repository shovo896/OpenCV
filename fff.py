import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Original Matrix:")
print(matrix)

# Add 10 to each element
matrix_plus_10 = matrix + 10
print("\nMatrix after adding 10:")
print(matrix_plus_10)

# Multiply each element by 2
matrix_times_2 = matrix * 2
print("\nMatrix after multiplying by 2:")
print(matrix_times_2)

# Sum of all elements
total_sum = np.sum(matrix)
print("\nSum of all elements:", total_sum)

# Mean of all elements
mean_value = np.mean(matrix)
print("Mean of all elements:", mean_value)
