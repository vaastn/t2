import numpy as np

class LinearEquationSolver:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def solve(self):
        try:
            # решение системы уравнений Ax = b
            x = np.linalg.solve(self.A, self.b)
            return x
        except np.linalg.LinAlgError:
            print("Система уравнений вырожденная или несовместная")
            return None

# пример использования
A = np.array([[2, 1], [1, -3]])
b = np.array([4, -1])

solver = LinearEquationSolver(A, b)
solution = solver.solve()

if solution is not None:
    print("Решение системы уравнений:")
    print(solution)
