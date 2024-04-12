import psycopg2


def get_connection():
    connect = psycopg2.connect(
        host='localhost',
        port=5432,
        database='flaskcarpricepredictormvcdb',
        user='postgres',
        password='12341234'
    )

    return connect
