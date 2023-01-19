import requests
from bs4 import BeautifulSoup, Comment
import re

response = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")

soup = BeautifulSoup(response.text, "html.parser")

comments = soup.find_all(string=lambda text: isinstance(text, Comment))
needed_string = comments[0]

# searching for xXXXxXXXx pattern in the first comment
pattern = re.compile(r'([a-z][A-Z]{3}[a-z][A-Z]{3}[a-z])')
matches = pattern.findall(needed_string)
for match in matches:
  print(match)

response.close()