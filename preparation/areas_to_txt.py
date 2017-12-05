from web_scraping import *

with open('data/region_areas.txt', 'w') as txt_file:
    for region_values in getAreaByRegion():
        txt_file.write('{}\n'.format(repr(region_values)))
