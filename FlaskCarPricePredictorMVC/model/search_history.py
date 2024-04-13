from FlaskCarPricePredictorMVC.data.connect import db
from FlaskCarPricePredictorMVC.model.user import User
from FlaskCarPricePredictorMVC.model.fipe_car import FipeCar
import datetime
from peewee import *


class ConsultHistory(Model):
    __tablename__ = 'search_history'
    fipe_id = ForeignKeyField(FipeCar, backref="fipe_car", null=False)
    user_id = ForeignKeyField(User, backref="user", null=False)
    consult_date = DateTimeField(default=datetime.datetime.now(), null=False)

    class Meta:
        database = db
