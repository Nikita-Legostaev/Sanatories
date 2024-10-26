
from pydantic import BaseModel, ConfigDict

class SNewRoom(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    purpose: str
    capacity: int