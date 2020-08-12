from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode("utf-8")
page_code = str(html)
a = page_code.count("C++")
b = page_code.count("Python")
print(a, b, sep = ' ')
