from .base import BASE
from sqlalchemy import Integer, VARCHAR, Boolean, TIMESTAMP, Column


class FootballLeague(BASE):
    __tablename__ = 'football'
    id = Column(Integer, nullable = False, unique = True, primary_key = True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)
    active = Column(Boolean, nullable=False)
    type = Column(VARCHAR(50), nullable=False)
    sub_type = Column(VARCHAR(50), nullable=False)
    last_played_at = Column(TIMESTAMP, nullable=False, index=True)
    country_id = Column(Integer, nullable = False)
    country_name = Column(VARCHAR(50), nullable=False)
    country_short = Column(VARCHAR(50), nullable=False)
    insert_date = Column(TIMESTAMP, nullable=False)

