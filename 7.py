import urllib.request
from PIL import Image
import os

urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
img = Image.open("oxygen.png")

width, height = img.size
middle_row = height // 2

# getting every 1st of tuples of gray pixels grouped by 7 and converting R value to ASCII 
pixels = [img.getpixel((x, middle_row)) for x in range(width)]
pixels = pixels[::7]

R_values = [p[0] for p in pixels]
ascii_chars = [chr(val) for val in R_values]
message = ''.join(ascii_chars)

second_message = ''.join([chr(val) for val in [105, 110, 116, 101, 103, 114, 105, 116, 121]])

print(second_message)
os.remove("oxygen.png")