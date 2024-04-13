import datetime
from peewee import *

db = PostgresqlDatabase('flaskcarpricepredictormvcdb', user='postgres', password='12341234',
                        host='localhost', port=5432)
