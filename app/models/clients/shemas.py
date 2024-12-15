
from pydantic import BaseModel, ConfigDict
from datetime import date
from sqlalchemy import Date


class SNewClient(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fullname: str
    birth_date: date
    email: str
    address: str

class SSeacrhClient(BaseModel):
    fullname: str | None
    birth_date: date | None
    email: str | None
    address: str | None