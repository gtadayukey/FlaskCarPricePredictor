
-- Create table for cars on the fipe data
CREATE TABLE carros_fipe(
	id SERIAL PRIMARY KEY,
	mes_referencia VARCHAR(10) NOT NULL,
	cod_fipe VARCHAR(10) NOT NULL,
	marca VARCHAR(20) NOT NULL,
	modelo VARCHAR(100) NOT NULL,
	ano_modelo VARCHAR(20) NOT NULL,
	autenticacao VARCHAR(20) NOT NULL,
	dia_consulta VARCHAR(20) NOT NULL,
	data_consulta VARCHAR(50) NOT NULL,
	preco_medio FLOAT NOT NULL
);

-- Create table for users
CREATE TABLE usuario(
	cod_usuario SERIAL PRIMARY KEY,
	nome VARCHAR(20) NOT NULL,
	sobrenome VARCHAR(20) NOT NULL,
	email VARCHAR(50) NOT NULL,
	senha VARCHAR(20) NOT NULL,
	data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for consult history
CREATE TABLE historico_consultas (
    cod_historico SERIAL PRIMARY KEY,
    fipe_id INT NOT NULL,
    cod_usuario INT NOT NULL,
    FOREIGN KEY (fipe_id) REFERENCES carros_fipe(id),
    FOREIGN KEY (cod_usuario) REFERENCES usuario(cod_usuario),
    data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
