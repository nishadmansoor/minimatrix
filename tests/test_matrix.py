from minimatrix.matrix import Matrix
from minimatrix.operations import add, multiply, scalar_multiply
from minimatrix.sparse import SparseMatrix
from minimatrix.utils import zeros, identity, random_matrix

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
    
def test_transpose():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    At = A.transpose()
    assert At.data == [[1, 4], [2, 5], [3, 6]]

def test_sparse():
    S = SparseMatrix((3,3))
    S.add_entry(0, 1, 5)
    S.add_entry(2, 2, 10)
    dense = S.to_dense()
    assert dense == [[0, 5, 0], [0, 0, 0], [0, 0, 10]]

def test_zeros():
    Z = zeros(2, 3)
    assert Z.data == [[0, 0, 0], [0, 0, 0]]

def test_identity():
    I = identity(3)
    assert I.data == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def test_random_matrix():
    R = random_matrix(2, 2, 1, 5)
    for row in R.data:
        for val in row:
            assert 1 <= val <= 5