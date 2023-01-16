import requests
from bs4 import BeautifulSoup

nothing_values = []
nothing_values_after_division = []

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
div_result = str(int(16044/2))
url_after_division = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={div_result}"

nothing_values.append('12345')
nothing_values_after_division.append(div_result)
print(url_after_division)

while True:
  response = requests.get(url_after_division)

  soup = BeautifulSoup(response.content, 'html.parser')

  text = soup.get_text()

  if "and the next nothing is" in text:
    number = text.split()[-1]
    nothing_values_after_division.append(number)
    url_after_division = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}"
  else:
    break

print(nothing_values_after_division)