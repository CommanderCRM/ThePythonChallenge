from itertools import groupby, islice

def lookandsay(number='1'):
  while True:
    yield number
    number = ''.join(str(len(list(g))) + k for k,g in groupby(number))

numbers = list(islice(lookandsay(), 31))
print(len(numbers[30]))