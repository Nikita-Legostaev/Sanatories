from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.rooms.repositpries import RoomsRepositories
from app.models.rooms.shemas import SNewRoom


router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
)


@router.get("/all")
async def get_all_rooms(offset: int = 0, limit: int = 10):
    all_client = await RoomsRepositories.get_all()
    return all_client[offset:limit]

@router.post("/add")
async def add_room(
    room: SNewRoom,
):
    added_client = await RoomsRepositories.add(
        purpose = room.purpose,
        capacity = room.capacity
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{room_id}")
async def remove_room(
    room_id: int,
):
    room = await RoomsRepositories.find_one_or_none(id=room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Команда не найдена")
    await RoomsRepositories.delete(id=room_id)
    return {"detail": "Команта успешно удалёна"}


@router.patch("/edit/{room_id}")
async def update_room(
    room_id: int,
    SRoom: SNewRoom,  
    ):
    room = await RoomsRepositories.find_by_id(id=room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    await RoomsRepositories.update(id=room_id, **SRoom.model_dump())
    return {"detail": "Комната успешно изменёна"}
