from pydantic import BaseModel
from typing import Optional


class MenNames(BaseModel):
    id: Optional[int]
    name_man: str
    gender: Optional[str]


class WomenNames(BaseModel):
    id: Optional[int]
    name_woman: str
    gender: Optional[str]


class ContactRequest(BaseModel):

    id: int
    name: str


class ContactResponse(BaseModel):

    id: int
    name: str
    gender: str
