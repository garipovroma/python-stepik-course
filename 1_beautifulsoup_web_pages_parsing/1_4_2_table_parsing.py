from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://stepik.org/media/attachments/lesson/209723/3.html").read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')
elements = soup.find_all('td')
sum = 0
for i in elements:
    sum += int(i.contents[0])
print(sum)
