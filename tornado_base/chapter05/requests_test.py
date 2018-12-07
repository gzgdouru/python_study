import requests

response = requests.post("http://127.0.0.1:8888",  json={"name":"ouru"})
print(response.text)