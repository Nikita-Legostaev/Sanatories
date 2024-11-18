from pydantic import BaseModel, ConfigDict

class SNewRoomStatus(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    room_id: int
    booking_id: int
    status: str 