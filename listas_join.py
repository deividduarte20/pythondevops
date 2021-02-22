cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
# Pode inverter para valores vir antes das cores
# duas_listas = zip(valores, cores)
# Função zip junta listas porém para imprimir temos que usar a função list()
print(list(duas_listas))

