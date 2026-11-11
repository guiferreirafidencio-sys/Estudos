import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
SELECT clientes.nome, pedidos.data,pedidos.status
FROM clientes JOIN pedidos ON clientes.id = pedidos.cliente_id
""")
resu = cursor.fetchall()
for x in resu:
    print(x)