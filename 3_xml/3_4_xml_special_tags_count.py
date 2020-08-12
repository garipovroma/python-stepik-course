import urllib.request
from xml.etree import ElementTree

url = "https://stepik.org/media/attachments/lesson/245681/map2.osm"
urllib.request.urlretrieve(url, "map4.osm")

tree = ElementTree.parse("map4.osm")
root = tree.getroot()

res = 0

for elem in list(root):
    for tag in list(elem):
        if (tag.get('k') == 'amenity' and tag.get('v') == 'fuel'):
            res += 1

print(res)