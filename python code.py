print("---------------------------------------")
print("Questão 18")
lista = [5.0, 6.9, 7.8, 10.0]
print(lista)
mem0 = lista[0]
mem1 = lista[1]
mem2 = lista[2]
mem3 = lista[3]

media = (mem0 + mem1 + mem2 + mem3) / 4
print(media)
print(min(lista))
print(max(lista))

print("---------------------------------------")
print("Questão 19")

if media >= 7:
    print("APROVADO", media)
if media <= 7:
    media = mem3 / 4
if media >= 5:
    print("APROVADO", media)
else:
    print("REPROVADO", media)

print("---------------------------------------")
print("Questão 20")
frase = ("exercícios de java")
print("exercicios de java")
exe = (input("digite a palavra 'python':\n "))
print("exercícios de ", exe)

print("---------------------------------------")
print("Questão 21")
string = ("exercícios de python")
string = string.upper()
print(string)

print("---------------------------------------")
print("Questão 22")

string2 = "nós estamos aqui presentes"
usu = (input("Digite o caractere que deseja saber a quantidade:\n"))
string2 = string2.count(usu)
print(string2)

print("---------------------------------------")
print("Questão 23")


print(list(range(1, 21)))
print(min(list(range(1, 21))))
print(max(list(range(1, 21))))
