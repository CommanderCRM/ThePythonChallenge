import urllib.request
import base64
from PIL import Image
from zipfile import ZipFile
import os
from collections import deque

url = 'http://www.pythonchallenge.com/pc/hex/maze.png'
credentials = b'butter:fly'
headers = {
    'Authorization': 'Basic ' + base64.b64encode(credentials).decode(),
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

img = Image.open(response)

directions = [(0,1), (0,-1), (1,0), (-1,0)]
white = (255, 255, 255, 255)

width, height = img.size

next_map = {}

entrance = (width - 2, 0)
exit = (1, height - 1)
queue = deque([exit])

def is_white_pixel(pixel):
    return pixel == white

# breadth-first search of the shortest path in the maze
while queue:
    pos = queue.popleft()
    if pos == entrance:
        break
    for d in directions:
        tmp = (pos[0] + d[0], pos[1] + d[1])
        if not tmp in next_map and 0 <= tmp[0] < width and 0 <= tmp[1] < height and not is_white_pixel(img.getpixel(tmp)):
            next_map[tmp] = pos
            queue.append(tmp)

path = []
while pos != exit:
    path.append(img.getpixel(pos)[0])
    pos = next_map[pos]

with open('maze.zip','wb') as f:
  f.write(bytes(path[1::2]))

with ZipFile('maze.zip') as zf:
    zf.extractall()

os.remove('maze.zip')