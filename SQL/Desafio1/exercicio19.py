import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()

cursor.execute("""
SELECT clientes.nome, SUM(produtos.preco * itens_pedido.quantidade)as total
FROM clientes JOIN  pedidos ON clientes.id = pedidos.cliente_id
JOIN itens_pedido ON pedidos.id = itens_pedido.pedido_id
JOIN produtos ON itens_pedido.produto_id = produtos.id
WHERE pedidos.status = 'Entregue'
GROUP BY clientes.nome , clientes.id ORDER BY total DESC LIMIT 1
""")

resu = cursor.fetchall()

for x in resu:
    print(x)