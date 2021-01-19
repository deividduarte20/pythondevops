# try:
#     a = {}
#     print(a[1])
# except NameError as erro:
#     print('Erro do desenvolvedor, fale com ele.')
# except (IndexError, KeyError) as erro:
#     print('Erro de índice.')
# except Exception as erro:
#     print('Ocorreu um erro inesperado')

# print('Continuar...')

def converter_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
while True:
    numero = converter_numero(input('Digite um número: '))

    if numero is None:
        print('Erro: isso não é um número')
    else:
        print(numero * 2)
        break