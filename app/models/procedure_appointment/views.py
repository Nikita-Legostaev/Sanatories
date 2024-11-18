from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.procedure_appointment.repositories import ProcedureAppointmentRepositories
from app.models.procedure_appointment.shemas import SNewProcedureAppointment


router = APIRouter(
    prefix="/procedure_appointment",
    tags=["procedure_appointment"],
)


@router.get("/all")
async def get_all_procedure_appointment(offset: int = 0, limit: int = 10):
    all_procedure_appointment = await ProcedureAppointmentRepositories.get_all()
    return all_procedure_appointment[offset:limit]

@router.post("/add_procedure_appointment")
async def add_procedure_appointment(
    SNewProcedureAppointment: SNewProcedureAppointment,
):
    added_procedure_appointment = await ProcedureAppointmentRepositories.add(
        client_id=SNewProcedureAppointment.client_id,
        procedure_id=SNewProcedureAppointment.procedure_id,
        staff_id=SNewProcedureAppointment.staff_id,
        date=SNewProcedureAppointment.date,
    )
    return {"detail": "Успешно"}


@router.delete("/{procedure_appointment_id}")
async def remove_procedure_appointment(
    procedure_appointment_id: int,
):
    procedure_appointment = await ProcedureAppointmentRepositories.find_one_or_none(id=procedure_appointment_id)
    if not procedure_appointment:
        raise HTTPException(status_code=404, detail="Не найдена")
    await ProcedureAppointmentRepositories.delete(id=procedure_appointment_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{procedure_appointment_id}")
async def update_procedure_appointment(
    procedure_appointment_id: int,
    SNewProcedureAppointment: SNewProcedureAppointment,  
    ):
    procedure_appointment = await ProcedureAppointmentRepositories.find_by_id(id=procedure_appointment_id)
    if not procedure_appointment:
        raise HTTPException(status_code=404, detail="Не найден")
    await ProcedureAppointmentRepositories.update(id=procedure_appointment_id, **SNewProcedureAppointment.model_dump())
    return {"detail": "Успешно изменёно"}
