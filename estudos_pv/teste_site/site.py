import requests

url = 'http://localhost:3001/teste_site/#footer' 
response = requests.get(url)
print(response.status_code)
# print(response.headers)
print(response.text)