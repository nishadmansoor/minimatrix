class Matrix:
    """Basic 2D matrix implementation using lists of lists."""

    def __init__(self, data):
        # Ensure rows are the same length
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def shape(self):
        """Return matrix dimensions as (rows, cols)."""
        return (self.rows, self.cols)

    def transpose(self):
        """Return a new transposed Matrix."""
        t_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(t_data)

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)
