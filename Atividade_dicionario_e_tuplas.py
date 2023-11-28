print("------------------------------------------")
print("Questão 1")
d = {
    "nome": "vinicius",
    "idade": "19 anos",
    "telerone": "9999-9999",
    "endereço": "rua V"
}

nome = d['nome']
print(nome)

print("------------------------------------------")
print("Questão 2")

# nome = (input("Digite seu nome:\n"))
# idade = int(input("Digite sua idade:\n"))
# telefone = int(input("Digite seu telefone:\n"))
# endereco = (input("Digite seu endereço:\n"))
#
#
# d = {
#     "nome" : nome,
#     "idade" : idade,
#     "telefone" : telefone,
#     "endereco" : endereco
# }
#
# print(d)

print("------------------------------------------")
print("Questão 3")
#
# agenda = {}
#
# resp = (input("Deseja inserir imformações?(sim \ nao)\n"))
#
# while resp == "sim":
#     cpf = int(input("Digite seu cpf:\n"))
#     nome2 = (input("Digite o seu nome:\n"))
#     idade2 = int(input("Digite sua idade:\n"))
#     telefone2 = int(input("Digite seu telefone:\n"))
#
#     agenda[cpf] = [nome2, idade2, telefone2]
#
# Remover as pessoas menores de 18 anos do dicionário original usando pop()
# for cpf in list(dic1.keys()):
#     if dic1[cpf][1] < 18:
#         dic2[cpf] = dic1.pop(cpf)

# Usando list() para criar uma cópia da lista de chaves
# for cpf in list(dic1.keys()):
#     if dic1[cpf][1] < 18:
#         dic2[cpf] = dic1.pop(cpf)

#     print(agenda)
#     resp = (input("Deseja inserir imformações?(sim \ nao)\n"))
#
# print("Dados adcionados!")
# print(agenda)

print("------------------------------------------")
print("Questão 4")
#
# dic1 = {}
# dic2 = {}
#
# ress = (input("Deseja inserir imformações?(sim \ nao)\n"))
#
# while ress == "sim":
#
#     cpf2 = int(input("Digite seu cpf:\n"))
#     nome3 = (input("Digite o seu nome:\n"))
#     idade3 = int(input("Digite sua idade:\n"))
#
#     # eu fiz de uma forma mais pratica, onde eu ja separado os dados
#     # das pessoas que tem uma idade menor que 18 anos.
#     # OBS: não é o que o professor pede.
#
#     if idade3 < 18:
#         dic2[cpf2] = [nome3, idade3]
#         print(dic2)
#     else:
#         dic1[cpf2] = [nome3, idade3]
#         print(dic1)
#
#     ress = (input("Deseja inserir imformações?(sim \ nao)\n"))
#
# print("Dados adcionados!")
# print(dic1)
# print(dic2)

print("------------------------------------------")
print("Questão 5")

# em vez de fazer o while com limite de 5, não fazer isso, fazer igual ao anterios
# perguntando se deseja continuar adcionando chaves-valor, ver a questão do limite
# de ate 5, é melhor ver com if e else, mais pratico.

# dic3 = {}
# dic_up = {}
# post = (input("Deseja inserir imformações?(sim \ nao)\n"))
#
# while post == "sim":
#     nome4 = (input("Digite o seu nome:\n"))
#     idade4 = int(input("Digite sua idade:\n"))
#
#     if len(dic3) > 4:
#         dic_up[nome4] = [idade4]
#
#     else:
#         dic3[nome4] = [idade4]
#
#     print(dic3)
#     post = (input("Deseja inserir imformações?(sim \ nao)\n"))
#
# print(dic3)
# print(dic_up)
# # len(dic3)

print("------------------------------------------")
print("Questão 6")

# string2 = "nós estamos aqui presentes"
# usu = (input("Digite o caractere que deseja saber a quantidade:\n"))
# string2 = string2.count(usu)
# print(string2)


# def contador(x):
#     n = 0
#     dicV = {
#         "a": n,
#         "e": n,
#         "i": n,
#         "o": n,
#         "u": n
#     }
#
#     x1 = x.count('a')
#     x2 = x.count('e')
#     x3 = x.count('i')
#     x4 = x.count('o')
#     x5 = x.count('u')
#
#     dicV['a'] = x1
#     dicV['e'] = x2
#     dicV['i'] = x3
#     dicV['o'] = x4
#     dicV['u'] = x5
#     print(dicV)
#
#
# frasex = (input("Digite uma frase, veremos suas vogais:\n"))
# contador(frasex)

# Outra forma mais simples!
# def contador(frase):
#     dicV = {
#         "a": 0,
#         "e": 0,
#         "i": 0,
#         "o": 0,
#         "u": 0
#     }
#
#     for vogal in dicV:
#         dicV[vogal] = frase.count(vogal)
#
#     print(dicV)
#
# frase = input("Digite uma frase, veremos suas vogais:\n")
# contador(frase)


print("------------------------------------------")
print("Questão 7")

boletim = {}

post = (input("Deseja adcionar imformações de alunos?(sim \ nao)\n"))

while post == "sim":

    name = (input("Digite o nome:"))
    if name == "":
        print("programa encerrado!")
        break
    else:
        note1 = float(input("Digite a primeira nota:"))
        note2 = float(input("Digite a segunda nota:"))
        boletim[name] = note1, note2
        print(boletim)
    post = (input("Deseja adcionar imformações de alunos?(sim \ nao)\n"))


def media(dic_boletim):
    for nome, notas in dic_boletim.items():
        nota1, nota2 = notas
        valor_media = (nota1 + nota2) / 2
        print("A média do aluno(a)", nome, "é", valor_media)


print(boletim)
media(boletim)