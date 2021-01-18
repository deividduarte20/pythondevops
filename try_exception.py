try:
    with open('tentativa.txt','r') as file:
        print('Arquivo aberto com sucesso, vamos começar o processamento')
except Exception as err:
    print('Falha ao acessar arquivo')

