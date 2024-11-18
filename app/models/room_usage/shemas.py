from pydantic import BaseModel, ConfigDict
from sqlalchemy import Date
from datetime import date


class SNewRoomUsage(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    room_id: int
    procedure_id: int
    staff_id: int
    date: date