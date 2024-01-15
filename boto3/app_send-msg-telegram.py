import requests

# https://api.telegram.org/bot{{TOKEN}}/getUpdates

bot_token = '1234567890:AAE0-ysx15fZ1P8J1jjjiWBKI5dpfh5ahwp' # Token inválido apenas para exemplo
id_canal = '-331008769490' # Id de grupo inválido apenas para exemplo

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

resposta = requests.post(
    api_url,
    json={
	"chat_id": id_canal,
	"text": "Olá, eu sou o AWS Bot via python"
	}
)
    
# Outro metodo de envio de mensagem
# msg = 'Mensagem via python'
 
# URL = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id_canal}&text={msg}'
 
# resposta = requests.post(URL)
# print(resposta.json())