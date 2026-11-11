import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
SELECT produtos.nome, itens_pedido.quantidade
FROM  produtos JOIN itens_pedido ON produtos.id = produto_id
""")
resu = cursor.fetchall()
for x in resu:
    print(x)