from FlaskCarPricePredictorMVC.config.connection_database import get_connection
from FlaskCarPricePredictorMVC.model.user import Usuario


def validar_cadastro(nome_recebido, sobrenome_recebido, email_recebido, senha_recebida1, senha_recebida2):
    erro_cadastro = "Senhas incompatíveis !"

    if senha_recebida1 == senha_recebida2:
        with get_connection() as conexao, conexao.cursor() as cursor:
            sql = """SELECT * FROM usuario WHERE email = %s"""
            cursor.execute(sql, (email_recebido,))
            usuario = cursor.fetchone()

            if usuario:
                erro_cadastro = "Ja possui uma conta !"
            else:
                sql = """INSERT INTO usuario (nome, sobrenome, email, senha) VALUES (%s, %s, %s, %s)"""

                cursor.execute(sql, (nome_recebido, sobrenome_recebido, email_recebido, senha_recebida1))
                conexao.commit()

                sql = """SELECT * FROM usuario WHERE email = %s"""
                cursor.execute(sql, (email_recebido,))

                usuario = cursor.fetchone()

                Usuario.nome_usuario = nome_recebido + " " + sobrenome_recebido
                Usuario.id_usuario_atual = usuario[0]
                Usuario.usuario_logado = True

    return erro_cadastro
