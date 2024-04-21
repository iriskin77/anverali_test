from pydantic import BaseModel
from typing import Optional


class PersonContactRequest(BaseModel):

    bitrix_id: int
    name: str


class PersonContactResponse(BaseModel):

    bitrix_id: int
    name: str
    gender: str
