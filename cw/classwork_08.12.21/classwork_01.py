"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).

"""


class Mytime:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"


    def __eq__(self, other) -> bool:
        return (
            self.hours == other.hours and
            self.minutes == other.minutes and
            self.seconds == other.seconds
            )


    def __ne__(self, other) -> bool:
        return (
            self.hours != other.hours and
            self.minutes != other.minutes and
            self.seconds != other.seconds
            )


    def __lt__(self, other) -> bool:
        return (
            self.hours < other.hours or
            self.minutes < other.minutes or
            self.seconds < other.seconds
            )


    def __le__(self, other) -> bool:
        return (
            self.hours <= other.hours or
            self.minutes <= other.minutes or
            self.seconds <= other.seconds
            )



    def __gt__(self, other) -> bool:
        return (
            self.hours > other.hours or
            self.minutes > other.minutes or
            self.seconds > other.seconds
            )


    def __ge__(self, other) -> bool:
        return (
            self.hours >= other.hours or
            self.minutes >= other.minutes or
            self.seconds >= other.seconds
            )


if __name__ == "__main__":
    my_time_1 = Mytime(1, 2, 3)
    my_time_2 = Mytime(1, 2, 3)
    my_time_3 = Mytime(2, 3, 4)


    print(my_time_1 == my_time_2)
    print(my_time_1 == my_time_3)


    print(my_time_1 != my_time_2)
    print(my_time_1 != my_time_3)


    print(my_time_1 >= my_time_2)
    print(my_time_1 >= my_time_3)


    print(my_time_1 <= my_time_2)
    print(my_time_1 <= my_time_3)

    print(my_time_1 < my_time_2)
    print(my_time_1 < my_time_3)

    print(my_time_1 > my_time_2)
    print(my_time_1 > my_time_3)