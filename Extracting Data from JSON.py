import json
import urllib.request

location = input("Enter URL: ")
url = urllib.request.urlopen(location)
data = url.read()

info = json.loads(data)

sum = 0
comments = info['comments']
for comment in comments:
    sum = sum + int(comment['count'])

print(sum)