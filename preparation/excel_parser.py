from openpyxl import load_workbook

BLOOD_CIRCULATION_ID = 'IX'

def getCountForYear(row, year: int):
    assert year >= 2005 and year <= 2014
    return row[year - 2003].value

def getCirulationValuesByYears(region_name):
    wb = load_workbook(filename="data/excel/{}.xlsx".format(region_name), read_only=True)
    sheet = wb.active

    result_list = []

    for row in sheet.rows:
        if row[0].value == BLOOD_CIRCULATION_ID:
            for year in range(2005,2015):
                result_list.append(getCountForYear(row,year))

            # we have reached the target row, so the rest is redundant
            break

    return result_list
