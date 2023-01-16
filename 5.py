import pickle
import os
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/banner.p"

urllib.request.urlretrieve(url, "banner.p")

with open("banner.p", "rb") as f:
    data = pickle.load(f)

for line in data:
  for count in line:
    print(count[0]*count[1],end='')
  print()

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "banner.p")
os.remove(file_path)