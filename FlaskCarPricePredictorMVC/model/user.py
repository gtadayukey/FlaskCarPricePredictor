from FlaskCarPricePredictorMVC.data.connect import db
from peewee import *


class User(Model):
    __tablename__ = 'user'
    first_name = CharField(20, null=False)
    last_name = CharField(20, null=False)

    class Meta:
        database = db
