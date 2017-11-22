from web_scraping import *

with open('data/region_areas.csv', 'w') as csv_file:
    for region_value in getAreaByRegion():
        print(region_value)
        # csv_file.write('{}\n'.format(region_value))
