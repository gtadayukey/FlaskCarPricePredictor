from connect import db
from FlaskCarPricePredictorMVC.model.user import User
from FlaskCarPricePredictorMVC.model.login import Login
from FlaskCarPricePredictorMVC.model.fipe_car import FipeCar
from FlaskCarPricePredictorMVC.model.search_history import ConsultHistory

db.connect()
db.create_tables((User, Login, FipeCar, ConsultHistory))

