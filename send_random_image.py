
import requests 
URL = 'https://dog.ceo/api/breeds/image/random'
response = requests.get(URL).json()
a = response.get('message')
print(a)