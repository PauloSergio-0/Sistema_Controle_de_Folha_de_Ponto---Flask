CREATE TABLE IF NOT EXISTS funcionario (
    id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    cpf VARCHAR NOT NULL,
    departamento VARCHAR NOT NULL,
    status INTEGER NOT NULL
    );