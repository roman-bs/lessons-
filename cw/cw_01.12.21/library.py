def filter_cars(CAR_LIST: list, year: int) -> list:
    result = []
    for car in CAR_LIST:
        if car["year"] < year:
            result.append(car)
    return result