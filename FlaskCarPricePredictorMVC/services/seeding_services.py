from FlaskCarPricePredictorMVC.data.connect import db


def seed():
    with db.connection() as con, con.cursor() as cursor:
        table_name = "usuario"
        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor.execute(query)
        count = cursor.fetchone()[0]

        if not count:
            # seed service implementation
            pass
