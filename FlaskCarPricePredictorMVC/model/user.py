import psycopg2
from sqlalchemy import create_engine, Column, String, Integer, TIMESTAMP, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:12341234@postgres/flaskcarpricepredictor')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column("user_id", Integer, primary_key=True)
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    register_date = Column("register_date", TIMESTAMP, default=True)

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"({self.user_id}) {self.first_name} {self.last_name} ({self.register_date})"


session = Session()

user = User(12312, "Mike", "Smith")
session.add(user)
session.commit()
