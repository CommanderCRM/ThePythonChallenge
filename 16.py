from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from PIL import Image
import numpy as np

password_mgr = HTTPPasswordMgrWithDefaultRealm()

password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com',
                          user='huge',
                          passwd='file')

auth_handler = HTTPBasicAuthHandler(password_mgr)

opener = build_opener(auth_handler)

response = opener.open('http://www.pythonchallenge.com/pc/return/mozart.gif')

img = Image.open(response)

# placing 195 (RGB pink) pixels in a straight line
shifted = [
  bytes(np.roll(row, -row.tolist().index(195)).tolist())
  for row in np.array(img)
]

Image.frombytes(img.mode, img.size, b"".join(shifted)).save("shifted.gif")
