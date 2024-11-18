from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.room_usage.repositpries import RoomUsageRepositories
from app.models.room_usage.shemas import SNewRoomUsage


router = APIRouter(
    prefix="/room_usage",
    tags=["room_usage"],
)


@router.get("/all")
async def get_all_room_usage(offset: int = 0, limit: int = 10):
    all_room_usage = await RoomUsageRepositories.get_all()
    return all_room_usage[offset:limit]

@router.post("/add_room_usage")
async def add_room_usage(
    SNewRoomUsage: SNewRoomUsage,
):
    added_room_usage = await RoomUsageRepositories.add(
        room_id=SNewRoomUsage.room_id,
        procedure_id=SNewRoomUsage.procedure_id,
        staff_id=SNewRoomUsage.staff_id,
        date=SNewRoomUsage.date,
    )
    return {"detail": "Успешно"}


@router.delete("/{room_usage_id}")
async def remove_room_usage(
    room_usage_id: int,
):
    room_usage = await RoomUsageRepositories.find_one_or_none(id=room_usage_id)
    if not room_usage:
        raise HTTPException(status_code=404, detail="Не найдена")
    await RoomUsageRepositories.delete(id=room_usage_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{room_usage_id}")
async def update_room_usage(
    room_usage_id: int,
    SNewRoomUsage: SNewRoomUsage,  
    ):
    room_usage = await RoomUsageRepositories.find_by_id(id=room_usage_id)
    if not room_usage:
        raise HTTPException(status_code=404, detail="Не найден")
    await RoomUsageRepositories.update(id=room_usage_id, **SNewRoomUsage.model_dump())
    return {"detail": "Успешно изменёно"}
