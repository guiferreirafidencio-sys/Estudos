import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
SELECT COUNT(nome) FROM clientes
""")
resultado = cursor.fetchone()
print(resultado[0])