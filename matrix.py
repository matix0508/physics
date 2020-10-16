from errors import WrongDimensionsError

def epsilon(i, j):
    if (i, j) == (0, 1):
        return 1
    if (i, j) == (1, 0):
        return -1

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
        self.T = None

    def get_data(self, tab):
        for i, row in enumerate(tab):
                for j, col in enumerate(row):
                    self.table[i][j] = col
        self.T = self.transpose()

    def data_one_by_one(self):
        for i, row in enumerate(self.table):
            for j, col in enumerate(row):
                self.table[i][j] = int(input(f"ROW: {i}, COL: {j}, INPUT: "))
        self.T = self.transpose()

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

        return output + "\n"

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
            output.T = output.transpose()
            return output
        raise WrongDimensionsError("Matrices have different dimensions")


    def __sub__(self, other):
        if self.same_type(other):
            output = Matrix(self.rows, self.cols)
            for i, row in enumerate(self.table):
                for j, col in enumerate(row):
                    output.table[i][j] = col - other.table[i][j]
            output.T = output.transpose()
            return output
        raise WrongDimensionsError("Matrices have different dimensions")

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
            output.T = output.transpose()
            return output
        else:
            raise WrongDimensionsError("number of columns of first matrix != number of rows in the other")

    def transpose(self):
        output = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                output.table[i][j] = self.table[j][i]
        return output

    def det(self):
        total=0
        # Section 1: store indices in list for row referencing
        indices = list(range(len(self.table)))

        # Section 2: when at 2x2 submatrices recursive calls end
        if len(self.table) == 2 and len(self.table[0]) == 2:
            val = self.table[0][0] * self.table[1][1] - self.table[1][0] * self.table[0][1]
            return val

        # Section 3: define submatrix for focus column and
        #      call this function
        for fc in indices: # A) for each focus column, ...
            # find the submatrix ...
            As = Matrix(self.rows, self.cols)
            As.table = self.table
                 # B) make a copy, and ...
            As.table = As.table[1:] # ... C) remove the first row
            height = len(As.table) # D)

            for i in range(height):
                # E) for each remaining row of submatrix ...
                #     remove the focus column elements
                As.table[i] = As.table[i][0:fc] + As.table[i][fc+1:]

            sign = (-1) ** (fc % 2) # F)
            # G) pass submatrix recursively
            sub_det = As.det()
            # H) total all returns from recursion
            total += sign * self.table[0][fc] * sub_det

        return total

    def change_col(self, colidx, col):
        output = Matrix(self.rows, self.cols)
        output.get_data(self.table)
        for i in range(self.rows):
            output.table[i][colidx] = col[i][0]
        return output

def solve(A, b):
    rows = b.rows
    W = A.det()
    x = []
    print(W)
    for i in range(rows):
        Wn = A.change_col(i, b.table)
        print(Wn)
        x.append([Wn.det()/W])
    output = Matrix(rows, 1)
    print(x)
    output.get_data(x)
    return output
