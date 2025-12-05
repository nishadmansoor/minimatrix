from minimatrix.matrix import Matrix
from minimatrix.operations import add, multiply, scalar_multiply

def test_add():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = add(A, B)
    assert C.data == [[6, 8], [10, 12]]

def test_multiply():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    B = Matrix([[7, 8], [9, 10], [11, 12]])
    C = multiply(A, B)
    assert C.data == [[58, 64], [139, 154]]

def test_scalar():
    A = Matrix([[1, 2], [3, 4]])
    k = 3
    C = scalar_multiply(A, k)
    assert C.data == [[3, 6], [9, 12]]
