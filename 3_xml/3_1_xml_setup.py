import xmltodict
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
urllib.request.urlretrieve(url, 'map1.osm')

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])