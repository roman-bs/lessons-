"""
Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска).
Создать функцию, которая возвращает новый список со всеми машинами, год выпуска которых больше Х
"""

def filter_cars(CAR_LIST: list, year: int) -> list:
    result = []
    for car in CAR_LIST:
        if car["year"] < year:
            result.append(car)
    return result

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
