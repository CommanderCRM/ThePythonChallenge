import requests
from bs4 import BeautifulSoup, Comment
from collections import Counter

response = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

soup = BeautifulSoup(response.text, "html.parser")

# searching for the most rare symbols in the second comment
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
needed_string = comments[1]
counts = Counter(needed_string)

print(counts)
response.close()