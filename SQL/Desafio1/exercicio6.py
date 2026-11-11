import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
SELECT clientes.nome, pedidos.id FROM clientes
JOIN pedidos ON clientes.id = pedidos.cliente_id
""")
resultado = cursor.fetchall()
for x in resultado:
    print(x)