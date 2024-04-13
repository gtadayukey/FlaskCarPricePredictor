import datetime
from peewee import *

db = PostgresqlDatabase('flaskcarpricepredictormvcdb', user='postgres', password='12341234',
                        host='localhost', port=5432)


class User(Model):
    __tablename__ = 'users'
    first_name = CharField()
    last_name = CharField()
    register_date = DateTimeField(default=datetime.UTC)

    class Meta:
        database = db


class Login(Model):
    __tablename__ = 'login'
    user_id = ForeignKeyField(User, backref="users")
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
