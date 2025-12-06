from .matrix import Matrix

def add(A: Matrix, B: Matrix) -> Matrix:
    """
    Adds two matrices element-wise.
    Parameters:
        A (Matrix): First matrix
        B (Matrix): Second matrix
    Returns: Matrix - Resultant matrix after addition 
    Raises: ValueError if dimensions do not match.
    """
    if A.shape() != B.shape():
        raise ValueError("Matrix dimensions must match for addition.")

    result = [
        [A.data[i][j] + B.data[i][j] for j in range(A.cols)]
        for i in range(A.rows)
    ]
    return Matrix(result)


def multiply(A: Matrix, B: Matrix) -> Matrix:
    """
    Matrix multiplication using triple nested loops.
    Parameters:
        A (Matrix): First matrix
        B (Matrix): Second matrix
    Returns: Matrix - The matrix product of A and B
    Raises: ValueError if inner dimensions do not match.
    """
    if A.cols != B.rows:
        raise ValueError("Inner dimensions must match for multiplication.")

    result = [
        [sum(A.data[i][k] * B.data[k][j] for k in range(A.cols)) for j in range(B.cols)]
        for i in range(A.rows)
    ]
    return Matrix(result)


def scalar_multiply(A: Matrix, k: float) -> Matrix:
    """Multiply every element of matrix by a scalar.
    Parameters:
        A (Matrix): Input matrix
        k (float): Scalar value
    Returns: Matrix - A new matrix containing matrix A multiplied by scalar k"""
    return Matrix([[A.data[i][j] * k for j in range(A.cols)] for i in range(A.rows)])