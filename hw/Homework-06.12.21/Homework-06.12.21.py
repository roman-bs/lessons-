"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задния ход (изменение знака скорости).
"""

class Car:
    def __init__(self, brand, model, year, speed = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed


    def speed_plus_5(self):
        self.speed += 5


    def speed_minus_5(self):
        self.speed -= 5


    def stop(self):
        self.speed = 0


    def speed_now(self):
        print(self.speed)


    def speed_reverse(self):
        self.speed *= -1


