from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter
from typing import Optional
from datetime import date

from app.models.clients.repositories import ClientRepository
from app.models.accommodations.repositories import AccommodationsRepositories
from app.models.accommodations_usage.repositpries import AccommodationsUsageRepositories
from app.models.bookings.repositories import BookingRepositories
from app.models.procedure_appointment.repositories import ProcedureAppointmentRepositories
from app.models.procedures.repositpries import ProcedureRepositories
from app.models.room_usage.repositpries import RoomUsageRepositories
from app.models.rooms.repositpries import RoomsRepositories
from app.models.staff.repositpries import StaffRepositories
from app.models.clients.shemas import SNewClient, SSeacrhClient


router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)


@router.get("/all")
async def get_all_clients(offset: int = 0, limit: int = 10):
    all_client = await ClientRepository.get_all()
    return all_client[offset:limit]

@router.post("/add_client")
async def add_client(
    client: SNewClient,
):
    added_client = await ClientRepository.add(
        address=client.address,
        birth_date=client.birth_date,
        email=client.email,
        fullname=client.fullname,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{client_id}")
async def remove_client(
    client_id: int,
):
    booking = await ClientRepository.find_one_or_none(id=client_id)
    await ClientRepository.delete(id=client_id)
    return {"detail": "Клиент успешно удалён"}


@router.patch("/edit/{client_id}")
async def update_client(
    client_id: int,
    SClient: SNewClient,  
    ):
    client = await ClientRepository.find_by_id(id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    await ClientRepository.update(id=client_id, **SClient.model_dump())
    return {"detail": "Клиент успешно изменён"}


@router.get("/search/")
async def search_client(
    offset: int = 0, limit: int = 10,
    fullname: str = None, 
    birth_date: date = None, 
    email: str = None, 
    address: str = None, 
):
    filter_params = {key: value for key, value in locals().items() if value is not None and key not in ['offset', 'limit']}
    
    client = await ClientRepository.get_all(**filter_params)
    
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    return client[offset:offset + limit]


@router.get("/count")
async def all_count():
    count_client = await ClientRepository.count()
    count_accommodations = await AccommodationsRepositories.count()
    count_accommodations_usage = await AccommodationsUsageRepositories.count()
    count_bookings = await BookingRepositories.count()
    count_procedure_appointment = await ProcedureAppointmentRepositories.count()
    count_procedures = await ProcedureRepositories.count()
    count_room_usage = await RoomUsageRepositories.count()
    count_rooms = await RoomsRepositories.count()
    count_staff = await StaffRepositories.count()
    all_count = count_client + count_accommodations + count_accommodations_usage + count_bookings + count_procedure_appointment + count_procedures + count_room_usage + count_rooms + count_staff
    return {"all_count": all_count,
            "count_client": count_client,
            "count_accommodations": count_accommodations,
            "count_accommodations_usage": count_accommodations_usage,
            "count_bookings": count_bookings,
            "count_procedure_appointment": count_procedure_appointment,
            "count_procedures": count_procedures,
            "count_room_usage": count_room_usage,
            "count_rooms": count_rooms,
            "count_staff": count_staff
            }