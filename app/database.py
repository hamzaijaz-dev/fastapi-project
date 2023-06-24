from datetime import datetime as dt

from databases import Database
from pytz import timezone as tz
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

DATABASE_URL = "sqlite:///./fastapi.db"

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("content", String(50)),
    Column("created_at", String(50), default=dt.now(tz("UTC")).strftime("%Y-%m-%d %H:%M")),
)
# Databases query builder

database = Database(DATABASE_URL)
