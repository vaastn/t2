class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c, (int, float)):
            return "Нужно вводить только числа!"

        if self.a < 0 or self.b < 0 or self.c < 0:
            return "С отрицательными числами ничего не выйдет!"

        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Жаль, но из этого треугольник не сделать."

        return "Ура, можно построить треугольник!"


# пример использования
triangle_checker = TriangleChecker(3, 4, 5)
print(triangle_checker.is_triangle())  # Ура, можно построить треугольник!

triangle_checker = TriangleChecker(1, 1, 1)
print(triangle_checker.is_triangle())  # Жаль, но из этого треугольник не сделать.

triangle_checker = TriangleChecker(-1, 2, 3)
print(triangle_checker.is_triangle())  # С отрицательными числами ничего не выйдет!

triangle_checker = TriangleChecker("a", 2, 3)
print(triangle_checker.is_triangle())  # Нужно вводить только числа!
