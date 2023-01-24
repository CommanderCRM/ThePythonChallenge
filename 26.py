import hashlib
import multiprocessing
from zipfile import ZipFile
import os

md5 = 'bbb8b499a0eef99b52c7f13f4e78c24b'

with open('mybroken.zip', 'rb') as zip_ref:
  data = zip_ref.read()


# replacing possibly broken bytes with 0-255 values, checking if correct
def search_and_save(data, md5, start, end):
  for i in range(start, end):
    for j in range(256):
      newData = data[:i] + bytes([j]) + data[i + 1:]
      if hashlib.md5(newData).hexdigest() == md5:
        with open('repaired.zip', 'wb') as f:
          f.write(newData)
        return


# algorithm is resource-intensive, hence multiprocessing
def multiprocess_search(data, md5code, num_processes):
  pool = multiprocessing.Pool(processes=num_processes)
  chunk_size = len(data) // num_processes
  chunks = [(i * chunk_size, (i + 1) * chunk_size)
            for i in range(num_processes)]
  pool.starmap(search_and_save,
               [(data, md5, start, end) for start, end in chunks])
  pool.close()
  pool.join()


multiprocess_search(data, md5, 4)

with ZipFile('repaired.zip') as zf:
  zf.extractall()

os.remove('repaired.zip')
