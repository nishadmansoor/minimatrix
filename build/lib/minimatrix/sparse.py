class SparseMatrix:
    """Sparse matrix using dictionary storage."""

    def __init__(self, shape, entries=None):
        self.shape = shape  # (rows, cols)
        self.data = {} if entries is None else entries

    def add_entry(self, row, col, value):
        """Add a non-zero entry to sparse matrix."""
        if value != 0:
            self.data[(row, col)] = value

    def to_dense(self):
        """Convert sparse matrix back to regular list-of-lists matrix."""
        rows, cols = self.shape
        dense = [[0 for _ in range(cols)] for _ in range(rows)]

        for (r, c), v in self.data.items():
            dense[r][c] = v

        return dense

    def __repr__(self):
        return f"SparseMatrix({len(self.data)} nonzero elements)"
