"""
Create the database engine for the app. Each request will use its local session
from the database.
"""

import sqlmodel

from app import config

# create sqlite database
sqlite_url = f"sqlite:///{config.settings.database.database}"

engine = sqlmodel.create_engine(sqlite_url, echo=config.settings.database.echo)


def get_db():
    """
    Create a database local database session to be used in
    FastAPI.
    """
    db = sqlmodel.Session(engine)
    try:
        yield db
    finally:
        db.close()


def migrate():
    """
    Do the migration
    """

    # importing domain models just for doing migration
    # because the classes should be loaded before calling
    # the migration.
    from app import domain as _

    sqlmodel.SQLModel.metadata.create_all(engine)
