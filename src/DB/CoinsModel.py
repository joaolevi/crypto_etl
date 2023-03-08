from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base

from .DBSession import DBSession

Base = declarative_base()

class Coins(Base):
    __tablename__ = 'tb_coins'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String)
    symbol = Column(String)
    data_added = Column(Text)
    last_updated = Column(Text)
    price = Column(Float)
    volume_24h = Column(Float)
    circulating_supply = Column(Float)
    total_supply = Column(Float)
    max_supply = Column(Float)
    volume_24h = Column(Float)
    percent_change_1h = Column(Float)
    percent_change_24h = Column(Float)
    percent_change_7d = Column(Float)
   
    def start(self):
        db = DBSession()
        db.start_db_session()
        Base.metadata.create_all(db.engine)
        print ('\nTable created on database')
        return db.session, db.engine