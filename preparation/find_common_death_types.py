from ExcelParserDeaths import *
import os

rome_numbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VII', 'VIII', 'IX', 'X',
                'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']


list_dir = os.listdir('data/excel')
list_dir.sort()

temp_intersection = []


def intersect_lists(first: list, second: list):
    intersection = []

    for item in first:
        if item in second:
            intersection.append(item)

    return intersection


for filename in list_dir:
    district_name = filename.split('.')[0]

    parser = ExcelParserDeaths(district_name)

    contained_numbers = []

    # now lets test each rome number if it is contained

    for number in rome_numbers:
        if parser.findRowById(number) is not False:
            contained_numbers.append(number)

    if temp_intersection == []:
        temp_intersection = contained_numbers
    else:
        temp_intersection = intersect_lists(contained_numbers, temp_intersection)

    print('{}: {}'.format(district_name, contained_numbers))
    print('common: {}'.format(temp_intersection))

    parser.close()


"""
result:
['I', 'II', 'III', 'IV', 'V', 'VI', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XVI', 'XVII', 'XVIII', 'XX']

"""
