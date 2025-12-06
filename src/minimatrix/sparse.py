class SparseMatrix:
    """
    A Sparse matrix stored in a dictionary
    Attributes: 
        shape (tuple): (rows, cols) of the matrix
        data (dict): keys are (row, col) tuples, values are non-zero entries
    """

    def __init__(self, shape, entries=None):
        """
        Initialize a sparse matrix.
        Parameters:
            shape (tuple): (rows, cols) of the matrix
            entries (dict): Optional initial non-zero entries
        """
        self.shape = shape  # (rows, cols)
        self.data = {} if entries is None else entries

    def add_entry(self, row, col, value):
        """
        Add a non-zero entry to sparse matrix.
        Parameters:
            row (int): Row index
            col (int): Column index
            value (float): Non-zero value to add
        """
        if value != 0:
            self.data[(row, col)] = value

    def to_dense(self):
        """
        Convert sparse matrix back to regular list-of-lists matrix.
        Returns: list of lists representing the dense matrix
        """
        rows, cols = self.shape
        dense = [[0 for _ in range(cols)] for _ in range(rows)]

        for (r, c), v in self.data.items():
            dense[r][c] = v

        return dense

    def __repr__(self):
        """
        Return a string representation of the sparse matrix.
        Returns: str
        """
        return f"SparseMatrix({len(self.data)} nonzero elements)"
