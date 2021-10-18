from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    id: int = Field(..., ge=0, description="Id must be more than or equal to 0")
    value: Optional[str] = Field(None)


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    timestamp: int = Field(...)

    class Config:
        orm_mode = True


class ItemUpdate(Item):
    pass
