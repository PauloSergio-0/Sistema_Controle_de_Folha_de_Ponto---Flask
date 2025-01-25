CREATE TABLE IF NOT EXISTS folha_ponto (
    id_funcionario INTEGER PRIMARY KEY ,
    nome VARCHAR NOT NULL,
    cpf VARCHAR NOT NULL,
    data VARCHAR NOT NULL,
    hora_entrada VARCHAR NOT NULL,
    hora_saida VARCHAR NOT NULL,
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
);