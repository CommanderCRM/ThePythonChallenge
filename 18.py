import gzip, difflib

# data is 2 columns
data = gzip.open("deltas.gz")
d1, d2 = [], []
for line in data:
  d1.append(line[:53].decode() + "\n")
  d2.append(line[56:].decode())

compare = difflib.Differ().compare(d1, d2)

# hex to bytes
with open("f.png", "wb") as f, open("f1.png",
                                    "wb") as f1, open("f2.png", "wb") as f2:
  for line in compare:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == '+':
      f1.write(bs)
    elif line[0] == '-':
      f2.write(bs)
    else:
      f.write(bs)
