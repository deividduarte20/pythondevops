# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'



def somar(x):
    fun2 = lambda x: x + 10
    return fun2(x) * 4

print(somar(2))