import requests
from io import BytesIO
from PIL import Image
import math
import os

url = 'http://www.pythonchallenge.com/pc/rock/beer2.png'
response = requests.get(url, auth=('kohsamui', 'thailand'))
img = Image.open(BytesIO(response.content))

if not os.path.exists("img"):
    os.makedirs("img")

data = list(img.getdata())
data_set = set(data)

# creating new images with perfect square dimensions
for max_num in sorted(data_set, reverse=True):
    img_data = [d for d in data if d < max_num]
    n = math.sqrt(len(img_data))
    if n == int(n) and n > 0:
        new_img = Image.new(img.mode, (int(n), int(n)))
        new_img.putdata(img_data)
        new_img.save(f"img/{int(n)}.png")
