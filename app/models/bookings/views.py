from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.bookings.repositories import BookingRepositories
from app.models.bookings.shemas import SNewBooking


router = APIRouter(
    prefix="/bookings",
    tags=["booking"],
)


@router.get("/all")
async def get_all_bookings(offset: int = 0, limit: int = 10):
    all_booking = await BookingRepositories.get_all()
    return all_booking[offset:limit]


@router.post("/add_bookings")
async def add_bookings(
    SNewBooking: SNewBooking,
):
    added_bookings = await BookingRepositories.add(
        client_id=SNewBooking.client_id,
        accommodation_id=SNewBooking.accommodation_id,
        check_in_date=SNewBooking.check_in_date,
        check_out_date=SNewBooking.check_out_date,
        status=SNewBooking.status,  
    )
    return {"detail": "Успешно"}


@router.delete("/{bookings_id}")
async def remove_bookings(
    bookings_id: int,
):
    bookings = await BookingRepositories.find_one_or_none(id=bookings_id)
    if not bookings:
        raise HTTPException(status_code=404, detail="Не найдена")
    await BookingRepositories.delete(id=bookings_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{bookings_id}")
async def update_bookings(
    bookings_id: int,
    SNewBooking: SNewBooking,  
    ):
    bookings = await BookingRepositories.find_by_id(id=bookings_id)
    if not bookings:
        raise HTTPException(status_code=404, detail="Не найден")
    await BookingRepositories.update(id=bookings_id, **SNewBooking.model_dump())
    return {"detail": "Успешно изменёно"}
