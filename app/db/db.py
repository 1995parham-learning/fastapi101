"""
Create the database engine for the app. Each request will use its local session
from the database.
"""

import sqlmodel

from app import config

# create sqlite database
sqlite_url = f"sqlite:///{config.settings.database.database}"

engine = sqlmodel.create_engine(sqlite_url, echo=config.settings.database.echo)
