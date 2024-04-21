from FlaskCarPricePredictorMVC.data.connect import db


def validate_login(email, password):
    with db.connection() as con, con.cursor() as cursor:
        query = """SELECT * FROM login WHERE email = %s AND password = %s"""
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        return user
