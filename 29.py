import requests
import bz2

url = 'http://www.pythonchallenge.com/pc/ring/guido.html'
credentials = b'repeat:switch'

response = requests.get(url, auth=('repeat', 'switch'))

# converting line length to byte, bz2 decompression
raw = response.text.splitlines()[12:]
data = bytes([len(i) for i in raw])
print(bz2.decompress(data))
