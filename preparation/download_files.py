import urllib.request
from web_scraping import *

links = getLinkByRegion()

print("Parsing completed")

for link in links:
    print("Downloading {}".format(link.region))
    urllib.request.urlretrieve(link.href, "data/excel/{}.xlsx".format(link.region))
    print("Downloaded {}".format(link.region))