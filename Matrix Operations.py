import numpy as np

# Create a matrix
matrix = np.array([[1, 2], [3, 4]])

# Transpose
print("Transpose:\n", matrix.T)

# Inverse
print("Inverse:\n", np.linalg.inv(matrix))

# Determinant
print("Determinant:", np.linalg.det(matrix))

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
