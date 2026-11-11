import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
SELECT clientes.nome , produtos.nome, itens_pedido.quantidade
FROM clientes JOIN pedidos ON clientes.id = pedidos.cliente_id
JOIN itens_pedido ON pedidos.id = itens_pedido.pedido_id
JOiN produtos ON itens_pedido.produto_id = produtos.id
""")

resu = cursor.fetchall()
print(resu)