"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""
import random


class Point:
    def __init__(self, x, y):
        self.axis_x =  x
        self.axis_y = y


class Figure(Point):
    def __init__(self):
        point_1 = Point(1, 1)
        point_2 = Point(8, 1)
        point_3 = Point(1, 8)
        point_4 = Point(8, 8)
        point_mid = Point(4, 8)



class Circle(Figure):
    def __init__(self, Point, radius):
        self.point = Point
        self.radius = radius

    def perimeter_circle(self): # нахождение периметра круга
        perimeter_circle = 2 * self.radius * 3.14
        return perimeter_circle

    def square_circle(self): # нахождение площади круга
        square_circle = 3.14 * self.radius ** 2
        return square_circle


class Triangle(Figure):
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3


    def square_triangle(self):
        side1 = self.axis_x


if __name__ == "__main__":
