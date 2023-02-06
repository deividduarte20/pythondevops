# Sistema calculo de consumo de energia

horas = int(input("Quantas horas por dia usará o ar condicionado? "))

dia_mes = int(input("Quantos dias por mês? "))

selo_procel = float(input("Qual o valor do selo procel? "))

calculo = horas * dia_mes * selo_procel / 30
print(f"O valor de consumo por mês é {calculo:.2f} kWz")