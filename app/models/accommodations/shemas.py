from pydantic import BaseModel, ConfigDict


class SNewAccommodations(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    room_type: str
    capacity: int
    daily_rate: int
