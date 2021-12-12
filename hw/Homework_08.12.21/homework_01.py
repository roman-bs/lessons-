"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""
import random


class Point:  # создается точка с рандомными координатами
    def __init__(self):
        self.axis_x =  random.randint(1, 10)
        self.axis_y = random.randint(1, 10)


class Figure(Point):
    def __init__(self,):
        self.radius = Point
        self.



class Circle(Figure):
    def __init__(self, Point, radius):
        self.center = Point
        self.radius = radius

    def perimeter_circle(self): # нахождение периметра круга
        perimeter_circle = 2 * self.radius * 3.14
        return perimeter_circle

    def square_circle(self): # нахождение площади круга
        square_circle = 3.14 * self.radius ** 2
        return square_circle


class Triangle(Figure):
    def __init__(self, point1, point2, point3):
        self.point1 = Point
        self.point2 = Point
        self.point3 = Point

