def divisao(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print('Forneça um número diferente de zero!')
    except TypeError:
        print('Forneça um número')
    finally:
        print('Será executado de qualquer forma')

resultado = divisao(12,2)
print(f'O resultado da divisão é {resultado}')