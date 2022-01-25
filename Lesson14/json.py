import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link: ')
print('Retrieving url:', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters') 

info = json.loads(data)
count = 0
sum = 0

for item in info["comments"]:
    count = count+1
    number = int(item["count"])
    sum = sum + number
print('Total count:', count)
print ('Sum:', sum)