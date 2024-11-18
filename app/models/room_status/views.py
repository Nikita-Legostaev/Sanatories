from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.room_status.repositpries import RoomStatusRepositories
from app.models.room_status.shemas import SNewRoomStatus


router = APIRouter(
    prefix="/room_status",
    tags=["room_status"],
)


@router.get("/all")
async def get_all_room_status(offset: int = 0, limit: int = 10):
    all_room_status = await RoomStatusRepositories.get_all()
    return all_room_status[offset:limit]

@router.post("/add_room_status")
async def add_room_status(
    SNewRoomStatus: SNewRoomStatus,
):
    added_room_status = await RoomStatusRepositories.add(
        room_id=SNewRoomStatus.room_id,
        booking_id=SNewRoomStatus.booking_id,
        status=SNewRoomStatus.status,
    )
    return {"detail": "Успешно"}


@router.delete("/{room_status_id}")
async def remove_room_status(
    room_status_id: int,
):
    room_status = await RoomStatusRepositories.find_one_or_none(id=room_status_id)
    if not room_status:
        raise HTTPException(status_code=404, detail="Не найдена")
    await RoomStatusRepositories.delete(id=room_status_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{room_status_id}")
async def update_room_status(
    room_status_id: int,
    SNewRoomStatus: SNewRoomStatus,  
    ):
    room_status = await RoomStatusRepositories.find_by_id(id=room_status_id)
    if not room_status:
        raise HTTPException(status_code=404, detail="Не найден")
    await RoomStatusRepositories.update(id=room_status_id, **SNewRoomStatus.model_dump())
    return {"detail": "Успешно изменёно"}
