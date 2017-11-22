import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

from statistics import *

def loadCsvFile(filename: str):
    data = []
    with open('data/{}.csv'.format(filename)) as csv_file:
        for line in csv_file:
            data.append(line.split(';'))

    return data


data_deaths = loadCsvFile('region_deaths')
data_counts = loadCsvFile('region_counts')
data_areas = loadCsvFile('region_areas')

data_deaths.sort(key=lambda tup: tup[0], reverse=True)
data_counts.sort(key=lambda tup: tup[0], reverse=True)
data_areas.sort(key=lambda tup: tup[0], reverse=True)

assert len(data_deaths) == len(data_counts) == len(data_areas)

for year in range(2005, 2015):
    values = [] # (name, density, percentage of deaths)

    for i in range(len(data_deaths)):
        district_name = data_counts[i][0]
        district_area = float(data_areas[i][1])
        district_count = float(data_counts[i][year - 2004])
        district_death = float(data_deaths[i][year - 2004])

        # by a year
        density = district_count / district_area
        percent_death = district_death / district_count

        values.append((district_name,density, percent_death))

    values.sort(key=lambda tup: tup[1], reverse=False)

    # print(values)

    # y_pos = np.arange(len(values))

    # plt.bar(y_pos, list(map(lambda tup: tup[2],values)), align='center', alpha=0.5)
    # plt.xticks(y_pos,list(map(lambda tup: tup[0], values)), rotation='vertical')
    # plt.ylabel('Okresy')
    # plt.title('Okresy v ČR')

    # plt.show()

    # print(getMean(values, 1))

    print(getPearsonCorrelation(values, 1, 2))