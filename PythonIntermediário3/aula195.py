# requests para requisições HTTP
import requests

url = 'http://localhost:3000/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)