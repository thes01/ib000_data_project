import requests
from bs4 import BeautifulSoup

def getRegionsTableHtml():
    page = requests.get('https://cs.wikipedia.org/wiki/Seznam_okres%C5%AF_v_%C4%8Cesku')
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup.find('table')

def getAreaByRegion():
    regions = []

    table = getRegionsTableHtml()

    for tr in table.find_all('tr'):
        tds = tr.find_all('td')

        if tds == []:
            continue

        a_region = tds[0].find('a')

        if a_region == None:
            continue

        region_name = a_region.get('title').replace('Okres ', '')
        text_area = tds[2].get_text().replace('\xa0','').replace(',','.')

        val_area = float(text_area)

        regions.append('{};{}'.format(region_name, val_area))

    return regions