
import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT nome,idade,cidade
    FROM clientes
    WHERE cidade = 'Guarulhos'
""")

resu = cursor.fetchall()

for x in resu:
    nome,idade,cidade = x
    print(nome,idade,cidade)

conexao.close()
