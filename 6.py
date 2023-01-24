import urllib.request
import zipfile
import os
import re

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
urllib.request.urlretrieve(url, "channel.zip")

nothing_list = []
comments = []

# linked list, but now in zip archive
with zipfile.ZipFile("channel.zip", "r") as zip_ref:
  current_file = "90052.txt"
  while True:
    contents = zip_ref.read(current_file).decode("utf-8")
    match = re.search("Next nothing is (\d+)", contents)
    if match:
      current_file = match.group(1) + ".txt"
      nothing_list.append(current_file)
      comments.append(zip_ref.getinfo(current_file).comment.decode("utf-8"))
    else:
      break

print("".join(comments))
os.remove("channel.zip")
