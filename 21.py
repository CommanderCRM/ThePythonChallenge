import zlib
import bz2

result = ""

with open("package.pack", "rb") as f:
  data = f.read()

decompress_methods = {
  b'x\x9c': (zlib.decompress, ' '),
  b'BZh': (bz2.decompress, '#'),
  b'\x9cx': (lambda x: x[::-1], '\n')
}

# constructing a message from different deciphered chunks
while True:
  for key in decompress_methods:
    if data.startswith(key):
      data = decompress_methods[key][0](data)
      result += decompress_methods[key][1]
      break
    elif key == b'\x9cx' and data.endswith(key):
      data = decompress_methods[key][0](data)
      result += decompress_methods[key][1]
      break
  else:
    break

print(result)
