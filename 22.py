import urllib.request
import base64
from PIL import Image, ImageDraw

url = 'http://www.pythonchallenge.com/pc/hex/white.gif'
credentials = b'butter:fly'
headers = {
    'Authorization': 'Basic ' + base64.b64encode(credentials).decode(),
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

img = Image.open(response)

joy_img = Image.new("RGB", (500, 200))
drawer = ImageDraw.Draw(joy_img)
cx, cy = 0, 100

# we need to make some pixels brighter moving in joystick-like style
for frame in range(img.n_frames):
    img.seek(frame)
    left, upper, right, lower = img.getbbox()

    dx = left - 100
    dy = upper - 100

    if dx == dy == 0:
      cx += 50
      cy = 100

    cx += dx
    cy += dy
    drawer.point([cx, cy])

joy_img.save("joy_img.png")