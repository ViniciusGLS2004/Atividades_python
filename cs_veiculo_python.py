import mysql.connector

cs = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cs_veiculo'
)

cursor = cs.cursor()


# class Veiculo:
#     def __init__(self, tipo, cor, ano, estado, kmrodados, leilao, num_placa, tipo_combustivel, direcao):
#         self.tipo = tipo
#         self.cor = cor
#         self.ano = ano
#         self.estado = estado
#         self.rodados = kmrodados
#         self.leilao = leilao
#         self.placa = num_placa
#         self.combustivel = tipo_combustivel
#         self.direcao = direcao
#
#     def create(self):
#         comando = (
#             'INSERT INTO veiculo (vei_tipo, vei_cor, vei_ano, vei_estado, vei_kmrodados, vei_leilao, '
#             'vei_num_placa, vei_tipo_combustivel, vei_direcao) '
#             'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
#         )
#         valores = (self.tipo, self.cor, self.ano, self.estado, self.rodados, self.leilao, self.placa,
#                    self.combustivel, self.direcao)
#         cursor.execute(comando, valores)
#         # edita o banco de dados
#
#         comando = f'SELECT * FROM veiculo'
#         cursor.execute(comando)
#         resultado = cursor.fetchall()  # ler o banco de dados
#         print(resultado)
#
#     def update(self, alter, idveiculo, alteracao_veiculo):  # função para alterar dado, ligado ao menu como parametro
#
#         if alter == 1:
#             comando = f'UPDATE veiculo SET vei_tipo = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 2:
#             comando = f'UPDATE veiculo SET vei_cor = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 3:
#             comando = f'UPDATE veiculo SET vei_ano = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 4:
#             comando = f'UPDATE veiculo SET vei_estado = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 5:
#             comando = f'UPDATE veiculo SET vei_kmrodados = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 6:
#             comando = f'UPDATE veiculo SET vei_leilao = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 7:
#             comando = f'UPDATE veiculo SET vei_num_placa = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 8:
#             comando = f'UPDATE veiculo SET vei_tipo_combustivel = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados
#
#         elif alter == 9:
#             comando = f'UPDATE veiculo SET vei_direcao = "{alteracao_veiculo}" WHERE vei_id = {idveiculo}'
#             cursor.execute(comando)
#             cs.commit()  # edita o banco de dados

        # elif alter == 10:
        #     comando = f'UPDATE veiculo SET vei_marca = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
        #     cursor.execute(comando)
        #     cs.commit()  # edita o banco de dados

        # elif alter == 11:
        #     comando = f'UPDATE veiculo SET vei_modelo = {alteracao_veiculo} WHERE vei_id = {idveiculo}'
        #     cursor.execute(comando)
        #     cs.commit()  # edita o banco de dados

    #     comando = f'SELECT * FROM veiculo'  # codigo para printar os dados da tabela
    #     cursor.execute(comando)
    #     resultado = cursor.fetchall()  # ler o banco de dados
    #     print(resultado)
    #
    # def delete(self, nomedelete):  # função para deletar um dado da tabela
    #     comando = f'DELETE FROM veiculo WHERE vei_num_placa = "{nomedelete}"'
    #     cursor.execute(comando)
    #     cs.commit()  # edita o banco de dados
    #
    #     comando = f'SELECT * FROM veiculo'  # codigo para printar os dados da tabela
    #     cursor.execute(comando)
    #     resultado = cursor.fetchall()  # ler o banco de dados
    #     print(resultado)


# criação do objeto com seus atributos
#
# vei_tipo = (input("Digite o tipo do veiculo:\n"))
# vei_cor = (input("Digite a cor do veiculo:\n"))
# vei_ano = int(input("Digite o ano do veiculo:\n"))
# vei_estado = (input("Digite o estado do veiculo:\n"))
# vei_kmrodados = float(input("Digite os km rodados do veiculo:\n"))
# vei_leilao = (input("Digite (sim ou nao) se o veiculo é ou não de leilao :\n"))
# vei_num_placa = int(input("Digite o numero da placa do veiculo:\n"))
# vei_tipo_combustivel = (input("Digite o tipo do combustivel do veiculo:\n"))
# vei_direcao = (input("Digite a direção do veiculo:\n"))
# veiculo = Veiculo(vei_tipo, vei_cor, vei_ano, vei_estado, vei_kmrodados, vei_leilao, vei_num_placa,
#                   vei_tipo_combustivel, vei_direcao)  # adcionado os dados do objeto na tabela
# veiculo.create()
# alt = (input("Deseja fazer aguma alteração na tabela? (sim \ nao):\n"))  # laço while para entrar no menu
# while alt == "sim":
#     menu = int(input("Me diga o que voce quer fazer:"  # menu para escolher o que qer fazer no bd veiculo
#                      "\n 1 - alterar dado:"
#                      "\n 2 - deletar dado:"
#                      "\n 3 - Sair:\n"))
#     if menu == 1:
#
#         alter = int(input("Digite a imformação especifica a ser alerada:"  # menu para fazer uma alteração especifica de um dado
#                   "\n 1 - alterar tipo:"
#                   "\n 2 - alterar cor:"
#                   "\n 3 - alterar ano:"
#                   "\n 4 - alterar estado:"
#                   "\n 5 - alterar km rodados:"
#                   "\n 6 - alterar leilão:"
#                   "\n 7 - alterar numero de placa:"
#                   "\n 8 - alterar tipo do combustivel:"
#                   "\n 9 - alterar direção:\n"))
#         if alter == 1:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = (input("Digite um novo tipo de veiculo:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Tipo alterado!")
#
#         elif alter == 2:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = (input("Digite a nova cor do veiculo:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Cor alterada!")
#
#         elif alter == 3:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = int(input("Digite um novo ano do veiculo:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Ano alterado!")
#
#         elif alter == 4:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = (input("Digite um novo estado do veiculo:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Estado alterado!")
#
#         if alter == 5:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = float(input("Digite um novo km rodados do veiculo:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Km rodados alterado!")
#
#         elif alter == 6:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = (input("Digite sim ou nao pra saber se é leilao ou nao:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Leilão alterado!")
#
#         elif alter == 7:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = int(input("Digite um novo numero de placa:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Numero de placa alterado!")
#
#         elif alter == 8:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = (input("Digite o novo tipo de combustivel:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Tipo de combustivel alterado!")
#
#         elif alter == 9:
#             ide = int(input("Digite o id do veiculo:\n"))
#             altera = (input("Digite uma nova direção do veiculo:\n"))
#             veiculo.update(alter, ide, altera)
#             print("Direção alterado!")
#
#     elif menu == 2:
#         nomedelete = int(input("Digite o numero da palaca do veiculo que quer deletar da tabela:\n"))
#         veiculo.delete(nomedelete)
#         print("veiculo deletado!")
#
#     elif menu == 3:
#         break
#
#     alt = (input("Deseja fazer aguma alteração na tabela veiculo? (sim \ nao):\n"))  # a mesma pergunta caso voçe queira retornar ao laço
# print("Codigo veiculo fechado!")


class Venda:
    def __init__(self, preco):
        self.preco = preco

    def create(self):
        comando = (
            f'INSERT INTO venda (ven_preco_veiculo) VALUES (%s)'
        )
        valores = (self.preco,)
        cursor.execute(comando, valores)
        # edita o banco de dados

        comando = f'SELECT * FROM venda'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

    def update(self, npreco, idpreco):
        comando = f'UPDATE venda SET ven_preco_veiculo = "{npreco}" WHERE ven_id = {idpreco}'
        cursor.execute(comando)
        cs.commit()  # edita o banco de dados

    comando = f'SELECT * FROM veiculo'  # codigo para printar os dados da tabela
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)


    def delete(self, npreco):  # função para deletar um dado da tabela
        comando = f'DELETE FROM venda WHERE ven_id = "{npreco}"'
        cursor.execute(comando)
        cs.commit()  # edita o banco de dados

        comando = f'SELECT * FROM venda'  # codigo para printar os dados da tabela
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

precov = float(input("Digite o preco do veiculo:\n"))
preco_veiculo = Venda(precov)
preco_veiculo.create()

altv = (input("Deseja fazer aguma alteração na tabela venda? (sim \ nao):\n"))  # laço while para entrar no menu
while altv == "sim":
    menu = int(input("Me diga o que voce quer fazer:"  # menu para escolher o que qer fazer no bd veiculo
                     "\n 1 - alterar dado:"
                     "\n 2 - deletar dado:"
                     "\n 3 - Sair:\n"))

    if menu == 1:
        ide = int(input("Digite o id da venda:\n"))
        alteravalor = (input("Digite um novo valor do veiculo:\n"))
        preco_veiculo.update(ide, alteravalor)
        print("Valor alterado!")

    elif menu == 2:
        nomedelete = int(input("Digite o numero de id da venda que quer deletar da tabela:\n"))
        preco_veiculo.delete(nomedelete)
        print("veiculo deletado!")

    elif menu == 3:
        break

    alt = (input("Deseja fazer aguma alteração na tabela venda? (sim \ nao):\n"))  # a mesma pergunta caso voçe queira retornar ao laço
    print("Codigo  venda fechado!")

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
