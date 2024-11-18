from pydantic import BaseModel, ConfigDict
from sqlalchemy import Date
from datetime import date

class SNewAccommodationsUsage(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    accommodations_id: int
    room_type: str
    start_data: date
    end_data: date
    capacity: int