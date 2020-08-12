from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(" https://stepik.org/media/attachments/lesson/209723/4.html").read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all('tr')
res = 0
data = []
for row in rows:
    elements = row.find_all('td')
    mas = [int(i.text.strip()) for i in elements]
    res += sum(mas)
print(res)