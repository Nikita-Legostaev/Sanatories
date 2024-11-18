
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Date
from datetime import date

class SNewProcedureAppointment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    client_id: int
    procedure_id: int
    staff_id: int
    date: date