import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()


cursor.execute("""SELECT clientes.nome, COUNT(pedidos.cliente_id) as total
FROM  clientes JOIN pedidos ON clientes.id = pedidos.cliente_id
GROUP BY  clientes.id, clientes.nome HAVING total > 1""")


resu = cursor.fetchall()
for x in resu:
    print(x)