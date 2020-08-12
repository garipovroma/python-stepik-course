from lxml import etree

html = etree.Element("html")
body = etree.SubElement(html, 'body')
table = etree.SubElement(body, 'table')
N = 10
M = 10
for i in range(1, N + 1):
    row = etree.SubElement(table, 'tr')
    for j in range(1, M + 1):
        value = i * j
        elem = etree.SubElement(row, 'td')
        link = etree.SubElement(elem, 'a')
        link.set('href', 'http://{value}.ru')
        link.text = str(value)

with open('5_1_3_table.html', 'wb') as fout:
    fout.write(etree.tostring(html, pretty_print=True))
