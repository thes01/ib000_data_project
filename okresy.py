import requests
from bs4 import BeautifulSoup

def getRegions():
    page = requests.get('https://cs.wikipedia.org/wiki/Seznam_okres%C5%AF_v_%C4%8Cesku')
    soup = BeautifulSoup(page.content, 'html.parser')

    lines = soup.select('table.wikitable tr')
    hrefs = []

    for line in lines:
        first_td = line.find('td')

        if first_td != None:
            hrefs.append(first_td.find('a').get('href'))

    return hrefs