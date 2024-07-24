import sqlite3

# criação do banco de dados
con = sqlite3.connect('exemplo')

cursor = con.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER)
'''
)

# inserir dados na tabela
cursor.execute(
    '''INSERT INTO usuarios(nome, idade) VALUES (?,?)
''', ("Teste", 30)
    )

con.commit()

cursor.execute(
    '''SELECT * FROM usuarios
'''
    )

registro = cursor.fetchall()

# comando para ler as informações inseridas no banco
for regis in registro:
    print(regis)