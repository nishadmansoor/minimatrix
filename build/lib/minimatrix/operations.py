from .matrix import Matrix

def add(A: Matrix, B: Matrix) -> Matrix:
    """Elementwise matrix addition."""
    if A.shape() != B.shape():
        raise ValueError("Matrix dimensions must match for addition.")

    result = [
        [A.data[i][j] + B.data[i][j] for j in range(A.cols)]
        for i in range(A.rows)
    ]
    return Matrix(result)


def multiply(A: Matrix, B: Matrix) -> Matrix:
    """Matrix multiplication using triple nested loops."""
    if A.cols != B.rows:
        raise ValueError("Inner dimensions must match for multiplication.")

    result = [
        [sum(A.data[i][k] * B.data[k][j] for k in range(A.cols)) for j in range(B.cols)]
        for i in range(A.rows)
    ]
    return Matrix(result)


def scalar_multiply(A: Matrix, k: float) -> Matrix:
    """Multiply every element of matrix by a scalar."""
    return Matrix([[A.data[i][j] * k for j in range(A.cols)] for i in range(A.rows)])