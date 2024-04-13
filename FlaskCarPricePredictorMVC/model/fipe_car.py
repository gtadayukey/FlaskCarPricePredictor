from FlaskCarPricePredictorMVC.data.connect import db
from peewee import *


class FipeCar(Model):
    __tablename__ = 'fipe_car'
    reference_month = CharField(10, null=False)
    fipe_code = CharField(10, null=False)
    brand = CharField(20, null=False)
    model = CharField(100, null=False)
    year_model = CharField(20, null=False)
    authentication = CharField(20, null=False)
    consult_day = CharField(20, null=False)
    consult_date = CharField(50, null=False)
    average_price = FloatField(null=False)

    class Meta:
        database = db
