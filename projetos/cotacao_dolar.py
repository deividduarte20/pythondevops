import requests

url = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = url.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]

cotacao_dolar = float(cotacao_dolar)
print(f"O valor em real é: {cotacao_dolar:.2f}")
