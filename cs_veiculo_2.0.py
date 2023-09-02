import mysql.connector

cs = mysql.connector.connect(
    host='localhost',
    user='root',
    password='odeiolol',
    database='cs_veiculo'
)

cursor = cs.cursor()

class Veiculo:
    def __init__(self, tipo, cor, ano, estado, kmrodados, leilao, num_placa, tipo_combustivel, direcao, marca, modelo, tipo_desempenho, desempenho, preco):
        self.tipo = tipo
        self.cor = cor
        self.ano = ano
        self.estado = estado
        self.rodados = kmrodados
        self.leilao = leilao
        self.placa = num_placa
        self.combustivel = tipo_combustivel
        self.direcao = direcao
        self.marca = marca
        self.modelo = modelo
        self.tipo_desempenho = tipo_desempenho
        self.desempenho = desempenho
        self.preco = preco

    def create(self):
        comando = (
            'INSERT INTO veiculo (vei_tipo, vei_cor, vei_ano, vei_estado, vei_kmrodados, vei_leilao, '
            'vei_num_placa, vei_tipo_combustivel, vei_direcao, vei_marca, vei_modelo, vei_tipo_desempenho, vei_desempenho, vei_preco) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        )
        valores = (self.tipo, self.cor, self.ano, self.estado, self.rodados, self.leilao, self.placa,
                   self.combustivel, self.direcao, self.marca, self.modelo, self.tipo_desempenho, self.desempenho, self.preco)
        cursor.execute(comando, valores)
        cs.commit()

        comando = f'SELECT * FROM veiculo'  # codigo para printar os dados da tabela
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

    def update(self, alter, idveiculo, alteracao_veiculo):
        if alter == 1:
            comando = f'UPDATE veiculo SET vei_tipo = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 2:
            comando = f'UPDATE veiculo SET vei_cor = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 3:
            comando = f'UPDATE veiculo SET vei_ano = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 4:
            comando = f'UPDATE veiculo SET vei_estado = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 5:
            comando = f'UPDATE veiculo SET vei_kmrodados = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 6:
            comando = f'UPDATE veiculo SET vei_leilao = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 7:
            comando = f'UPDATE veiculo SET vei_num_placa = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 8:
            comando = f'UPDATE veiculo SET vei_tipo_combustivel = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 9:
            comando = f'UPDATE veiculo SET vei_direcao = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 10:
            comando = f'UPDATE veiculo SET vei_marca = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 11:
            comando = f'UPDATE veiculo SET vei_modelo = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 12:
            comando = f'UPDATE veiculo SET vei_tipo_desempenho = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 13:
            comando = f'UPDATE veiculo SET vei_desempenho = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        elif alter == 14:
            comando = f'UPDATE veiculo SET vei_preco = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
            cursor.execute(comando)
            cs.commit()

        comando = f'SELECT * FROM veiculo'  # codigo para printar os dados da tabela
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

    def delete(self, nomedelete):
        comando = f'DELETE FROM veiculo WHERE vei_num_placa = "{nomedelete}"'
        cursor.execute(comando)
        cs.commit()

    comando = f'SELECT * FROM veiculo'  # codigo para printar os dados da tabela
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)

# Criação do objeto com seus atributos
vei_tipo = input("Digite o tipo do veiculo:\n")
vei_cor = input("Digite a cor do veiculo:\n")
vei_ano = int(input("Digite o ano do veiculo:\n"))
vei_estado = input("Digite o estado do veiculo:\n")
vei_kmrodados = float(input("Digite os km rodados do veiculo:\n"))
vei_leilao = input("Digite (sim ou nao) se o veiculo é ou não de leilao :\n")
vei_num_placa = int(input("Digite o numero da placa do veiculo:\n"))
vei_tipo_combustivel = input("Digite o tipo do combust ivel do veiculo:\n")
vei_direcao = input("Digite a direção do veiculo:\n")
vei_marca = input("Digite a marca do veiculo:\n")
vei_modelo = input("Digite o modelo do veiculo:\n")
vei_tipo_desempenho = input("Digite o tipo de desempenho do veiculo:\n")
vei_desempenho = input("Digite o desempenho do veiculo:\n")
vei_preco = float(input("Digite o preço do veiculo:\n"))

veiculo = Veiculo(vei_tipo, vei_cor, vei_ano, vei_estado, vei_kmrodados, vei_leilao, vei_num_placa,
                  vei_tipo_combustivel, vei_direcao, vei_marca, vei_modelo, vei_tipo_desempenho, vei_desempenho, vei_preco)
veiculo.create()

alt = input("Deseja fazer alguma alteração na tabela? (sim ou nao):\n")
while alt == "sim":
    menu = int(input("Me diga o que você quer fazer:"
                     "\n 1 - alterar dado:"
                     "\n 2 - deletar dado:"
                     "\n 3 - Sair:\n"))
    if menu == 1:
        alter = int(input("Digite a informação específica a ser alterada:"
                          "\n 1 - alterar tipo:"
                          "\n 2 - alterar cor:"
                          "\n 3 - alterar ano:"
                          "\n 4 - alterar estado:"
                          "\n 5 - alterar km rodados:"
                          "\n 6 - alterar leilão:"
                          "\n 7 - alterar numero de placa:"
                          "\n 8 - alterar tipo do combustivel:"
                          "\n 9 - alterar direção:"
                          "\n 10 - alterar marca:"
                          "\n 11 - alterar modelo:"
                          "\n 12 - alterar tipo de desempenho:"
                          "\n 13 - alterar desempenho:"
                          "\n 14 - alterar preço:\n"))
        if alter >= 1 and alter <= 14:
            ide = int(input("Digite o id do veiculo:\n"))
            altera = input("Digite o novo valor:\n")
            veiculo.update(alter, ide, altera)
            print("Dado alterado!")

    elif menu == 2:
        nomedelete = input("Digite o numero da placa do veiculo que quer deletar da tabela:\n")
        veiculo.delete(nomedelete)
        print("Veiculo deletado!")

    elif menu == 3:
        break

    alt = input("Deseja fazer alguma alteração na tabela veiculo? (sim ou nao):\n")
print("Codigo veiculo fechado!")
cursor.close()
cs.close()

# CREATE
# pro_id  = int(input("digite o id do produto:\n"))
# pro_nome = (input("Digite o nome do produto:\n"))
# pro_valor = float(input("Digite o valor do produto?:\n"))
# comando = f'INSERT INTO produto (pro_nome, pro_valor) VALUES ("{pro_nome}", {pro_valor})'
# cursor.execute(comando)
# db.commit() # edita o banco de dados

# UPDATE

# pro_nome = "chocolate"
# pro_valor = 11
# comando = f'UPDATE produto SET pro_valor = {pro_valor} WHERE pro_nome = "{pro_nome}"'
# cursor.execute(comando)
# db.commit() # edita o banco de dados

# comando = f'SELECT * FROM produto'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

# DELETE

# pro_nome = "bolacha"
# comando = f'DELETE FROM produto WHERE pro_nome = "{pro_nome}"'
# cursor.execute(comando)
# db.commit() # edita o banco de dados

# comando = f'SELECT * FROM produto'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

# READ

# comando = f'SELECT * FROM produto'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)
