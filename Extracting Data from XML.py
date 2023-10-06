import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
data.decode()
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
sum = 0
for comment in comments:
    count = comment.find('count').text
    sum = sum + int(count)

print(sum)