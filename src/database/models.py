from sqlalchemy import (
    Column,
    Integer,
    String,
    Table
)

from src.database import metadata


items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("value", String, nullable=True),
    Column("timestamp", Integer)
)
