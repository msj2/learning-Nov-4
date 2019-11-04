import requests

session = requests.session()
session.proxies = {}
r = session.get("http://httpbin.org/ip")
print(r.text)
