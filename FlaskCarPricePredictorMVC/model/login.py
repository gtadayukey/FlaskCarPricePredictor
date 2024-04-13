from FlaskCarPricePredictorMVC.model.user import User
from FlaskCarPricePredictorMVC.data.connect import db
import datetime
from peewee import *


class Login(Model):
    __tablename__ = 'login'
    user_id = ForeignKeyField(User, primary_key=True, backref="user", null=False)
    email = CharField(50, unique=True, null=False)
    password = CharField(20, null=False)
    register_date = DateTimeField(default=datetime.datetime.now(), null=False)

    class Meta:
        database = db
