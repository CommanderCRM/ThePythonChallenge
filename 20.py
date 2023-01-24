import urllib.request
import base64
import os
from zipfile import ZipFile

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
credentials = b'butter:fly'
headers = {
  'Authorization': 'Basic ' + base64.b64encode(credentials).decode(),
  'Range': 'bytes=1152983631-'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

with open("level21.zip", "wb") as f:
  f.write(response.read())

with ZipFile('level21.zip') as zf:
  zf.extractall(pwd=b'redavni')

os.remove('level21.zip')
