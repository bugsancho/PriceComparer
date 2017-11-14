from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from PriceComparer.persistance.models.base_entity import DeclarativeBase

from PriceComparer.settings import DATABASE


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    print('Crteatin engine------------------')
    return create_engine(URL(**DATABASE))


def ensure_database_exists(engine=None):
    """"""
    if not engine:
        engine = db_connect()
    DeclarativeBase.metadata.create_all(engine)
