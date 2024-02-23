from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class ContactBase(BaseModel):
    forename: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: Optional[str] = Field(max_length=50)
    phone_number: str = Field(max_length=20)
    born_date: date


class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=250)
    password: str = Field(min_length=8, max_length=16)

