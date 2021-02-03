'''
Criar um programa que calcula a quantidade de tinta necessária para pintar
uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
Uma lata de tinta pinta 5 metros quadrado
Calculo:
Altura * Largura = Metros quadrados / pelo rendimento da lata
'''

def pintura():
    rendimento = int(input('Qual é o rendimento da lata? '))
    altura = float(input('Qual a altura da parede? '))
    largura = float(input('Qual a largura da parede? '))
    resultado = (altura * largura) / rendimento
    return f'Você precisa de {resultado} latas de tinta'

print(pintura())









