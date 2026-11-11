import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
SELECT nome,categoria,preco FROM produtos
WHERE preco > 500
""")
resultado = cursor.fetchall()
for x in resultado:
    nome,categoria,preço = x
    print(nome,categoria,preço)