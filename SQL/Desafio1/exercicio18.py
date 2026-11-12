import sqlite3 

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()


cursor.execute("""
SELECT SUM(produtos.preco * itens_pedido.quantidade) FROM produtos 
JOIN  itens_pedido ON produtos.id = itens_pedido.produto_id
JOIN pedidos ON pedidos.id = itens_pedido.pedido_id                       
WHERE pedidos.status = 'Entregue' """)

resu = cursor.fetchone()
print(f"Faturamento total R$ {resu[0]:.2f}")