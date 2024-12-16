# API - Application Programming Interface
import requests
import webbrowser

url = "https://random.dog/woof.json"

r = requests.get(url)
print(r.json())

data = r.json()
webbrowser.open(data["url"])