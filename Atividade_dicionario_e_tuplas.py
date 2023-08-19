print("------------------------------------------")
print("Questão 1")
# Crie um dicionário d e coloque nele seus dados: nome, idade,
# telefone,endereço. Usando o dicionário d criado anteriormente, imprima
# seu nome.
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
# Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:
# nome, idade, telefone,endereço. Também usando d, imprima todos os
# itens do dicionário no formato chave : valor, ordenado pela chave.

nome = (input("Digite seu nome:\n"))
idade = int(input("Digite sua idade:\n"))
telefone = int(input("Digite seu telefone:\n"))
endereco = (input("Digite seu endereço:\n"))

d = {
    "nome": nome,
    "idade": idade,
    "telefone": telefone,
    "endereco": endereco
}

print(d)

print("------------------------------------------")
print("Questão 3")
# Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
# chave (cpf), nome, idade, telefone. O programa deve ler um número
# indeterminado de dados, criar a agenda e imprimir todos os itens do
# dicionário no formato chave: nome-idadefone.

agenda = {}

resp = (input("Deseja inserir imformações?(sim \ nao)\n"))

while resp == "sim":
    cpf = int(input("Digite seu cpf:\n"))
    nome2 = (input("Digite o seu nome:\n"))
    idade2 = int(input("Digite sua idade:\n"))
    telefone2 = int(input("Digite seu telefone:\n"))

    agenda[cpf] = [nome2, idade2, telefone2]

    # Remover as pessoas menores de 18 anos do dicionário original usando pop()
    # for cpf in list(dic1.keys()):
    #     if dic1[cpf][1] < 18:
    #         dic2[cpf] = dic1.pop(cpf)

    # Usando list() para criar uma cópia da lista de chaves
    # for cpf in list(dic1.keys()):
    #     if dic1[cpf][1] < 18:
    #         dic2[cpf] = dic1.pop(cpf)

    print(agenda)
    resp = (input("Deseja inserir imformações?(sim \ nao)\n"))

print("Dados adcionados!")
print(agenda)

print("------------------------------------------")
print("Questão 4")
# Crie um programa que cadastre informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um dicionário. Depois remova todas as
# pessoas menores de 18 anos do dicionário e coloque em outro dicionário.

dic1 = {}
dic2 = {}

ress = (input("Deseja inserir imformações?(sim \ nao)\n"))

while ress == "sim":

    cpf2 = int(input("Digite seu cpf:\n"))
    nome3 = (input("Digite o seu nome:\n"))
    idade3 = int(input("Digite sua idade:\n"))

    # eu fiz de uma forma mais pratica, onde eu ja separado os dados
    # das pessoas que tem uma idade menor que 18 anos.
    # OBS: não é o que o professor pede.

    if idade3 < 18:
        dic2[cpf2] = [nome3, idade3]
        print(dic2)
    else:
        dic1[cpf2] = [nome3, idade3]
        print(dic1)

    ress = (input("Deseja inserir imformações?(sim \ nao)\n"))

print("Dados adcionados!")
print(dic1)
print(dic2)

print("------------------------------------------")
print("Questão 5")
# Considere um sistema onde os dados são armazenados em dicionários.
# Nesse sistema existe um dicionario principal e o dicionário de backup.
# Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
# dados na tela e apaga o seu conteúdo. Crie um programa que insira dados
# em um dicionário, realizando o backup a cada dado e excluindo os dados
# do dicionário principal quando ele atingir tamanho 5.

dic3 = {}
dic_up = {}
post = (input("Deseja inserir imformações?(sim \ nao)\n"))

while post == "sim":
    nome4 = (input("Digite o seu nome:\n"))
    idade4 = int(input("Digite sua idade:\n"))

    if len(dic3) > 4:
        dic_up[nome4] = [idade4]

    else:
        dic3[nome4] = [idade4]

    print(dic3)
    post = (input("Deseja inserir imformações?(sim \ nao)\n"))

print(dic3)
print(dic_up)
len(dic3)

print("------------------------------------------")
print("Questão 6")
# Escreva uma função que conta a quantidade de vogais em um texto e
# armazena tal quantidade em um dicionário, onde a chave é a vogal
# considerada.

def contador(x):
    n = 0
    dicV = {
        "a": n,
        "e": n,
        "i": n,
        "o": n,
        "u": n
    }

    x1 = x.count('a')
    x2 = x.count('e')
    x3 = x.count('i')
    x4 = x.count('o')
    x5 = x.count('u')

    dicV['a'] = x1
    dicV['e'] = x2
    dicV['i'] = x3
    dicV['o'] = x4
    dicV['u'] = x5
    print(dicV)


frasex = (input("Digite uma frase, veremos suas vogais:\n"))
contador(frasex)

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
# Escreva um programa que lê duas notas de vários alunos e armazena tais
# notas em um dicionário, onde a chave é o nome do aluno. A entrada de
# dados deve terminar quando for lida uma string vazia como nome.
# Escreva uma função que retorna a média do aluno, dado seu nome.

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

print("------------------------------------------")
print("Questão 8")
# Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
# Escreva um programa que leia todos os tempos em segundos e os guarde
# em um dicionário, onde a chave é o nome do corredor. Ao final diga de
# quem foi a melhor volta da prova e em que volta; e ainda a classificação
# final em ordem (1o o campeão). O campeão é o que tem a menor média
# de tempos.

import random


def gerar_dicionario_quantidade_numeros(chaves, quantidade):
    dic = {}
    for chave in chaves:
        numeros_aleatorios = [random.randint(30, 60) for _ in range(quantidade)]
        dic[chave] = numeros_aleatorios
        media = sum(dic[chave]) / len(dic[chave])
        Mtemp = min(dic[chave])
        print(media)
        print(Mtemp)

    return dic


chaves = ['corredor1', 'corredor2', 'corredor3', 'corredor4', 'corredor5', 'corredor6']
quantidade = 10

dicionario_aleatorio = gerar_dicionario_quantidade_numeros(chaves, quantidade)

print(dicionario_aleatorio)
# O codigo etá imcompleto, não consegui achar uma solução :(