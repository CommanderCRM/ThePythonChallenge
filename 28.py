import urllib.request
import base64
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/ring/bell.png'
credentials = b'repeat:switch'
headers = {
    'Authorization': 'Basic ' + base64.b64encode(credentials).decode(),
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

# getting green channel, calculating difference every 2 bytes, removing most frequent value in diff
img = Image.open(response)

green_data = list(img.getchannel("G").getdata())

diff = [abs(a - b) for a, b in zip(green_data[0::2], green_data[1::2])]

filtered = list(filter(lambda x: x != 42, diff))

try:
    decoded_string = bytes(filtered).decode()
    print(decoded_string)
except UnicodeDecodeError as e:
    print(f"Error decoding bytes to string: {e}")