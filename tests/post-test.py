import requests

url = 'http://192.168.0.108:5000/api/control'
myobj = {
    'vid': 27,
    'steer': 6,
    'mgc' : 43795
}

x = requests.post(url, json = myobj)

print(x.text)

while True:
    pass