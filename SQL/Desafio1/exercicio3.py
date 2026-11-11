import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
SELECT *
FROM pedidos WHERE
status = 'Entregue'
""")
resultado = cursor.fetchall()
for x in resultado:
    
    print(x)