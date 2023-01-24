import pickle
import os
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/banner.p"

urllib.request.urlretrieve(url, "banner.p")

with open("banner.p", "rb") as f:
  data = pickle.load(f)

# recovering data from pickle format, printing line-by-line
for line in data:
  for count in line:
    print(count[0] * count[1], end='')
  print()

os.remove("banner.p")
