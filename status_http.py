import requests

# Solicita URL a ser verificada
url = input("Digite a url: ")

# Efetua o request do status http
request = requests.get(url)
print(request.status_code)