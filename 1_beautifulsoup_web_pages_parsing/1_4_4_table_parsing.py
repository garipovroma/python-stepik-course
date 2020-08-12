from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(" https://stepik.org/media/attachments/lesson/209723/5.html").read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
elements = soup.find_all('td')
mas = [int(i.text.strip()) for i in elements]
print(sum(mas))