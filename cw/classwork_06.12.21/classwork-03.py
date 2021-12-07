"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""


class Cat:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def meow(self):
        print(f"Meow {self.name}")

    def change_name(self, name):
        self.name = name


if __name__ == "__main__":
    cat_gucii = Cat(100, 100, "Gucci", 10)
    cat_gucii.jump()
    cat_gucii.change_name("Ralph")
    cat_gucii.change_name("Gucci")
    cat_gucii.meow()

    print(cat_gucii.name)
    print(cat_gucii.height)
    print(cat_gucii.weight)
    print(cat_gucii.age)
