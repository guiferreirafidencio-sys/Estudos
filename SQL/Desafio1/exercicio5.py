import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
SELECT AVG(preco) FROM produtos
""")
resultado = cursor.fetchone()
print(resultado)