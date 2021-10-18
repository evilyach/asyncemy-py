import sys
from typing import List

from fastapi import (
    FastAPI,
    HTTPException,
    Response,
    status
)
import uvicorn

from src.database import database, engine, metadata
import src.database.crud as crud
import src.database.schemas as schemas


metadata.create_all(bind=engine)
app: FastAPI = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def root():
    return "Hello World!"


@app.post("/api/add_item")
async def add_item(item: schemas.ItemCreate, response: Response = status.HTTP_200_OK):
    try:
        result = await crud.add_item(item=item)
    except Exception as error:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return HTTPException(status_code=response.status_code, detail=f"{error}")

    return result


@app.get("/api/get_items", response_model=List[schemas.Item])
async def get_items(skip: int = 0, limit: int = 100):
    return await crud.get_items(skip=skip, limit=limit)


@app.post("/api/update_item")
async def update_item(item: schemas.ItemBase, response: Response = status.HTTP_200_OK):
    try:
        obj = await crud.get_item_by_id(id=item.id)
    except Exception:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(
            status_code=response.status_code,
            detail=f"Could not find object with {id=}"
        )

    return await crud.update_item(item)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        log_level="info",
        reload=True
    )
