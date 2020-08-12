def build_html_body(html):
    return "<html>\n<body>\n" + html + "\n</body>\n</html>"

def build_table(table):
    return "<table>" + table + "</table>"

def build_row(row):
    res = ''
    for elem in row:
        res += build_element(elem)
    return "<tr>" + res + "</tr>\n"

def build_element(element):
    return "<td>" + str(element) + "</td>"

table = ""
for i in range(1, 11):
    row = [i * j for j in range(1, 11)]
    table += build_row(row)
html = build_html_body(build_table(table))
fout = open("5_2_table.html", "w")
fout.write(html)
fout.close()