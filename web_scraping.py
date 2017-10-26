import requests
from bs4 import BeautifulSoup

def getTableHtml(url: str):
    page = requests.get('https://www.czso.cz/csu/czso/okresy-podle-pohlavi-2005-2014')
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup.find('table')

def getLinkByRegion():
    links = []
    table = getRegionsTableHtml()
    all_trs = table.find_all('tr')
    trs_names = all_trs[::4]
    trs_hrefs = all_trs[1::4]

    if len(trs_names) != len(trs_hrefs):
        raise IndexError()

    for index in range(len(trs_names)):
        name = trs_names[index].find('b').get_text().split(' - ')[0]
        href = trs_hrefs[index].find('a').get('href')

        links.append((name, href))

    return links

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