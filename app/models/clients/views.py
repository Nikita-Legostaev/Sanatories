from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.clients.repositories import ClientRepository
from app.models.clients.shemas import SNewClient


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