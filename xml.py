from lxml import etree

# get a value from an unique entry
def getEntryValue(entries, id, indicator):
    for entry in entries:
        match_id = False
        match_indicator = False

        value = ''
        for child in entry:
            if child.tag == '{http://vdb.czso.cz/xml/export}uze' and child.text == id:
                match_id = True
            if child.tag == '{http://vdb.czso.cz/xml/export}uka' and child.text == indicator:
                match_indicator = True
            if child.tag == '{http://vdb.czso.cz/xml/export}hod':
                value = child.text

        if match_id and match_indicator:
            return value
        
        
tree = etree.parse('data/ob_2004.xml')
root = tree.getroot()

elements = tree.findall('//{http://vdb.czso.cz/xml/export}element')
entries = tree.findall('//{http://vdb.czso.cz/xml/export}udaj')

for element in elements:
    wanted = False
    el_name = ''
    el_id = element.attrib['ID']
    for child in element:
        if (child.tag == '{http://vdb.czso.cz/xml/export}ciselnik' and child.text == '101') or (child.tag == '{http://vdb.czso.cz/xml/export}kod' and child.text == '3018'):
            wanted = True
        if (child.tag == '{http://vdb.czso.cz/xml/export}text'):
            el_name = child.text

    if not wanted:
        continue

    val = getEntryValue(entries, el_id, 'u1')

    print("{}: {}".format(el_name, val))

