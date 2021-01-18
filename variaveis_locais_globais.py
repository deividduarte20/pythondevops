EMPRESA = 'JLCP'

def imprima_nome():
    nome = 'Robert'
    global EMPRESA
    EMPRESA = 'Python Devops'
    print(f'O {nome} trabalha na {EMPRESA}')

imprima_nome()
print(EMPRESA)