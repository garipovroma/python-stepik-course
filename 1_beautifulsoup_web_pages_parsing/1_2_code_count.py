from urllib.request import urlopen
from re import findall
from collections import Counter

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode("utf-8")
page_code = str(html)
data = findall(r'<code>\w+.</code>', page_code)
most_frequent = Counter(data).most_common()
ans = [i[0][6:-7] for i in most_frequent if i[1] == most_frequent[0][1]]
ans = sorted(ans)
for i in ans:
    print(i, end = ' ')
# <code>
# </code>