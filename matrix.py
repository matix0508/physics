class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.table.append(row)
    def get_data(self, tab):
        for i, row in enumerate(tab):
                for j, col in enumerate(row):
                    self.table[i][j] = col

    def data_one_by_one(self):
        for i, row in enumerate(self.table):
            for j, col in enumerate(row):
                self.table[i][j] = int(input(f"ROW: {i}, COL: {j}, INPUT: "))

    def __eq__(self, other):
        if not self.same_type(other):
            return False
        for i, row in enumerate(self.table):
            for j, col in enumerate(row):
                if other.table[i][j] != col:
                    return False
        return True

    def __repr__(self):
        output = ""
        if self.cols > 1:
            output = "["
        for i, row in enumerate(self.table):
            output += str(row)
            if i != len(self.table) - 1:
                output += "\n"
        if self.cols > 1:
            output += "]"
        return output

    def same_type(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return True
        else:
            return False

    def __add__(self, other):
        if self.same_type(other):
            output = Matrix(self.rows, self.cols)
            for i, row in enumerate(self.table):
                for j, col in enumerate(row):
                    output.table[i][j] = col + other.table[i][j]


    def __sub__(self, other):
        if self.same_type(other):
            output = Matrix(self.rows, self.cols)
            for i, row in enumerate(self.table):
                for j, col in enumerate(row):
                    output.table[i][j] = col - other.table[i][j]
            return output

    def __mul__(self, other):
        if type(other) == type(self):
            return self.dot(other)

    def dot(self, other):
        if self.cols == other.rows:
            output = Matrix(self.rows, other.cols)
            for i, row in enumerate(output.table):
                for j, col in enumerate(row):
                    for k in range(self.cols):
                        output.table[i][j] += self.table[i][k] * other.table[k][j]
            return output


        return output
