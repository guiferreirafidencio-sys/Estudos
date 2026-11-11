
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL,
    idade INTEGER
)
""")

# Produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

# Pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data DATE NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
""")

# Itens de cada pedido
cursor.execute("""
CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
""")

# Dados dos clientes
cursor.executemany("""
INSERT INTO clientes (nome, cidade, idade)
VALUES (?, ?, ?)
""", [
    ("Carlos", "Guarulhos", 25),
    ("Mariana", "São Paulo", 32),
    ("João", "Guarulhos", 19),
    ("Ana", "Mogi das Cruzes", 28),
    ("Pedro", "São Paulo", 40),
])

# Dados dos produtos
cursor.executemany("""
INSERT INTO produtos (nome, categoria, preco)
VALUES (?, ?, ?)
""", [
    ("Notebook", "Eletrônicos", 3500),
    ("Mouse", "Acessórios", 80),
    ("Teclado", "Acessórios", 150),
    ("Monitor", "Eletrônicos", 1200),
    ("Cadeira", "Móveis", 900),
])

# Pedidos
cursor.executemany("""
INSERT INTO pedidos (cliente_id, data, status)
VALUES (?, ?, ?)
""", [
    (1, "2026-10-01", "Entregue"),
    (2, "2026-10-02", "Entregue"),
    (1, "2026-10-05", "Pendente"),
    (3, "2026-10-07", "Entregue"),
    (4, "2026-10-10", "Cancelado"),
    (5, "2026-10-12", "Entregue"),
])

# Produtos dentro dos pedidos
cursor.executemany("""
INSERT INTO itens_pedido (pedido_id, produto_id, quantidade)
VALUES (?, ?, ?)
""", [
    (1, 1, 1),
    (1, 2, 2),
    (2, 3, 1),
    (2, 4, 1),
    (3, 5, 2),
    (3, 2, 1),
    (4, 1, 1),
    (5, 3, 2),
    (6, 4, 2),
])

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
