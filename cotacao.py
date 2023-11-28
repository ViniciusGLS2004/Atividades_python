print("Questão 1")
print("A cotação dos reais para dolar seria:", 65.00//3.50, "Reais")

print("Questão2")
cell = 300.00
cha= 23.87
gin = 66.66
ade = 1.42*6
frete = 12.34
TotalUSD = cell+cha+gin+ade+frete

TotalReais = TotalUSD//3.25
IOF = 6.38/10
TotalReaisIOF = TotalReais*IOF

print("A soma total dos itens é:",round(TotalUSD,2))
print("O Total para reais é:", TotalReais)
print("O Total para reais com IOF é:", TotalReaisIOF)