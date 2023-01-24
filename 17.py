import requests
from bs4 import BeautifulSoup
import urllib.parse
import bz2
import xmlrpc.client

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345"
phonebook = "http://www.pythonchallenge.com/pc/phonebook.php"
cookie_url = "http://www.pythonchallenge.com/pc/stuff/violin.php"

server = xmlrpc.client.ServerProxy(phonebook)
cookies = {"info": "the flowers are on their way"}

info_string = b''

# following the linked list
while True:
  response = requests.get(url)

  info_string += response.cookies["info"].encode('latin-1')

  soup = BeautifulSoup(response.content, 'html.parser')

  text = soup.get_text()

  if "and the next busynothing is" in text:
    number = text.split()[-1]
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={number}"
  else:
    break

# unquoting URL, decoding bz2
unquoted_string = urllib.parse.unquote_to_bytes(info_string)
decoded_string = bz2.decompress(unquoted_string)

# sending XML-RPC to get contact data
response = server.phone("Leopold")

# sending request with cookies to get a response
cookie_response = requests.get(cookie_url, cookies=cookies)
print(cookie_response.content)
