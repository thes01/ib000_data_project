import urllib.request
from web_scraping import *

links = getLinkByRegion()

print("Parsing completed")

for (name, href) in links:
    print("Downloading {}".format(name))
    urllib.request.urlretrieve(href, "data/excel/{}.xlsx".format(name))
    print("Downloaded {}".format(name))