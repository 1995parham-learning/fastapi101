"""
Create the database engine for the app. Each request will use its local session
from the database.
"""

import sqlmodel

# importing domain models just for doing migration
# because the classes should be loaded before calling
# the migration.
from app import config
from app import domain as _

# create sqlite database
sqlite_url = f"sqlite:///{config.settings.database.database}"

engine = sqlmodel.create_engine(sqlite_url, echo=config.settings.database.echo)

# python modules are signleton and here we do the migration.
sqlmodel.SQLModel.metadata.create_all(engine)
