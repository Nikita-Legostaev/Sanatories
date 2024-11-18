from pydantic import BaseModel, ConfigDict
from sqlalchemy import Date
from datetime import date

class SNewBooking(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    client_id: int
    accommodation_id: int
    check_in_date: int
    check_out_date: date
    status: int