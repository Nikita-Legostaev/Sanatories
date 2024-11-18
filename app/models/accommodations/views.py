from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.accommodations.repositories import AccommodationsRepositories
from app.models.accommodations.shemas import SNewAccommodations


router = APIRouter(
    prefix="/accommodations",
    tags=["accommodations"],
)


@router.get("/all")
async def get_all_accommodations(offset: int = 0, limit: int = 10):
    all_accommodations = await AccommodationsRepositories.get_all()
    return all_accommodations[offset:limit]

@router.post("/add_accommodations")
async def add_accommodations(
    SNewAccommodations: SNewAccommodations,
):
    added_accommodations = await AccommodationsRepositories.add(
        room_type=SNewAccommodations.room_type,
        capacity=SNewAccommodations.capacity,
        daily_rate=SNewAccommodations.daily_rate,
    )
    return {"detail": "Успешно"}


@router.delete("/{accommodations_id}")
async def remove_accommodations(
    accommodations_id: int,
):
    accommodations = await AccommodationsRepositories.find_one_or_none(id=accommodations_id)
    if not accommodations:
        raise HTTPException(status_code=404, detail="Не найдена")
    await AccommodationsRepositories.delete(id=accommodations_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{accommodations_id}")
async def update_accommodations(
    accommodations_id: int,
    SNewAccommodations: SNewAccommodations,  
    ):
    accommodations = await AccommodationsRepositories.find_by_id(id=accommodations_id)
    if not accommodations:
        raise HTTPException(status_code=404, detail="Не найден")
    await AccommodationsRepositories.update(id=accommodations_id, **SNewAccommodations.model_dump())
    return {"detail": "Успешно изменёно"}
