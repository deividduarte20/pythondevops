import requests

# Função que obtem habilidades do pokemon
def pegar_habilidades(url):
    print(f'Habilidades do {animal}:')
    for i in url['abilities']:
        print(i['ability']['name'])

# Consumindo api pokemon
pokemon = input("Digite o nome Pokemon: ")
animal = pokemon.lower()
if pokemon != str():
    print("Valor inválido")
url = requests.get(f"https://pokeapi.co/api/v2/pokemon/{animal}")
poke = url.json()
pegar_habilidades(poke)