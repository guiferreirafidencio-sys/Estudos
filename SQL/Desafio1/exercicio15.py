import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()


cursor.execute("""
SELECT categoria, AVG(preco) 
FROM produtos GROUP BY categoria ORDER BY preco DESC
""")
resultado = cursor.fetchall()
for x in resultado:
    print(x)