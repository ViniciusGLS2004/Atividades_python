import mysql.connector

jm = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='jm_veiculo'
)

cursor = jm.cursor()


class Cliente: # classe para a tabela cliente

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def create(self): # função create para criar um dado na tabela

        comando = f'INSERT INTO cliente (cli_nome, cli_CPF, cli_endereco) VALUES ("{self.nome}", {self.cpf}, "{self.endereco}")'
        cursor.execute(comando)
        jm.commit()  # edita o banco de dados

        comando = f'SELECT * FROM cliente'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

    def update(self, alter, idcliente, alteracao_cliente): # função para alterar dado, ligado ao menu como parametro

        if alter == 1:
            comando = f'UPDATE cliente SET cli_nome = "{alteracao_cliente}" WHERE cli_id = {idcliente}'
            cursor.execute(comando)
            jm.commit()  # edita o banco de dados

        elif alter == 2:
            comando = f'UPDATE cliente SET cli_endereco = "{alteracao_cliente}" WHERE cli_id = {idcliente}'
            cursor.execute(comando)
            jm.commit()  # edita o banco de dados

        elif alter == 3:
            comando = f'UPDATE cliente SET cli_tel = {alteracao_cliente} WHERE cli_id = {idcliente}'
            cursor.execute(comando)
            jm.commit()  # edita o banco de dados

        elif alter == 4:
            comando = f'UPDATE cliente SET cli_RG = {alteracao_cliente} WHERE cli_id = {idcliente}'
            cursor.execute(comando)
            jm.commit()  # edita o banco de dados

        comando = f'SELECT * FROM cliente' #codigo para printar os dados da tabela
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

    def delete(self, nomedelete): # função para deletar um dado da tabela
        comando = f'DELETE FROM cliente WHERE cli_nome = "{nomedelete}"'
        cursor.execute(comando)
        jm.commit()  # edita o banco de dados

        comando = f'SELECT * FROM cliente' #codigo para printar os dados da tabela
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

# criação do objeto com seus atributos
cli_nome = (input("Digite o nome do cliente :\n"))
cli_cpf = int(input("Digite o cpf do cliente: \n"))
cli_endereco = (input("Digite o endereço do cliente: \n"))
cliente = Cliente(cli_nome, cli_cpf, cli_endereco) #adcionado os dados do objeto na tabela
cliente.create()
alt = (input("Deseja fazer aguma alteração na tabela? (sim \ nao):\n")) # laço while para entrar no menu
while alt == "sim":
    menu = int(input("Me diga o que voce quer fazer:" # menu para escolher o que qer fazer no bd cliente
                     "\n 1 - alterar dado:"
                     "\n 2 - deletar dado:"
                     "\n 3 - Sair:\n"))
    if menu == 1:

        alter = int(input("Digite a imformação especifica a ser alerada:" # menu para fazer uma alteração especifica de um dado
                          "\n 1 - alterar nome:"
                          "\n 2 - alterar endereco:"
                          "\n 3 - alterar telefone:"
                          "\n 4 - alterar RG:\n"))
        if alter == 1:
            ide = int(input("Digite o id do cliente:\n"))
            altera = (input("Digite um novo nome:\n"))
            cliente.update(alter, ide, altera)
            print("Nome alterado!")

        elif alter == 2:
            ide = int(input("Digite o id do cliente:\n"))
            altera = (input("Digite um novo endereco:\n"))
            cliente.update(alter, ide, altera)
            print("Endereço alterado!")

        elif alter == 3:
            ide = int(input("Digite o id do cliente:\n"))
            altera = (input("Digite um novo telefone:\n"))
            cliente.update(alter, ide, altera)
            print("Telefone alterado!")

        elif alter == 4:
            ide = int(input("Digite o id do cliente:\n"))
            altera = int(input("Digite um novo RG:\n"))
            cliente.update(alter, ide, altera)
            print("RG alterado!")

    elif menu == 2:
        nomedelete = (input("Digite o nome do cliente que quer deletar da tabela:\n"))
        cliente.delete(nomedelete)
        print("Cliente deletado!")

    elif menu == 3:
        break

    alt = (input("Deseja fazer aguma alteração na tabela? (sim \ nao):\n")) # a mesma pergunta caso voçe queira retornar ao laço
print("Codigo fechado!")
cursor.close()
jm.close()

#CREATE
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