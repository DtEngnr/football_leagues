from Utils.ReqeustSender import test
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append("..")
from model.base import Base
from model.football_league import FootballLeague
from config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_local = SessionLocal()

leagues = test()

for league in leagues:
    new_record = FootballLeague(
        name=league['name'],
        active=league['active'],
        type=league['type'],
        sub_type=league['sub_type'],
        last_played_at=league['last_played_at'],
        country_id=league['country']['country_id'],
        country_name=league['country']['country_name'],
        country_short=league['country']['country_iso2']
    )
    session_local.add(new_record)

session_local.commit()
