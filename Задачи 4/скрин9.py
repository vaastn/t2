class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def shape(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0]) if self.matrix else 0
        return rows, cols

    def transpose(self):
        rows, cols = self.shape()
        transposed_matrix = [[self.matrix[j][i] for j in range(rows)] for i in range(cols)]
        return Matrix(transposed_matrix)

    def determinant(self):
        rows, cols = self.shape()
        if rows != cols:
            raise ValueError("Определитель может быть вычислен только для квадратных матриц")
        if rows == 1:
            return self.matrix[0][0]
        if rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        det = 0
        for i in range(cols):
            minor = [row[:i] + row[i + 1:] for row in (self.matrix[1:])]
            det += (-1) ** i * self.matrix[0][i] * Matrix(minor).determinant()
        return det

    @staticmethod
    def add(matrix1, matrix2):
        if matrix1.shape() != matrix2.shape():
            raise ValueError("Матрицы должны иметь одинаковую форму для сложения")
        return Matrix([[matrix1.matrix[i][j] + matrix2.matrix[i][j] for j in range(matrix1.shape()[1])] for i in range(matrix1.shape()[0])])

    @staticmethod
    def subtract(matrix1, matrix2):
        if matrix1.shape() != matrix2.shape():
            raise ValueError("Матрицы должны иметь одинаковую форму для вычитания")
        return Matrix([[matrix1.matrix[i][j] - matrix2.matrix[i][j] for j in range(matrix1.shape()[1])] for i in range(matrix1.shape()[0])])

    @staticmethod
    def multiply(matrix1, matrix2):
        rows1, cols1 = matrix1.shape()
        rows2, cols2 = matrix2.shape()
        if cols1 != rows2:
            raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице для умножения")
        result = [[sum(matrix1.matrix[i][k] * matrix2.matrix[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
        return Matrix(result)

# пример использования:
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])

print("Матрица 1:")
print(matrix1)
print("\nМатрица 2:")
print(matrix2)

print("\nМатрица 1 + Матрица 2:")
print(Matrix.add(matrix1, matrix2))

print("\nМатрица 1 - Матрица 2:")
print(Matrix.subtract(matrix1, matrix2))

print("\nМатрица 1 * Матрица 2:")
print(Matrix.multiply(matrix1, matrix2))

print("\nТранспонированная матрица 1:")
print(matrix1.transpose())

print("\nОпределитель матрицы 1:")
print(matrix1.determinant())
