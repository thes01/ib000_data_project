import requests
from bs4 import BeautifulSoup
from okresy import getRegions

all_regions = getRegions()

values = []

def getValFromTh(th):
    return th.find_next_sibling().get_text().split('\xa0')[0]

for region in all_regions:
    page = requests.get('https://cs.wikipedia.org{}'.format(region))
    soup = BeautifulSoup(page.content, 'html.parser')

    th_area = soup.find('th', text="Rozloha")
    th_count = soup.find('th', text="Počet obyvatel")

    if th_area != None and th_count != None:
        area = getValFromTh(th_area)
        count = getValFromTh(th_count)

        print("Area: {} Count: {}".format(area, count))
    else:
        print("-")



# link = soup.select('a[title="Hustota zalidnění"]')
# value = link.find_parent().find_next_sibling().get_text().split('\xa0')[0]

# print('Pro {} je hustota zalidnění {} ob./km2'.format(region, value))