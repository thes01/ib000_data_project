from math import sqrt


def getMean(values: list, index: int):
    assert index >= 0 and index < len(values)

    sum = 0

    for list_obj in values:
        sum += float(list_obj[index])

    return sum / len(values)


def getStandartDeviation(values: list, index: int, mean=None):
    assert index >= 0 and index < len(values)

    if mean is None:
        mean = getMean(values, index)

    sum_of_diffs = 0

    for list_obj in values:
        _x = float(list_obj[index])

        sum_of_diffs += (_x - mean) ** 2

    return sqrt(sum_of_diffs / (len(values) - 1))


def getPearsonCorrelation(values: list, index_x: int, index_y: int):
    _n = len(values)
    mean_x = getMean(values, index_x)
    mean_y = getMean(values, index_y)

    st_dev_x = getStandartDeviation(values, index_x, mean_x)
    st_dev_y = getStandartDeviation(values, index_y, mean_y)

    sum_of_products = 0
    for list_obj in values:
        sum_of_products += list_obj[index_x] * list_obj[index_y]

    return (sum_of_products - _n * mean_x * mean_y) / ((_n - 1) * st_dev_x * st_dev_y)
