import requests

url = 'http://192.168.0.108:5000/api/control'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)
