from FlaskCarPricePredictorMVC.data.connect import db


def validate_register(first_name, last_name, email, first_password, second_password):
    if first_password == second_password:
        with db.connection() as con, con.cursor() as cursor:
            query = """SELECT * FROM usuario WHERE email = %s"""
            cursor.execute(query, email)
            user = cursor.fetchone()

            if user:
                return "Ja possui uma conta !"
            else:
                query = """INSERT INTO usuario (nome, sobrenome, email, senha) VALUES (%s, %s, %s, %s)"""

                cursor.execute(query, (first_name, last_name, email, first_password, second_password))
                con.commit()

                query = """SELECT * FROM usuario WHERE email = %s"""
                cursor.execute(query, email)

                user = cursor.fetchone()

                return user

