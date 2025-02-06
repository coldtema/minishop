from fastapi import APIRouter, Path
from items import crud
from typing import Annotated

router = APIRouter(prefix="/items")

@router.get("/")
def get_item_by_id():
    return "list of items"

@router.get("/latest")
def get_item_by_id():
    return "latest_item"

@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(gt=0, lt=1_000_000)]):
    return crud.get_item_by_id(item_id)
