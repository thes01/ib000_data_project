from web_scraping import *

with open('data/region_areas.csv', 'w') as csv_file:
    for region_values in getAreaByRegion():
        csv_file.write('{};{}\n'.format(repr(region_values["name"]), repr(region_values["area"])))