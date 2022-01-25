import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count=0

html = urllib.request.urlopen(url, context=ctx).read()

tree=ET.fromstring(html)
names=tree.findall('comments')
found=names[0].findall('comment')
for i in found:
    num=i.find('count').text
    count=count+int(num)
print(count)