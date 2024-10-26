from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.bookings.repositories import BookingRepositories


router = APIRouter(
    prefix="/bookings",
    tags=["booking"],
)


@router.get("/all")
async def get_all_bookings(offset: int = 0, limit: int = 10):
    all_booking = await BookingRepositories.get_all()
    return all_booking[offset:limit]