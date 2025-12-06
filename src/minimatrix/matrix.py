class Matrix:
    """
    A simple Matrix class for basic matrix operations.
    Attributes:
        data (list of list of floats): 2D list representing matrix elements
        rows (int): Number of rows in the matrix
        cols (int): Number of columns in the matrix
    """

    def __init__(self, data):
        """
        Initalize a matrix 
        Parameters: data (list of list of floats): 2D list representing matrix elements
        Raises: ValueError: If rows are not of the same length
        """
        # Ensure rows are the same length
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def shape(self):
        """
        Return matrix dimensions as (rows, cols).
        Returns: tuple (number of rows, number of columns)
        """
        return (self.rows, self.cols)

    def transpose(self):
        """
        Return a new transposed Matrix.
        Returns: the transposed Matrix
        """
        t_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(t_data)

    def __repr__(self):
        """
        Returns a string representation of the matrix. 
        Returns: str
        """
        return "\n".join(str(row) for row in self.data)
