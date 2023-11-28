# arquivo = open('arquivos.txt', 'r')
# conteudo = arquivo.read(6)
# print(conteudo)
# arquivo.close()


# arquivo = open('arquivos.txt', 'r', )
# linha = "."
# while linha != "":
#     linha = arquivo.readline()
#     print(linha)
#
# print("fim do arquivo")
# arquivo.close()
#

# with open('arquivos.txt', 'r', econding="utf-8") as arquivo:
#     conteudo = arquivo.read()
# print(conteudo)

# arquivo =  with open('arquivos.txt', 'r', econding="utf-8" ) as arquivo:
# linhas = arquivo.readlines()
# for linha in linhas:
#     print(linha)
#
# print("fim do arquivo")
# arquivo.close()


# def gerarlistaordenada():
#     quantidade = int(input("imforme a quantidade elementos:"))
#     arquivo = open('arquivos.txt', 'w')
#
#     for elemento in range(quantidade):
#         arquivo.write(str(elemento) + "\n")
#     arquivo.close()

crescente = open('crescente.txt', 'w')


while crescente > 100:

    print(crescente, ";")
    crescente += 1

crescente.close()