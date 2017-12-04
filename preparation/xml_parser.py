from lxml import etree

DISTRICT_ID = '101'
PRAGUE_ID = '3018'

# a helper function to add the namespace and/or global prefix
def tag(tag_name: str, is_global=False, namespace = "{http://vdb.czso.cz/xml/export}"):
    glob_prefix = "//" if is_global else ""
    return glob_prefix + namespace + tag_name

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

def processEntries(entries):
    entries_list = {}

    for entry in entries:
        value = ''
        uze_id = ''
        indicator = ''

        for child in entry:
            if child.tag == tag('uze'):
                uze_id = child.text
            if child.tag == tag('uka'):
                indicator = child.text
            if child.tag == tag('hod'):
                value = child.text
            if value != '' and uze_id != '' and indicator != '':
                break

        # entries_list.append({"uze" : uze_id, "indicator": indicator, "value": value})

        # we are interested only in u1 indicator values

        if indicator == 'u1':
            entries_list[uze_id] = value

    return entries_list


def getDictOfDiscrictsForYear(year: int):
    assert year >= 2005 and year <= 2014

    discricts_dict = {}
        
    tree = etree.parse('data/ob_{}.xml'.format(year))
    root = tree.getroot()

    elements = tree.findall('//{http://vdb.czso.cz/xml/export}element')
    entries = tree.findall('//{http://vdb.czso.cz/xml/export}udaj')

    entries_list = processEntries(entries)

    for element in elements:
        wanted = False
        el_name = ''
        el_id = element.attrib['ID']
        for child in element:
            if (child.tag == '{http://vdb.czso.cz/xml/export}ciselnik' and child.text == DISTRICT_ID) or (child.tag == '{http://vdb.czso.cz/xml/export}kod' and child.text == PRAGUE_ID):
                wanted = True
            if (child.tag == '{http://vdb.czso.cz/xml/export}text'):
                el_name = child.text

        if not wanted:
            continue

        val = entries_list[el_id]

        # val = getEntryValue(entries, el_id, 'u1')

        # add region to the dictionary
        discricts_dict[el_name] = val

    return discricts_dict
