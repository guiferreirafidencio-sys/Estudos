import sqlite3


conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()


cursor.execute("""
SELECT pedidos.id ,SUM(produtos.preco * itens_pedido.quantidade)
FROM pedidos JOIN itens_pedido ON pedidos.id = itens_pedido.pedido_id
JOIN produtos ON itens_pedido.produto_id = produtos.id
GROUP BY pedidos.id
""")
resu = cursor.fetchall()

for x in resu:
    id,valor = x
    print(f"pedido numero {id} deu R${valor}")