from datetime import datetime
from typing import List

from src.database import database
from src.database.models import items
from src.database.schemas import Item, ItemCreate, ItemUpdate


async def get_item_by_id(id: int):
    query = items.select().where(id == items.c.id)
    result = await database.fetch_one(query)
    return Item(**dict(result))


async def get_items(limit: int = 100, skip: int = 0) -> List[Item]:
    query = items.select().offset(skip).limit(limit)
    results = await database.fetch_all(query)
    return [Item(**dict(result)) for result in results]


async def add_item(item: ItemCreate) -> Item:
    timestamp = int(datetime.utcnow().timestamp())
    query = items.insert().values(**item.dict(), timestamp=timestamp)
    try:
        await database.execute(query)
    except Exception as e:
        raise Exception(e)
    return Item(**item.dict(), timestamp=timestamp)


async def update_item(item: ItemUpdate) -> Item:
    query = items.update().values(**item.dict()).where(item.id == items.c.id)
    await database.execute(query)
    new_item = await get_item_by_id(item.id)
    return Item(**new_item.dict())
