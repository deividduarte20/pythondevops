import requests

url = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = url.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]

print(cotacao_dolar)