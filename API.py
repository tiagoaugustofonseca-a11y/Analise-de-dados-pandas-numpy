import requests

url = 'https://dummyjson.com/products'
response = requests.get(url)
data = response.json()
