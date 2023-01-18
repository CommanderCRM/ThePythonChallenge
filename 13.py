import xmlrpc.client

url = "http://www.pythonchallenge.com/pc/phonebook.php"
server = xmlrpc.client.ServerProxy(url)

response = server.phone("Bert")

print(response)
