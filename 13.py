import xmlrpc.client

# XML-RPC request is needed
url = "http://www.pythonchallenge.com/pc/phonebook.php"
server = xmlrpc.client.ServerProxy(url)

response = server.phone("Bert")

print(response)
