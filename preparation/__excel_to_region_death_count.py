# from excel_parser import getCirulationValuesByYears
# import os

# with open('data/region_deaths.csv', mode='w') as csv_file:
#     list_dir = os.listdir('data/excel')
#     list_dir.sort()
    
#     for filename in list_dir:
#         district_name = filename.split('.')[0]
#         district_deaths = getCirulationValuesByYears(district_name)

#         csv_file.write(district_name + ";")

#         for year_value in district_deaths:
#             csv_file.write("{};".format(year_value))

#         csv_file.write('\n')

    