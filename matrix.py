class Matrix:
    def __init__(self):
        self.rows = []
        self.cols = []

    def same_type(self, other):
        if len(self.rows) == len(other.rows) and len(self.cols) == len(other.cols):
            return True
        else:
            return False

    def __add__(self, other):
        output = Matrix()
        for i, row in enumerate(self.rows):
            output.rows.append(row + other.rows[i])

        for i, col in enumerate(self.cols):
            output.cols.append(col + other.cols[i])

        return output

    def __sub__(self, other):
        output = Matrix()
        for i, row in enumerate(self.rows):
            output.rows.append(row - other.rows[i])

        for i, col in enumerate(self.cols):
            output.cols.append(col - other.cols[i])

        return output
