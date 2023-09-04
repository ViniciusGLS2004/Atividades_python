import mysql.connector
from PIL import Image
from io import BytesIO

# Inicialize as variáveis de conexão e cursor com None
#garantir que as variáveis estejam definidas
conexao = None
cursor = None
dados_imagem = None
imagem = None

#usando try para caso ocorrra augum erro
try:
    # Conecte-se ao banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='odeiolol',  # senha do seu banco de dados
        database='cs_veiculo'
    )

    cursor = conexao.cursor()

    # Abra o arquivo da imagem no modo binário e leia os dados
    # Abrimos o arquivo de imagem no modo binário ('rb') e lemos os dados binários da imagem, armazenando-os na variável dados_imagem.
    with open(r'C:\Users\vg160\PycharmProjects\python_Iniciante\imagens\One.png', 'rb') as arquivo:
        dados_imagem = arquivo.read()

    # Insira os dados da imagem no banco de dados
    inserir_imagem = ("INSERT INTO imagens (nome, dados_imagem) VALUES (%s, %s)")
    dados = ('One.png', dados_imagem)

    cursor.execute(inserir_imagem, dados)
    # salva os dados da imagem no banco de dados.
    conexao.commit()

    # Execute a consulta SQL para recuperar os dados da imagem
    buscar_imagem = ("SELECT dados_imagem FROM imagens WHERE nome = %s")
    nome = ('One.png',)

    cursor.execute(buscar_imagem, nome)
    dados_imagem = cursor.fetchone()[0]

    # Ler todos os resultados pendentes
    cursor.fetchall()

    # Carregue os dados binários da imagem em um objeto Image
    imagem = Image.open(BytesIO(dados_imagem))

    # Exiba a imagem
    imagem.show()

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

finally:
    # Certifique-se de fechar a conexão e o cursor, mesmo se ocorrer uma exceção
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
