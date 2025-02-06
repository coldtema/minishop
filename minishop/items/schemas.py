from pydantic import BaseModel, Field
from typing import Annotated

class Items(BaseModel):
    item_id: Annotated[int, Field(gt=0, lt=1_000_000)]
