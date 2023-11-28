# 1. Classe Triangulo: Crie uma classe que modele
# um triangulo:
# – Atributos: LadoA, LadoB, LadoC
# – Métodos: calcular Perímetro, getMaiorLado;
# Crie um programa que utilize esta classe. Ele deve
# pedir ao usuário que informe as medidas de um
# triangulo. Depois, deve criar um objeto com as
# medidas e imprimir sua área e maior lado.

# class triangulo:
#
#     def __init__(self, ladoA, ladoB, ladoC):
#         self.lado1 = ladoA
#         self.lado2 = ladoB
#         self.lado3 = ladoC
#
#     def perimetro(self):
#         peri = self.lado1 + self.lado2 + self.lado3
#         print(f"O perimetro do triangulo é: {peri}")
#
#     def MaiorLado(self):
#         if self.lado1 > self.lado2 and self.lado1 > self.lado3:
#             print(f"O lado A é o maior lado, com {self.lado1} centimetros")
#         elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
#             print(f"O lado B é o maior lado, com {self.lado2} centimetros")
#         elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
#             print(f"O lado C é o maior lado, com {self.lado3} centimetros")
#         else:
#             print(("Os lados são iguais!"))
#
#
# lado1 = int(input("Digite o primeiro lado do triangulo: "))
# lado2 = int(input("Digite o segundo lado do triangulo: "))
# lado3 = int(input("Digite o terceiro lado do triangulo: "))
# tri = triangulo(lado1, lado2, lado3)
# tri.perimetro()
# tri.MaiorLado()

# 2. Classe Funcionário: Implemente a classe
# Funcionário. Um funcionário tem um nome e um
# salário. Escreva um construtor com dois parâmetros
# (nome e salário) e o método aumentarSalario
# (porcentualDeAumento) que aumente o salário do
# funcionário em uma certa porcentagem. Exemplo de
# uso:
# harry=funcionário("Harry",25000)
# harry.aumentarSalario(10)
# Faca um programa que teste o método da classe.

# class Funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.salario = salario
#
#     def aumentarSalario(self, percentualDeAumento):
#         conta = (self.salario * percentualDeAumento)/100
#         self.salario += conta
#         print(f"O Aumento do salario do funcionario é de {self.salario} ")
#
# nome = (input("Digite o nome do funcionario:\n"))
# salario = int(input("Digite o salario do funcionario:\n"))
# funcionario = Funcionario(nome, salario)
# print(f"O nome do funcionario é {nome}, e o seu salrio é {salario} R$")
# percent = int(input("Digite o aumento do salario pela porcentagem:\n"))
# funcionario.aumentarSalario(percent)

# 3. Crie uma classe Livro que possui os
# atributos nome, qtdPaginas, autor e preço. – Crie os métodos getPreco para obter o valor
# do preco e o método setPreco para setar
# um novo valor do preco.
# Crie um codigo de teste

class Livro:
    def __init__(self, nome, qtdpaginas, autor, preco):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        print(f"O atual preço do livro é de {self.preco}")

    def setPreco(self, newP):
        oldP = self.preco
        self.preco = newP
        print(f"O preço do livro foi modificado de {oldP} para {self.preco} R$")


nome = (input("Digite o nome do livro:\n"))
qtdpaginas = int(input("Digite a quantidades de paginas no livro:\n"))
autor = (input("Digite o nome do autor do livro:\n"))
preco = float(input("Digite o preço do livro:\n"))

book = Livro(nome, qtdpaginas, autor, preco)
print(f"O nome do livro é {nome}, tem {qtdpaginas} paginas, seu autor é {autor} e seu preço é de {preco} R$ ")
book.getPreco()
novoP = float(input("Digite o novo preço do livro:\n"))
book.setPreco(novoP)

