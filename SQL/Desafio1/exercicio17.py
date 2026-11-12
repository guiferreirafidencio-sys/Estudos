import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()


cursor.execute("""
SELECT produtos.nome, SUM(itens_pedido.quantidade) AS total
FROM produtos JOIN itens_pedido ON produtos.id = itens_pedido.produto_id
GROUP BY produtos.id,  produtos.nome HAVING total > 1 ORDER BY total DESC
""")

resu = cursor.fetchall()

for x in resu:
    print(x)