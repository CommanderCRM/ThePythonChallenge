import urllib.request
import base64
from PIL import Image
import bz2
import keyword

url = 'http://www.pythonchallenge.com/pc/hex/zigzag.gif'
credentials = b'butter:fly'
headers = {
  'Authorization': 'Basic ' + base64.b64encode(credentials).decode(),
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)


def get_palette_table(im):
  palette = im.getpalette()[::3]
  table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))
  return table


# difference between image and its color palette table
def get_diff_indices(im, table):
  raw = im.tobytes()
  trans = raw.translate(table)
  zipped = list(zip(raw[1:], trans[:-1]))
  diff = list(filter(lambda p: p[0] != p[1], zipped))
  indices = [i for i, p in enumerate(zipped) if p[0] != p[1]]
  return raw, diff, indices


def create_new_image(im, indices, raw):
  im2 = Image.new("RGB", im.size)
  colors = [(255, 255, 255)] * len(raw)
  for i in indices:
    colors[i] = (0, 0, 0)
  im2.putdata(colors)
  return im2


def get_text(diff):
  if diff:
    s = [t[0] for t in diff]
    text = bz2.decompress(bytes(s))
  else:
    text = ''
  return text


def filter_keywords(text):
  return set(
    [w.decode() for w in text.split() if not keyword.iskeyword(w.decode())])


im = Image.open(response)
table = get_palette_table(im)
raw, diff, indices = get_diff_indices(im, table)
im2 = create_new_image(im, indices, raw)
text = get_text(diff)
keywords = filter_keywords(text)

print(keywords)
