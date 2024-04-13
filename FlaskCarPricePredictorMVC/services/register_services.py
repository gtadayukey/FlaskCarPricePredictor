from FlaskCarPricePredictorMVC.data.connect import db


def validar_cadastro(nome_recebido, sobrenome_recebido, email_recebido, senha_recebida1, senha_recebida2):
    erro_cadastro = "Senhas incompatíveis !"

    if senha_recebida1 == senha_recebida2:
        with db.connection() as conexao, conexao.cursor() as cursor:
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

    return erro_cadastro

