# def boas_vindas():
#     print('Olá Deivid!')
#     print('Temos 5 laptops em estoque')

# boas_vindas()

# def somar_dois_numeros():
#     numero1 = 10
#     numero2 = 5
#     resultado = numero1 + numero2
#     print(resultado)


# somar_dois_numeros()

# def boas_vindas(nome,quantidade):
#     print(f'Olá {nome}.')
#     print(f'Temos {quantidade} laptops em estoque')

# boas_vindas('Maria', 4)

# Argumento que define valor é default
# Argumento sem valor é não default

# def boas_vindas(nome,quantidade=6):
#     print(f'Olá {nome}.')
#     print(f'Temos {quantidade} laptops em estoque')

# boas_vindas('Maria')

# Functions (Funções)
    # DRY - Don't repeat youself
    # Realizam uma tarefa
    # Calcula e retorna um valor

def cliente1(nome):
    print(f'Olá {nome}')

cliente1('Maria')

def cliente2(nome):
    return f'Olá {nome}'

print(cliente2('José'))