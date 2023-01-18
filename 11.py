from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from PIL import Image

password_mgr = HTTPPasswordMgrWithDefaultRealm()

password_mgr.add_password(realm=None,
                        uri='http://www.pythonchallenge.com',
                        user='huge',
                        passwd='file')

auth_handler = HTTPBasicAuthHandler(password_mgr)

opener = build_opener(auth_handler)

response = opener.open('http://www.pythonchallenge.com/pc/return/cave.jpg')

img = Image.open(response)

(w, h) = img.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(0, w, 2):
    for j in range(0, h, 2):
        even.putpixel((i // 2, j // 2), img.getpixel((i, j)))

for i in range(1, w, 2):
    for j in range(1, h, 2):
        odd.putpixel((i // 2, j // 2), img.getpixel((i, j)))

even.save('even.jpg')
odd.save('odd.jpg')
