import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
pos = input('Enter position: ')

urls = [url]
for u in urls:
    lst = []
    html = urllib.request.urlopen(u, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lst.append(tag.get('href', None))
    urls.append(lst[int(pos) - 1])
    if len(urls) == (int(count) + 1):
        break

for u in urls:
    print(u)
