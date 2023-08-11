print("---------------------------------------")
print("Questão 1")

lista1 = [1, 2, 3, 4, 5]
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
print(lista1[4])

print("---------------------------------------")
print("Questão 2")

lista2 = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1]
print(lista2[-1])
print(lista2[-2])
print(lista2[-3])
print(lista2[-4])
print(lista2[-5])
print(lista2[-6])
print(lista2[-7])
print(lista2[-8])
print(lista2[-9])
print(lista2[-10])
print(lista2[-11])

print("---------------------------------------")
print("Questão 3")

lista3 = [6.0, 5.9, 7.8, 10.0]
print(lista3)
mem0 = lista3[0]
mem1 = lista3[1]
mem2 = lista3[2]
mem3 = lista3[3]

media = (mem0 + mem1 + mem2 + mem3) / 4
print(media)

print("---------------------------------------")
print("Questão 4 e 5")
numeros = list(range(1, 21))
print(numeros)
print(min(list(range(1, 21))))
print(max(list(range(1, 21))))
del numeros
print("A lista foi apagada!")

print("---------------------------------------")
print("Questão 7,8 e 9")

print("Compras do mes!")

compras1 = (input("Adcione um produto de limpeza na lista:\n"))
compras2 = (input("Adcione um produto de limpeza na lista:\n"))
compras3 = (input("Adcione um produto de limpeza na lista:\n"))
compras4 = (input("Adcione um sorvete na lista:\n"))

listas = []
listas.append(compras1)
listas.append(compras2)
listas.append(compras3)
listas.append(compras4)

print("Voce comprou os produtos de limpeza, parábens!")
listas.remove(compras1)
listas.remove(compras2)
listas.remove(compras3)
print(listas)
print(("Voce comprou um sorvete, parábens!"))
listas.remove(compras4)
print("lista:", listas)

print("---------------------------------------")
print("Questão 10")

def restodiv(x):
    x = x % 2
    if x == 1:
        print("É IMPAR!:", x)
    else:
        print("É PAR!:", x)


print("Digite um numero, e saberemos se ele é par ou impar!")
osu = int(input("Digite aqui:\n"))
restodiv(osu)

print("---------------------------------------")
print("Questão 11")

def inverso(y=[], u=[]):
    len(y)
    len(u)
    if len(y) == len(u):
        print("São um par inverso!")
        print(y, u)
    else:
        print("Não são um par inverso!")
        print(y, u)


print("Digite duas palavras, e veremos se elas são, um par inverso!")

p1 = (input("Digite uma palavra:\n"))
p2 = (input("Digite uma palavra:\n"))

inverso(p1, p2)

print("---------------------------------------")
print("Questão 12")


def imprime_impares(my):
    for num in my:
        if num % 2 != 0:
            print(num, "é um número ímpar")


mylist = (list(range(1, 51)))
print(mylist)
imprime_impares(mylist)
