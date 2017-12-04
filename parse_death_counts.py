from ExcelParserDeaths import *
import os

list_dir = os.listdir('data/excel')
list_dir.sort()

with open('data/region_deaths.txt', 'w') as txt_file:
    for filename in list_dir:
        district_name = filename.split('.')[0]

        parser = ExcelParserDeaths(district_name)

        txt_file.write("{}\n".format({"region": district_name, "deaths": parser.getValuesByYearsForCommonIds()}))

        parser.close()
