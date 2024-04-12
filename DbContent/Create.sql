
-- Create table for cars on the fipe data
CREATE TABLE fipe_car(
	car_id SERIAL PRIMARY KEY,
	reference_month VARCHAR(10) NOT NULL,
	fipe_code VARCHAR(10) NOT NULL,
	brand VARCHAR(20) NOT NULL,
	model VARCHAR(100) NOT NULL,
	year_model VARCHAR(20) NOT NULL,
	authentication VARCHAR(20) NOT NULL,
	consult_day VARCHAR(20) NOT NULL,
	consult_date VARCHAR(50) NOT NULL,
	average_price FLOAT NOT NULL
);

-- Create table for users
CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for login
CREATE TABLE login(
	user_id FOREIGN KEY,
	email VARCHAR(50) NOT NULL,
	password VARCHAR(20) NOT NULL,
);

-- Create table for consult history
CREATE TABLE user_analysis_history (
    cod_historico SERIAL PRIMARY KEY,
    fipe_id INT NOT NULL,
    cod_usuario INT NOT NULL,
    FOREIGN KEY (fipe_id) REFERENCES carros_fipe(id),
    FOREIGN KEY (cod_usuario) REFERENCES usuario(cod_usuario),
    data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
