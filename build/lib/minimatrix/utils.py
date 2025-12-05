import random
from .matrix import Matrix

def zeros(rows, cols):
    """Create a matrix filled with zeros."""
    return Matrix([[0 for _ in range(cols)] for _ in range(rows)])

def identity(n):
    """Create an identity matrix."""
    return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

def random_matrix(rows, cols, min_val=0, max_val=10):
    """Create a matrix filled with random integers."""
    return Matrix([[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)])
