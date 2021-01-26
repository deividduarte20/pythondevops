import random

chute = 0
chances = 7
tentativas = 1
jogador = ''
# Sistema sorteará um número entre 1 e 100
numero_secreto = random.randint(1,15)

print('#######################################')
print('Bem vindo ao jogo de advinhação')
print('Você terá sete chances para advinhar o número')
print('#######################################')

# programa solicita o nome do jogador
jogador = input('Digite seu nome: ')
print('Chute um número entre 1 e 15')

while tentativas <= 7:
    chute = int(input('Digite o número: '))
    if chute < numero_secreto:
        print('Você errou. Seu número é menor que o sorteado, tente novamente')
        print(f'Tentativa {tentativas} de {chances}')
    elif chute == numero_secreto:
        print('PARABÉNS!!!!, jogador')
        print('Você acertou com %d tentativas' % tentativas)
        tentativas = 8
    else:
        print('Você errou, seu número é maior que o sorteado, tente novamente')
        print('Tentativa %d de %d' % (tentativas, chances))
    
    if tentativas == 6:
        print('Última tentativa')
    elif tentativas == 7:
        print('### Fim de jogo ###')

    tentativas = tentativas + 1
