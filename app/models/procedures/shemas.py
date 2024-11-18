from pydantic import BaseModel, ConfigDict

class SNewProcedure(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    procedure_name: str
    description: str
    cost: int