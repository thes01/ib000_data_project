def loadNames(filename: str):
    with open('data/{}.csv'.format(filename)) as csv:
        names = []

        for line in csv:
            names.append(line.split(';')[0])
    return names

first = loadNames('region_areas')
second = loadNames('region_counts')
third = loadNames('region_deaths')


print(second == third)