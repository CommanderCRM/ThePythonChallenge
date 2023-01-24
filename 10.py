from itertools import groupby, islice


# https://oeis.org/A005150
def lookandsay(number='1'):
  while True:
    yield number
    number = ''.join(str(len(list(g))) + k for k, g in groupby(number))


# we need to find the length of a[30]
numbers = list(islice(lookandsay(), 31))
print(len(numbers[30]))
