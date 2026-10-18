from typing import Annotated

from fastapi import Depends, Query
from pydantic import BaseModel

class PaginationParams(BaseModel):
    page: Annotated[int, Query(default=1,ge=1)]
    per_page: Annotated[int, Query(default=5,ge=1,le=100)]

PaginationDep = Annotated[PaginationParams, Depends()]