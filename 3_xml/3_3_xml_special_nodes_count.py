import urllib.request
from xml.etree import ElementTree

url = "https://stepik.org/media/attachments/lesson/245681/map2.osm"
urllib.request.urlretrieve(url, "map3.osm")

tree = ElementTree.parse("map3.osm")
root = tree.getroot()

res = 0

for node in root.iter('node'):
    for tag in node:
        if (tag.get('k') == 'amenity' and tag.get('v') == 'fuel'):
            res += 1

print(res)

