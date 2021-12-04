"""
формить предыдущую задачу в виде программы, вынести функцию в отдельный файл, добавить комментарии с описанием.

"""
from library import filter_cars


if __name__ == "__main__":
    CAR_LIST = [
        {
            "serial": 12345,
            "color": "red",
            "year": 1999,
        },
        {
            "serial": 1234,
            "color": "black",
            "year": 2005,
        },
        {
            "serial": 12345,
            "color": "red",
            "year": 2010,
        },
        {
            "serial": 125,
            "color": "red",
            "year": 2020,
        },
    ]


    year = int(input("Year: "))
    print(filter_cars(CAR_LIST, year))


    print(list(filter(lambda x: x["year"] < year, CAR_LIST)))