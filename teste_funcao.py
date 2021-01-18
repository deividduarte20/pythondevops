'''
def qualidade(nome,virtude):
    print(f'O {nome} é {virtude}')

qualidade('Luiz', 'enjoado')
'''

def qualidade(nome,virtude):
    virtudes = f'{nome} é {virtude}'
    return(virtudes)

qualidades = qualidade('Luiz', 'enjoado')
print(qualidades)