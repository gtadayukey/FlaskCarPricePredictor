from FlaskCarPricePredictorMVC.data.connect import db


def validar_login(email_recebido, senha_recebida):
    with db.connection() as conexao, conexao.cursor() as cursor:
        sql = """SELECT * FROM usuario WHERE email = %s"""
        cursor.execute(sql, (email_recebido,))
        usuario = cursor.fetchone()
