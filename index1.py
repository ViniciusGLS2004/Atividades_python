print("questão 1")
print("O resto da divisão de 10 por 3 é:", 10%3)

print()
print("questão 2")
print("Tabuada de 13:")
cont = 0
for i in range(11):
    print("13 X", cont, " = ", 13*i)
    cont += 1

print("Questão 3:")
meses = int(4)
semanas = int(4)
aulasPorSemana = int(2)
aulasTotais = int(((meses*semanas)*4)/aulasPorSemana) # pode usar o numero 7 por causa dos dias

print("Davir tem ot total", aulasTotais, ".")
print("E tera que comparecer há", int(aulasTotais*8.75))
print("logo, ele só podera faltar", int(aulasTotais*0.25), "aulas")
