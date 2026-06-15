PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS itens_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco NUMERIC NOT NULL CHECK (preco >= 0)
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    data_pedido TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
);

CREATE TABLE itens_pedido (
    id INTEGER PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
    FOREIGN KEY (produto_id) REFERENCES produtos (id)
);

INSERT INTO clientes (id, nome, email) VALUES
    (1, 'Ana Souza', 'ana@email.com'),
    (2, 'Bruno Lima', 'bruno@email.com'),
    (3, 'Carla Silva', 'carla@email.com');

INSERT INTO produtos (id, nome, preco) VALUES
    (1, 'Teclado', 120.00),
    (2, 'Mouse', 80.00),
    (3, 'Monitor', 950.00);

INSERT INTO pedidos (id, cliente_id, data_pedido) VALUES
    (1, 1, '2026-06-10'),
    (2, 2, '2026-06-11');

INSERT INTO itens_pedido (id, pedido_id, produto_id, quantidade) VALUES
    (1, 1, 1, 1),
    (2, 1, 2, 2),
    (3, 2, 3, 1);

-- Consultas de exemplo
SELECT c.nome AS cliente, p.id AS pedido, p.data_pedido
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
ORDER BY p.id;

SELECT pr.nome AS produto, SUM(i.quantidade) AS quantidade_vendida
FROM itens_pedido i
JOIN produtos pr ON pr.id = i.produto_id
GROUP BY pr.id, pr.nome
ORDER BY quantidade_vendida DESC;

SELECT c.nome AS cliente,
       ROUND(SUM(pr.preco * i.quantidade), 2) AS total_gasto
FROM clientes c
JOIN pedidos p ON p.cliente_id = c.id
JOIN itens_pedido i ON i.pedido_id = p.id
JOIN produtos pr ON pr.id = i.produto_id
GROUP BY c.id, c.nome
ORDER BY total_gasto DESC;
