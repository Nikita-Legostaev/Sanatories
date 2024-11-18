from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.procedures.repositpries import ProcedureRepositories
from app.models.procedures.shemas import SNewProcedure


router = APIRouter(
    prefix="/procedure",
    tags=["procedure"],
)


@router.get("/all")
async def get_all_procedure(offset: int = 0, limit: int = 10):
    all_procedure = await ProcedureRepositories.get_all()
    return all_procedure[offset:limit]

@router.post("/add_procedure")
async def add_procedure(
    SNewProcedure: SNewProcedure,
):
    added_procedure = await ProcedureRepositories.add(
        procedure_name=SNewProcedure.procedure_name,
        description=SNewProcedure.description,
        cost=SNewProcedure.cost,
    )
    return {"detail": "Успешно"}


@router.delete("/{procedure_id}")
async def remove_procedure(
    procedure_id: int,
):
    procedure = await ProcedureRepositories.find_one_or_none(id=procedure_id)
    if not procedure:
        raise HTTPException(status_code=404, detail="Не найдена")
    await ProcedureRepositories.delete(id=procedure_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{procedure_id}")
async def update_procedure(
    procedure_id: int,
    SNewProcedure: SNewProcedure,  
    ):
    procedure = await ProcedureRepositories.find_by_id(id=procedure_id)
    if not procedure:
        raise HTTPException(status_code=404, detail="Не найден")
    await ProcedureRepositories.update(id=procedure_id, **SNewProcedure.model_dump())
    return {"detail": "Успешно изменёно"}
