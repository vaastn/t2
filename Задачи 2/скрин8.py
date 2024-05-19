import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    

    def move(self, distance, direction):
        if direction == 'up':
            self.y += distance
        elif direction == 'down':
            self.y -= distance
        elif direction == 'left':
            self.x -= distance
        elif direction == 'right':
            self.x += distance
    

    def is_on_x_axis(self):
        return self.y == 0
    
    
    def is_on_y_axis(self):
        return self.x == 0


# проверка функциональности класса
point1 = Point(3, 4)
point2 = Point(6, 8)

print("Расстояние между точками:", point1.distance_to(point2))
print("Точка 1 на оси X?", point1.is_on_x_axis())
print("Точка 2 на оси Y?", point2.is_on_y_axis())

point1.move(5, 'right')
print("Координаты точки 1 после перемещения:", point1.x, point1.y)
