# Implementação do CRUD em Python para compra de um produtos no supermercado:
# Crie um BD Supermercado
# Crie uma Tabela Produto
# Produto possui: codProduto, nomeProduto, valorProduto

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='DB_supermercado'
)
#Cria cursor, responsavel por fazer manipulação no banco
cursor = db.cursor()

#CREATE
# pro_id  = int(input("digite o id do produto:\n"))
pro_nome = (input("Digite o nome do produto:\n"))
pro_valor = float(input("Digite o valor do produto?:\n"))
comando = f'INSERT INTO produto (pro_nome, pro_valor) VALUES ("{pro_nome}", {pro_valor})'
cursor.execute(comando)
db.commit() # edita o banco de dados

comando = f'SELECT * FROM produto'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)


# READ

# comando = f'SELECT * FROM produto'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

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

#Fechar Conexão e Cursor
cursor.close()
db.close()