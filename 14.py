from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from PIL import Image

password_mgr = HTTPPasswordMgrWithDefaultRealm()

password_mgr.add_password(realm=None,
                        uri='http://www.pythonchallenge.com',
                        user='huge',
                        passwd='file')

auth_handler = HTTPBasicAuthHandler(password_mgr)

opener = build_opener(auth_handler)

response = opener.open('http://www.pythonchallenge.com/pc/return/wire.png')

img = Image.open(response)

new_img = Image.new("RGB", (100, 100))

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, p = -1, 0, 0
d = 200
while d/2 > 0:
  for v in delta:
    steps = d // 2
    for s in range(steps):
      x, y = x + v[0], y + v[1]
      new_img.putpixel((x, y), img.getpixel((p,0)))
      p += 1
    d -= 1

new_img.save("new_image.png")