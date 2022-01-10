import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
repeat_process = int(input("Enter count:"))
link_position = int(input("Enter position:"))

repeater = 0
while repeater < repeat_process:
    repeater += 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    position = 0
    for tag in tags:
        new_url = tag.get('href', None)
        if position < link_position:
            position += 1
            url = new_url
        else:
            break
    print("Retrieving:", url)