# consumer.py
import requests

response = requests.get('http://127.0.0.1:5000/')
data = response.json()

print("Data from RESTful API:")
print(data)
