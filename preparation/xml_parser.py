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
            if child.tag == tag('uze') and child.text == id:
                match_id = True
            if child.tag == tag('uka') and child.text == indicator:
                match_indicator = True
            if child.tag == tag('hod'):
                value = child.text

        if match_id and match_indicator:
            return value

def getDictOfDiscrictsForYear(year: int):
    assert year >= 2005 and year <= 2014

    discricts_dict = {}
        
    tree = etree.parse('data/ob_{}.xml'.format(year))
    root = tree.getroot()

    elements = tree.findall(tag('element', is_global=True))
    entries = tree.findall(tag('udaj', is_global=True))

    for element in elements:
        wanted = False
        el_name = ''
        el_id = element.attrib['ID']
        for child in element:
            if (child.tag == tag('ciselnik') and child.text == DISTRICT_ID) or (child.tag == tag('kod') and child.text == PRAGUE_ID):
                wanted = True
            if (child.tag == tag('text')):
                el_name = child.text

        if not wanted:
            continue

        val = getEntryValue(entries, el_id, 'u1')

        # add region to the dictionary
        discricts_dict[el_name] = val

    return discricts_dict
