import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

from statistics import *

COMMON_IDS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XVI', 'XVII', 'XVIII', 'XX']


def loadTxtFile(filename: str):
    data = []
    with open('data/{}.txt'.format(filename)) as txt_file:
        for line in txt_file:
            if len(line) > 0:
                data.append(eval(line))
    return data

data_deaths = loadTxtFile('region_deaths')
data_counts = loadTxtFile('region_counts')
data_areas = loadTxtFile('region_areas')

data_deaths.sort(key=lambda dict: dict["region"])
data_counts.sort(key=lambda dict: dict["region"])
data_areas.sort(key=lambda dict: dict["region"])

assert len(data_deaths) == len(data_counts) == len(data_areas)

for common_id in COMMON_IDS:
    print('{}:\n'.format(common_id))

    for year in range(2004, 2005):
        values = []  # (name, density, percentage of deaths)

        for i in range(len(data_deaths)):
            district_name = data_counts[i]["region"]
            district_area = data_areas[i]["area"]
            district_count = int(data_counts[i]["counts"][year - 2005])
            district_death = data_deaths[i]["deaths"][common_id][year - 2005]

            # by a year
            density = district_count / district_area
            percent_death = (district_death / district_count) * 100

            values.append((district_name, density, percent_death))

        values.sort(key=lambda tup: tup[1], reverse=False)

        y_pos = np.arange(len(values))

        plt.rcParams["figure.figsize"] = (15, 10)
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.2)

        plt.bar(y_pos, list(map(lambda tup: tup[2], values)), align='center', alpha=0.5)
        plt.xticks(y_pos, list(map(lambda tup: tup[0], values)), rotation='vertical')
        plt.ylabel('Počet úmrtí v %')
        plt.title('Úmrtí {} v jedn. okresech v roce {} - seřazeno podle hustoty (vlevo nejmenší)'.format(common_id, year))

        plt.savefig('graphs/{}-{}'.format(common_id, year), dpi=200)
        plt.clf()

        print("{}: {}".format(year, getPearsonCorrelation(values, 1, 2)))
