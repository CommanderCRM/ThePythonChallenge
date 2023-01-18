from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
import os

password_mgr = HTTPPasswordMgrWithDefaultRealm()

password_mgr.add_password(realm=None,
                        uri='http://www.pythonchallenge.com',
                        user='huge',
                        passwd='file')

auth_handler = HTTPBasicAuthHandler(password_mgr)

opener = build_opener(auth_handler)

response = opener.open('http://www.pythonchallenge.com/pc/return/evil2.gfx')

with open("evil2.gfx", "wb") as f:
    f.write(response.read())

print(os.path.getsize("evil2.gfx"))

with open("evil2.gfx", "rb") as f:
    data = f.read()

for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])

os.remove("evil2.gfx")