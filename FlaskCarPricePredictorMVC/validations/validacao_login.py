from FlaskCarPricePredictorMVC.config.connection_database import get_connection
from FlaskCarPricePredictorMVC.user.usuario import Usuario


def validar_login(email_recebido, senha_recebida):
    with get_connection() as conexao, conexao.cursor() as cursor:
        sql = """SELECT * FROM usuario WHERE email = %s"""
        cursor.execute(sql, (email_recebido,))
        usuario = cursor.fetchone()

        if usuario and usuario[4] == senha_recebida:
            Usuario.nome_usuario = usuario[1] + " " + usuario[2]
            Usuario.id_usuario_atual = usuario[0]
            Usuario.usuario_logado = True
