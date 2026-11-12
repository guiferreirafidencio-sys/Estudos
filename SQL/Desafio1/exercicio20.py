import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()

cursor.execute("""
SELECT clientes.nome, COUNT(pedidos.id) AS total
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
AND pedidos.status != 'Cancelado'
GROUP BY clientes.id, clientes.nome
HAVING total = 0
""")
resu = cursor.fetchall()
for x in resu:
    print(x)