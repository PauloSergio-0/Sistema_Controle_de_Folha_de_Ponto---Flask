CREATE TABLE IF NOT EXISTS funcionario (
    id_funcionario SERIAL PRIMARY KEY ,
    nome VARCHAR NOT NULL,
    cpf VARCHAR NOT NULL,
    departamento VARCHAR NOT NULL,
    status INTEGER NOT NULL
    );