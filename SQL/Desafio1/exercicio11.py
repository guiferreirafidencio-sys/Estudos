import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()

cursor.execute("""
SELECT clientes.nome,COUNT(pedidos.cliente_id)
FROM clientes JOIN pedidos ON clientes.id = pedidos.cliente_id
GROUP BY clientes.id,clientes.nome
""")
resultado = cursor.fetchall()
for x in resultado:
    nome,quantidade = x
    print(f"{nome} comprou {quantidade} itens")
    