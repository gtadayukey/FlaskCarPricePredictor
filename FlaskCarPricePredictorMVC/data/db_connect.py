from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://postgres:12341234@localhost/flaskcarpricepredictormvcdb')

with engine.connect() as connection:
    result = connection.execute()