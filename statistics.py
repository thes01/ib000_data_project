from math import sqrt


def getMean(values: list):
    sum = 0

    for val in values:
        sum += float(val)

    return sum / len(values)


def getStandartDeviation(values: list, mean=None):
    if mean is None:
        mean = getMean(values)

    sum_of_diffs = 0

    for val in values:
        _x = float(val)

        sum_of_diffs += (_x - mean) ** 2

    return sqrt(sum_of_diffs / (len(values) - 1))


def getPearsonCorrelation(values_x: list, values_y: list):
    assert len(values_x) == len(values_y)

    _n = len(values_x)
    mean_x = getMean(values_x)
    mean_y = getMean(values_y)

    st_dev_x = getStandartDeviation(values_x, mean_x)
    st_dev_y = getStandartDeviation(values_y, mean_y)

    sum_of_products = 0

    for i in range(_n):
        sum_of_products += values_x[i] * values_y[i]

    return (sum_of_products - _n * mean_x * mean_y) / ((_n - 1) * st_dev_x * st_dev_y)
