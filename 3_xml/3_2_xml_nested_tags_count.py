import xmltodict
import urllib.request

from xml.etree import ElementTree

# downloading osm file
url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
urllib.request.urlretrieve(url, 'map2.osm')


# first solution using xmltodict
a, b = 0, 0

with open('map1.osm', 'r', encoding='utf-8') as fin:
    xml = fin.read()
    parsedxml = xmltodict.parse(xml)
    for node in parsedxml['osm']['node']:
        if ('tag' in node):
            a += 1
        else:
            b += 1
print(a, b)

# second solution using xml.etree

tree = ElementTree.parse("map2.osm")
root = tree.getroot()
nodes = root.findall('node')
c, d = 0, 0

for node in root.iter('node'):
    tag = node.find('tag')
    if (tag == None):
        d += 1
    else:
        c += 1
print(c, d)