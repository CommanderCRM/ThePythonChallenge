import urllib.request
import base64
import os
from PIL import Image
import wave
import shutil

credentials = b'butter:fly'
headers = {
  'Authorization': 'Basic ' + base64.b64encode(credentials).decode(),
}

if not os.path.exists("wav"):
  os.mkdir("wav")

# getting 25 .wav files
for i in range(1, 26):
  url = f"http://www.pythonchallenge.com/pc/hex/lake{i}.wav"
  filename = f"wav/lake{i}.wav"
  req = urllib.request.Request(url, headers=headers)
  with urllib.request.urlopen(req) as response, open(filename,
                                                     'wb') as out_file:
    data = response.read()
    out_file.write(data)
  print(f"File {i} downloaded.")

width, height = 300, 300
result = Image.new('RGB', (width, height), 0)

# constructing an image from 25 wav files as bytes, in grid
for i, file in enumerate(os.listdir("wav")):
  with wave.open("wav/" + file, 'r') as f:
    num_frames = f.getnframes()
    byte = f.readframes(num_frames)
    img = Image.frombytes('RGB', (60, 60), byte)
    result.paste(img, (60 * (i % 5), 60 * (i // 5)))

result.save("result.jpg")

print('Image constructed.')

shutil.rmtree('wav')
