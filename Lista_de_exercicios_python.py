# 1. Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class bola:
    def __init__(self, cor, circunstancia, material):
        self.cor = cor
        self.circunstancia = circunstancia
        self.material = material

    def Trocacor(self, troca):
        self.cor = troca

    def mostracor(self):
        print("A cor atual é:", self.cor)

cor = (input("Digite a cor da boa:\n"))
circu = int(input("Digite a circunstancia da bola:\n"))
material = (input("Digite o material da bola:\n"))

futebol = bola(cor, circu, material)
print(f"A bola ter a cor {futebol.cor}, sua circunstancia é {futebol.circunstancia} e seu material é {futebol.material}.")
troca = (input("Digite a nova cor da bola:\n"))
futebol.Trocacor(troca)
print(f"A nova cor da bola é {futebol.cor}")
futebol.mostracor()

# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def Mudarlado(self, nlado):
        self.lado = nlado

    def Retornalado(self):
        print(f"O lado atual do quadrado é de {self.lado} centimetros!")

    def Areaquad(self):
        self.lado = self.lado ** 2
        print(f"A Área do quadrado, é de {self.lado} centimetros²")


lado = int(input("Digite o valor de um lado de um quandrado:\n"))
quadrado = Quadrado(lado)
Nlado = int(input("Digite um novo valor ao lado de um quadrado:\n"))
quadrado.Mudarlado(Nlado)
quadrado.Retornalado()
quadrado.Areaquad()


# 3. Classe Retângulo: Crie uma classe que modele um retângulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura,
# a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área
# e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
# informe as medidas de um local. Depois, deve criar um objeto com as
# medidas e calcular a quantidade de pisos e de rodapés necessárias para
# o local.

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.base = ladoA
        self.altura = ladoB

    def Mudarlado(self, nbase, naltura):
        self.base = nbase
        self.altura = naltura

    def Retornalado(self):
        print(f"A base do retangulo é de {self.base} centimetros!")
        print(f"A altura do retangulo é de {self.altura} centimetros!")

    def Area_retangulo(self):
        AreaTl = self.base * self.altura
        print(f"A Área do retangulo, é de {AreaTl} centimetros²")
        return AreaTl  # Retorna o valor da área

    def Perimetro(self):
        peri = 2 * (self.base + self.altura)
        print(f"O perimetro do retangulo, é de {peri} centimetros")


base = int(input("Digite o valor da comprimento do ambiente:\n"))
altura = int(input("Digite o valor da largura do ambiente:\n"))
AreaT = base * altura
print(f"A Area do ambiente é de {AreaT} metros")

lado1 = int(input("Digite o valor da comprimento do piso:\n"))
lado2 = int(input("Digite o valor da largura do piso:\n"))
retangulo = Retangulo(lado1, lado2)
area_piso = retangulo.Area_retangulo()
print(f"Valor da área do piso é de {area_piso} centimetros²")

qtd_pisos = AreaT / area_piso
print(f"Eu precisaria de {qtd_pisos:.2f} pisos, para prencher a Área do ambiente!")

Peri_ambiente = 2 * (base + altura)
print(f"O perimetro do Ambiente seria de {Peri_ambiente} metros")
tamanho_do_rodape = int(input("Digite o tamanho do rodape:\n"))
quantidade_rodapes = AreaT / tamanho_do_rodape
print(f"Eu precisaria de {quantidade_rodapes} rodapes, para prencher a Área do ambiente")


# 4. Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão,
# a cada ano que nossa pessoa envelhece, sendo a idade dela menor que
# 21 anos, ela deve crescer 0,5 cm.
#
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Emvelhecer(self, id1):
        if id1 > self.idade:
            self.idade = id
            print(f"A idade aumentou para {self.idade} e a pessoa ficou mais velha")
            return self.idade
        else:
            print("A pessoa não envelheceu!")

    def Engordar(self):
        self.peso += 0.5 * self.idade
        print(f"O peso da pessoa aumentou para {self.peso} kilogramas ")
        return self.peso

    def Emagrecer(self, id3):
        if id3 < self.idade:
            self.peso -= 1.5
            print(f"O peso da pessoa diminuiu para {self.peso} kilogramas ")
            return self.peso
        else:
            print("A pessoa não emagreceu!")
    def Crescer(self, id4):
        if id4 <= 21:
            self.altura = self.altura + 0.5
            print(f"A pessoa agora tem {self.altura} centimentros de altura")
        else:
            print(f"a pessoa continua com a altura de {self.altura} centimentos!")


nome = (input("Digite o nome da pessoa:\n"))
idade = int(input("Digite a idade da pessoa:\n"))
peso = float(input("Digite o peso da pessoa:\n"))
altura = float(input("Digite a altura da pessoa:\n"))

pessoa = Pessoa(nome, idade, peso, altura)

resp = (input("Deseja gigitar uma nova idade da pessoa?(sim \ nao):\n"))
while resp == "sim":

    id = int(input("Digite uma nova idade da pessoa:\n"))
    pessoa.Emvelhecer(id)
    pessoa.Engordar()
    pessoa.Emagrecer(id)
    pessoa.Crescer(id)

    resp = (input("Deseja digitar uma nova idade da pessoa?(sim \ nao):\n"))

print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nPeso: {pessoa.peso}\nAltura: {pessoa.altura}")


# 5. Classe Conta Corrente: Crie uma classe para implementar uma conta
# corrente. A classe deve possuir os seguintes atributos: número da conta, nome
# do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
# saque; No construtor, saldo é opcional, com valor default zero e os demais
# atributos são obrigatórios.

class Conta_Corrente:
    def __init__(self, num_conta, name_correntista, saldo):
        self.conta = num_conta
        self.corrente = name_correntista
        self.saldoop = saldo

    def alterarNome(self, new):
        self.corrente = new
        print(f"Nome atualizado!, olá, {self.corrente}")

    def Deposito(self, dep):
        self.saldoop = self.saldoop + dep
        print(f"A sua conta tem {self.saldoop} Reais")

    def Saque(self, saq):
        if self.saldoop < saq:
            print("Voce não tem saldo nesta conta!")
        else:
            self.saldoop = self.saldoop - saq
            print(f"Voce retirou {saq} reais da sua conta")
            print(f"A sua conta tem {self.saldoop} reais no momento")


conta = int(input("Digite o numero da sua conta:\n"))
nome = (input("Digite o seu nome:\n"))
re = (input("Deseja adcionar um saldo?(sim \ nao)"))

if re == "sim":
    saldo = int(input("Digite o seu saldo:\n"))
else:
    saldo = 0

conta_corrente = Conta_Corrente(conta, nome, saldo)

res = (input("Deseja modificar os seus dados?(sim \ nao)"))

while res == "sim":
    resp = (input("Qual ação voce quer fazer em seus dados?(nome \ depositar \ saque )\n"))

    if resp == "nome":
        nome = (input("Digite um novo nome:\n"))
        conta_corrente.alterarNome(nome)

    elif resp == "depositar":
        saldo = int(input("Digite a quantidade do deposito:\n"))
        conta_corrente.Deposito(saldo)

    else:
        saque = int(input("Digite o valor que voce quer sacar:\n"))
        conta_corrente.Saque(saque)

    res = (input("Deseja modificar os seus dados?(sim \ nao)"))

print(f"Numero da conta: {conta_corrente.conta}\nNome: {conta_corrente.corrente}\n"
      f"Saldo: {conta_corrente.saldoop}")

# 6. Classe TV: Faça um programa que simule um televisor criando-o como um
# objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou
# diminuir o volume. Certifique-se de que o número do canal e o nível do volume
# permanecem dentro de faixas válidas.

class TV:
    def __init__(self, numero_canal, numero_volume):
        self.canal = numero_canal
        self.volume = numero_volume

    def ajustarVolume(self, vol):
        if vol < 0 or vol > 100:
            print(f"O volume informado não existe!")
        else:
            self.volume = vol
            print(f"O volume atual da tv é {self.volume}")

    def MudarCanal(self, call):
        if call < 1 or call > 99:
            print(f"O canal informado não existe!")
        else:
            self.canal = call
            print(f"O canal da TV foi modificado para {self.canal}")

while True:
    canal = int(input("Digite o número do canal (1 a 99):\n "))
    volume = int(input("Digite o volume da TV (0 a 100):\n "))

    if canal < 1 or canal > 99:
        print("Erro: O número do canal deve estar entre 1 e 99.")
    elif volume < 0 or volume > 100:
        print("Erro: O volume deve estar entre 0 e 100.")
    else:
        break  # Sai do loop se as entradas estiverem corretas

print("Canal e volume válidos.")


tv = TV(canal, volume)
mod = (input("Deseja mudar augo da televisão?(sim \ nao)"))

while mod == "sim":
    resp = (input("Qual ação voce quer fazer na televisão?( canal \ volume )\n"))

    if resp == "canal":
        canal = int(input("Digite um novo canal:\n"))
        tv.MudarCanal(canal)

    elif resp == "volume":
        volume = int(input("Digite o novo volume da TV:\n"))
        tv.ajustarVolume(volume)

    mod = (input("Deseja mudar augo da televisão?(sim \ nao)"))

print(f"Numero da canal: {tv.canal}\nNumero do volume: {tv.volume}\n")

# 7. Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho
# Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome,
# Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
#
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor
# do nosso tamagushi, este humor é uma combinação entre os atributos Fome e
# Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
# armazenar esta informação por que ela pode ser calculada a qualquer momento.


class Tamaguchi:

    def __init__(self, Nome, Fome, Saude, Idade):
        self.nome = Nome
        self.fome = Fome
        self.saude = Saude
        self.idade = Idade

    def AlterarNome(self, name):
        self.nome = name
        print(f"Nome atualizado!, olá, {self.nome}")

    def AlterarFome(self, hungry):
        if hungry == 0:
            self.fome = hungry
        elif hungry == 1:
            self.fome = hungry
            print("O seu tamagotchi está com muita fome!")
        elif hungry == 2:
            self.fome = hungry
            print("O seu tamagotchi está com fome!")
        elif hungry == 3:
            self.fome = hungry
            print("O seu tamagotchi está satisfeito!")
        elif hungry == 4:
            self.fome = hungry
            print("O seu tamagotchi está muito satisfeito!")

    def AlterarSaude(self, life):
        if life == 0:
            self.saude = life
        if life == 1:
            self.saude = life
            print("O seu tamagotchi está com pouca saude!")
        elif life == 2:
            self.saude = life
            print("O seu tamagotchi está com saude mediana!")
        elif life == 3:
            self.saude = life
            print("O seu tamagotchi está com saude!")
        elif life == 4:
            self.saude = life
            print("O seu tamagotchi está com muita saude!")

    def AlterarIdade(self, age):
        if age == 0:
            self.idade = age
            print("O seu tamagotchi é um ovo!")
        if age == 1:
            self.idade = age
            print("O seu tamagotchi é um bebe!")
        elif age == 2:
            self.idade = age
            print("O seu tamagotchi é uma criança!")
        elif age == 3:
            self.idade = age
            print("O seu tamagotchi adolescente!")
        elif age == 4:
            self.idade = age
            print("O seu tamagotchi é um adulto!")

    def Humor(self):
        if self.fome == 0 or self.saude == 0:
            return "O seu tamagotchi morreu!"
        elif self.fome == 1 or self.saude == 1:
            return "O seu tamagotchi não esta feliz"
        elif self.fome == 2 or self.saude == 2:
            return "O seu tamagotchi esta um pouco feliz"
        elif self.fome == 3 or self.saude == 3:
            return "O seu tamagotchi esta feliz"
        elif self.fome == 4 or self.saude == 4:
            return "O seu tamagotchi esta muito feliz"


nome = (input("Digite o nome do seu tamagotchi:\n"))

while True:
    fome = int(input("Digite o nivel da fome do seu tamagotchi(de 1 a 4):\n"))
    saude = int(input("Digite o nivel da saude do seu tamagotchi(de 1 a 4):\n"))
    idade = int(input("Digite a idade do seu tamagotchi(1 a 4):\n"))

    if fome < 1 or fome > 4:
        print("Erro: O nivel da fome do tamagotchi deve estar entre 1 e 4.")
    elif saude < 1 or saude > 4:
        print("Erro: O nivel de saude do tamagotchi deve estar entre 1 e 4.")
    elif idade < 0 or idade > 4:
        print("Erro: A idade do tamagotchi deve estar entre 0 e 4.")
    else:
        break  # Sai do loop se as entradas estiverem corretas

print("Canal e volume válidos.")

tamaguchi = Tamaguchi(nome, fome, saude, idade)

tama = (input("Deseja mudar augo no seu tamaguchi?(sim \ nao)"))

while tama == "sim":
    tamachi = (input("Qual ação voce quer fazer no seu tamagotchi?( nome \ fome \ saude \ idade )\n"))

    if tamachi == "nome":
        nome = (input("Digite um novo nome para o seu tamagotchi:\n"))
        tamaguchi.AlterarNome(nome)

    elif tamachi == "fome":
        fome = int(input("Digite o nivel de fome do seu tamagotchi:\n"))
        if fome != 0:
            tamaguchi.AlterarFome(fome)
        else:
            tamaguchi.AlterarFome(fome)
            print("O tamagotchi morreu!")
            break
    elif tamachi == "saude":
        saude = int(input("Digite o nivel de saude do seu tamagotchi:\n"))
        if saude != 0:
            tamaguchi.AlterarSaude(saude)
        else:
            tamaguchi.AlterarSaude(saude)
            break
    elif tamachi == "idade":
        idade = int(input("Digite a idade do seu tamagotchi:\n"))
        tamaguchi.AlterarIdade(idade)

    tama = (input("Deseja mudar augo no seu tamaguchi?(sim \ nao)"))

print(f"Nome: {tamaguchi.nome}\nFome: {tamaguchi.fome}\nSaude: {tamaguchi.saude}\nIdade: {tamaguchi.idade}\nHumor: {tamaguchi.Humor()}")

# 8. Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos
# nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e
# digerir(). Faça um programa ou teste interativamente, criando pelo menos dois
# macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
# o conteúdo do estomago a cada refeição.
# Experimente fazer com que um macaco coma o outro. É possível criar um
# macaco canibal?

class Macaco:

    def __init__(self, nome, estomago):
        self.nome = nome
        self.bucho = []
        self.bucho.append(estomago)

    def comer(self, comida):
        self.bucho.append(comida)
        print(f"O macaco comeu {comida}")

    def VerBucho(self):
        print(f"O macaco comeu {self.bucho}")

    def Digerir(self):
        self.bucho.clear()
        print("Alimentos digeridos, não ha nada no estomago!")


nome1 = (input("Digite o nome do macaco1:\n"))
panca1 = (input("De um alimento para o macaco1:\n"))

macaco1 = Macaco(nome1, panca1)
macaco1.VerBucho()
eat1 = (input("Deseja fazer augo para o macaco1?(sim \ nao)\n"))
while eat1 == "sim":
    opc1 = (input("Deseja alimentar ou digerir o estomago do macaco1?(alimentar \ digerir)\n"))
    if opc1 == "alimentar" and len(macaco1.bucho) < 3:
        panca1 = (input("De um alimento para o 1:\n"))
        macaco1.comer(panca1)
        macaco1.VerBucho()
    elif opc1 == "digerir":
       macaco1.Digerir()
    else:
        print("O estomago do macaco1 está cheio!")
        break
    eat1 = (input("Deseja fazer augo para o macaco1?(sim \ nao)"))

print(f"Nome: {macaco1.nome}\nEstomago: {macaco1.bucho}")

nome2 = (input("Digite o nome do macaco2:\n"))
panca2 = (input("De um alimento para o macaco2:\n"))

macaco2 = Macaco(nome2, panca2)
macaco2.VerBucho()
eat2 = (input("Deseja fazer augo para o macaco2?(sim \ nao)\n"))
while eat2 == "sim":
    opc2 = (input("Deseja alimentar ou digerir o estomago do macaco2?(alimentar \ digerir)\n"))
    if opc2 == "alimentar" and len(macaco2.bucho) < 3:
        panca2 = (input("De um alimento para o macaco2:\n"))
        macaco2.comer(panca2)
        macaco2.VerBucho()
    elif opc2 == "digerir":
       macaco2.Digerir()
    else:
        print("O estomago do macaco2 está cheio!")
        break
    eat2 = (input("Deseja fazer augo para o macaco?(sim \ nao)"))

print(f"Nome: {macaco2.nome}\nEstomago: {macaco2.bucho}")

if len(macaco1.bucho) == 0:
    print("O macaco 1 comeu o macaco 2")
elif len(macaco2.bucho) == 0:
    print("O macaco 2 comeu o macaco 1")

# 9. Classe Ponto e Retângulo: Faça um programa completo utilizando funções e
# classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y.
# b. Possua uma classe chamada Retângulo, com os atributos largura e
# altura.
# c. Possua uma função para imprimir os valores da classe Ponto
# d. Possua uma função para encontrar o centro de um Retângulo.
# e. Você deve criar alguns objetos da classe Retângulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice
# inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor
# para um objeto do tipo ponto que indique os valores de x e y para o centro
# do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro
# deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Imprimir(self):
        print(f"A classe ponto tem como cordenada x como {self.x:.2f} e cordenada y como {self.y:.2f}")


class Retangulo:
    def __init__(self, ponto_inferior_esquerdo, largura, altura):
        self.ponto_inferior_esquerdo = ponto_inferior_esquerdo
        self.largura = largura
        self.altura = altura

    def Centro_retangulo(self):
        # Calcula o centro do retângulo usando as coordenadas do ponto inferior esquerdo
        centro_x = self.ponto_inferior_esquerdo.x + self.largura / 2
        centro_y = self.ponto_inferior_esquerdo.y + self.altura / 2
        return centro_x, centro_y


x = float(input("Digite o valor de X do vertice inferior esquerdo:\n"))
y = float(input("Digite o valor Y do vertice inferior esquerdo:\n"))
largura = float(input("Digite a largura do retangulo:\n"))
altura = float(input("Digite a altura do retangulo:\n"))

vertice_imferior_esquerdo = Ponto(x, y)
vertice_imferior_esquerdo.Imprimir()
retangulo = Retangulo(vertice_imferior_esquerdo, largura, altura)

alt = (input("Deseja fazer auguma alteração no retangulo? (sim \ nao):\n"))
while alt == "sim":
    alte = input(("O que voce deseja mudar? (largura ou altura):\n"))

    if alte == "largura":
        largura = float(input("Digite a nova largura do retangulo:\n"))
        retangulo.largura = largura

    elif alte == "altura":
        altura = float(input("Digite a nova altura do retangulo:\n"))
        retangulo.altura = altura

    alt = (input("Deseja fazer auguma alteração no retangulo? (sim \ nao):\n"))
print(f" A largura do retangulo é {retangulo.largura} e a altura é {retangulo.altura}")
centro_x, centro_y = retangulo.Centro_retangulo()

print(f"O centro do retângulo está nas coordenadas ({centro_x}, {centro_y})")

# 10. Classe Bomba de Combustível: Faça um programa completo utilizando
# classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo
# esses atributos:
# i. tipoCombustivel.
# ii. valorLitro
# iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:
#
# i. abastecerPorValor( ) – método onde é informado o valor a ser
# abastecido e mostra a quantidade de litros que foi colocada no
# veículo
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em
# litros de combustível e mostra o valor a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de
# combustível restante na bomba.
#
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a
# quantidade de combustível total na bomba

class BombaCombustivel:

    def __init__(self, ValorLitro, TipoCombustivel, QuantidadeCombustivel, ):
        self.tipoC = TipoCombustivel  # o tipo de combustivel
        self.valorL = ValorLitro  # imformar o valor por litro
        self.qtd_combustivel = QuantidadeCombustivel  # imformar a quantidade para colocar no carro

    def Abastecer_por_valor(self, av):
        litros_abastecidos = av / self.valorL
        self.qtd_combustivel -= litros_abastecidos
        print(f"Deu {litros_abastecidos}:.2f litros no seu veiculo!")
        return litros_abastecidos

    def Abaster_por_litro(self, li):
        valor_total = li * self.valorL
        self.qtd_combustivel -= li
        print(f"Deu {valor_total} R$")
        return valor_total

    def Alterar_valor(self, nlitro):  # serve para voce mudar o valor primario dele, independente do tipo do combustivel
        self.valorL = nlitro
        print(f"O valor por litro foi alterado para {self.valorL} R$")

    def Alterar_Combustivel(self, ncombustivel):
        if ncombustivel == "gasolina":
            self.valorL += 1.5
            self.tipoC = ncombustivel
            print(f"O valor por litro foi alterado para {self.valorL} R$")
            print(f"O combustivel foi alterado para {self.tipoC}")

        elif ncombustivel == "alcool":
            self.valorL += 2.0
            self.tipoC = ncombustivel
            print(f"O valor por litro foi alterado para {self.valorL} R$")
            print(f"O combustivel foi alterado para {self.tipoC}")

        elif ncombustivel == "diesel":
            self.valorL += 2.5
            self.tipoC = ncombustivel
            print(f"O valor por litro foi alterado para {self.valorL} R$")
            print(f"O combustivel foi alterado para {self.tipoC}")

    def Alterar_quantidade_combustivel(self, bus):
        self.qtd_combustivel += bus
        print(f"foi adcionado {self.qtd_combustivel} litros na bomba!")


print("BEM-VINDO AO POSTO BOMBA-NERD!")
valorl = float(input("Imforme o preço por litro:\n"))
tipoc = (input("Imforme o tipo de combustivel da bomba (gasolina / alcool / diesel):\n"))

if tipoc == "gasolina":
    valorl += 1.5

elif tipoc == "alcool":
    valorl += 2.0

elif tipoc == "diesel":
    valorl += 2.5
print(f"O valor do combustivel do tipo {tipoc} ficou {valorl} reais")

qtd_bus = int(input("Digite a quantidade de combustivel que tera na bomba:\n"))
while qtd_bus == 0 or qtd_bus > 60000:
    if qtd_bus == 0:
        print("Não há combustível na bomba!")
    else:
        print("Limite máximo de combustível foi ultrapassado!")
    qtd_bus = int(input("Digite a quantidade de combustivel que tera na bomba:\n"))


bombacombustivel = BombaCombustivel(valorl, tipoc, qtd_bus)

print("HORA DE USAR A BOMBA!")
din = (input("Deseja entrar no menu? (sim \ nao):\n"))

while din == "sim":
    menu = int(input("Me diga o que voce quer fazer:"
                     "\n 1 - abaster_por_valor:"
                     "\n 2 - abastecer_por_litro:"
                     "\n 3 - alterar_valor:"
                     "\n 4 - alterar_combustivel:"
                     "\n 5 - alterar_quantidade_combustivel:"
                     "\n 6 - Sair:\n"))
    if menu == 1:
        valor = float(input("Digite o valor que quer gastar:\n"))
        bombacombustivel.Abastecer_por_valor(valor)
    elif menu == 2:
        litro = float(input("Digite quantos litros quer para o veiculo:\n"))
        bombacombustivel.Abaster_por_litro(litro)
    elif menu == 3:
        valorl = float(input("Imforme o novo preço por litro:\n"))
        bombacombustivel.Alterar_valor(valorl)
    elif menu == 4:
        tipoc = (input("Imforme o novo tipo de combustivel da bomba (gasolina / alcool / diesel):\n"))
        bombacombustivel.Alterar_Combustivel(tipoc)
    elif menu == 5:
        qtd_bus = int(input("Digite a quantidade de combustivel que tera na bomba:\n"))
        bombacombustivel.Alterar_quantidade_combustivel(qtd_bus)
    elif menu == 6:
        break

print("OBRIGADO POR USAR O MEU CODIGO!")