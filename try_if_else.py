# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor númerico')
finally:
    print('Código ok')


# else:
#     print('Usuário digitou um valor correto')
#     resultado = valor * 2
#     print(resultado)