veiculoplaca = []
veiculomarca = []
veiculomodelo = []
veiculoano = []
veiculocod = []

def addVeiculo():
    veiculoplaca.append(input('Digite a placa: '))
    veiculomarca.append(input('Digite a marca: '))
    veiculomodelo.append(input('Digite o modelo: '))
    veiculoano.append(input('Digite o ano: '))
    veiculocod.append(input('Digite o código: '))

def removeVeiculo():
    veiculoremovido = input('Digite a placa do veículo:')
    if veiculoremovido in veiculoplaca:
        veiculoplaca.remove(veiculoremovido)
        print("Veículo removido com sucesso.")
    else:
        print('Descuple, esta placa não existe.')

def imprimeVeiculo():
    veiculoconsultado = input("Digite a placa do veículo que você quer consultar: ")
    if veiculoconsultado in veiculoplaca:
        print('''A placa deste carro é: {}.
         Marca: {}.
         Modelo:{}.
         Ano: {}.
         Código: {}.'''.format(veiculoplaca,veiculomarca,veiculomodelo,veiculoano, veiculocod))
    else:
        print('Descuple, esta placa não existe.')




menu = 0
while menu < 4:
    print('Menu:')
    print('''
    1. Inserir um veículo na lista
    2. Remover um veículo da lista
    3. Consultar Cadastro (Digite a placa do veículo que você deseja consultar)
    4. Finalizar o programa''')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        addVeiculo()
    elif menu == 2:
        removeVeiculo()
    elif menu == 3:
        imprimeVeiculo()
    else:
        print('Programa Finalizado')