nome = 'Silvio Santos '
canto1 = 'vem ai, '
canto2 = 'lá '

print(nome + canto1 + canto2 * 6 + "!!\n")

nome2 = "texto bonito "

print(nome2 * 3)
print(nome2)

palavra = "sucumba"
print(len(palavra))  # TODO: É assim que funciona o len
print(palavra[0])  # TODO: para mostrar tudo imformação tem que ter um print, diferente do terminal
print(palavra[5])

frase = "Aprender python é meia boca"
print(frase[0:17])  # do zero até o 5
print(frase[:])  # escreve tudo
print(frase[7:])  # se emitir o segundo indice significa "obter ate o fianl"
print(frase[:7])  # se emitir o primeiro indice significa "obter desde o começo"

# pessoa = input("Digite seu nome:\n")
# imfo = "olá, {}".format(pessoa)
# print(imfo)

# Outra forma é: print("olá,", pessoa)


call = '{} * {} = {}'.format(7, 6, 7 * 6)
print(call)

palavra2 = "python"
numero = 10
booleano = False
mentira = '{} é {}. E as outras Linguagens? {}'.format(palavra2, numero, booleano)
print(mentira)

frase2 = "Slvio santos vem ai, oleoleolá"
print(frase2[:6])
print(frase2[6:13])
print(frase2[13:21])
print(frase2.split())
print("---------------------------------------")
print("Exercício 1\n")
frase3 = "Python é muito legal."

joy1 = frase3[0:6]
joy2 = frase3[7:9]
joy3 = frase3[9:14]
joy4 = frase3[15:]
print(joy1)
print(joy2)
print(joy3)
print(joy4)

print("---------------------------------------")
print("Exercício 2\n")
print(len(frase3))
print(len(joy1))
print(len(joy2))
print(len(joy3))
print(len(joy4))

print("---------------------------------------")
print("Exercício 3\n")

frase4 = "Python é muito legal."
print(frase4.split())

print("---------------------------------------")
print("Imverter valores")
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

print("---------------------------------------")
print("comentario aqui para não me atrapalhar")
# idade = input("Digite sua idade:\n")
# altura = input("Digite sua altura:\n")
# print(idade," Anos e ",altura," de altura")
# type

print("---------------------------------------")

a = 7
if a > 3:
    print("estou no if")
else:
    print("Estou no else")

print("---------------------------------------")
print("Exercício 4\n")

a = 5
b = 9
if b <= a:
    print("b tem o valor menor")
else:
    print("a tem o valor menor")

print("---------------------------------------")
print("Exercício 5\n")

# idade = int(input("Digite sua idade:\n"))
# peso = int(input("Digite seu peso:\n"))
# descanso = int(input("Digite suas horas dormidas:\n"))

# if idade >= 16 and peso >= 50 and descanso >= 6:
#   print("Voce pode doar sangue")
# else:
#   print("Voce não pode doar sangue")

print("---------------------------------------")
print("Exercício 6\n")
# num1 = int(input("Digite um numero:\n"))
# num2 = int(input("Digite um numero:\n"))
# numT = num1 + num2
# if numT >= 20:
#   numT += 8
#    print("O valor é:", numT)
# else:
#    numT -= 5
#    print("O valor é:", numT)
print("---------------------------------------")
# laço FOR: aqui repetimos o print 3 vezes
for n in range(0, 3):
    print(n)
# Laço WHILE: Aqui iniciamos o n em 0, e repetimos o print até que seu valor seja maior ou igual a 3.
n = 0
while n < 3:
    print(n)
    n += 1

lista = list(range(0, 3))  # TODO: atribuir sempre uma variavel para uma classe
print(lista)

# Para cada letra na palavra, imprimir a letra
palavra4 = "diacono"
for letra in palavra4:
    print(letra)

print("---------------------------------------")
print("Exercício 7\n")

n = list(range(0, 5))
print(n)

m = 5
while m > 0:
    print(m)
    m -= 1

lista = ['a', 'c', 'e', 'b', 'd']
lista.sort()
print(lista)

lista = ['a', 'c', 'e', 'b', 'd']
lista.sort(reverse=True)
print(lista)

print("---------------------------------------")
print("Exercício 7\n")

# nume1 = int(input("Digite um numero Inteiro:\n"))
# nume2 = int(input("Digite um numero inteiro:\n"))
# nume3 = float(input("Digite um numero Real:\n"))

# Qa = nume1**2
# print(Qa)

print("---------------------------------------")
print("Aprendendo lista\n")

lista = [2, 34, 19, "wild rift", 5, 91, 7]
print(lista)
lista[0] = 1
print(lista)

lista[-1] = "teste"
print(lista)
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-3])
print(lista[-4])
print(19 in lista)
print("odeiolol" in lista)
print(len(lista))
del lista[2]
print(lista)
del lista[-1]
print(lista)

lista2 = ["aqua", "ruby"] * 2
list = lista + lista2
print(list)

list = [1, 34, 'wild rift', 5, 91, 'aqua', 'ruby', 'aqua', 'ruby']
list.append('e')
print(list)
list.insert(0, 'eita')
print(list)

listD = [1, 3, 5, 8, 2, 4]
listD.sort()
print(listD)

listF = ['aqua', 'ronaldo', 'junjiito', 'ruby']
listF.sort()
print(listF)

listF = listD.copy()
print(listF)

print("---------------------------------------")
print("Função range()")

# Create a list in a range of 10-20
My_list = [*range(1, 200)]

# Print the list
print(My_list)

print("---------------------------------------")
print("Funções")


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

media = (mem0 + mem1 + mem2 + mem3)/4
print(media)

print("---------------------------------------")
print("Questão 4")

for n in range(1, 21):
    print(n)

    

    print("O maior numero é: ",  )


