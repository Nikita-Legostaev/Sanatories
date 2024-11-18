from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.accommodations_usage.repositpries import AccommodationsUsageRepositories 
from app.models.accommodations_usage.shemas import SNewAccommodationsUsage


router = APIRouter(
    prefix="/accommodations_usage",
    tags=["accommodations_usage"],
)


@router.get("/all")
async def get_all_accommodations_usage(offset: int = 0, limit: int = 10):
    all_accommodations = await AccommodationsUsageRepositories.get_all()
    return all_accommodations[offset:limit]

@router.post("/add_accommodations_usage")
async def add_accommodations_usage(
    SNewAccommodationsUsage: SNewAccommodationsUsage,
):
    added_accommodations_usage = await AccommodationsUsageRepositories.add(
        accommodations_id=SNewAccommodationsUsage.accommodations_id,
        room_type=SNewAccommodationsUsage.room_type,
        start_data=SNewAccommodationsUsage.start_data,
        end_data=SNewAccommodationsUsage.end_data,
        capacity=SNewAccommodationsUsage.capacity, 
    )
    return {"detail": "Успешно"}


@router.delete("/{accommodations_usage_id}")
async def remove_accommodations(
    accommodations_usage_id: int,
):
    accommodations_usage = await AccommodationsUsageRepositories.find_one_or_none(id=accommodations_usage_id)
    if not accommodations_usage:
        raise HTTPException(status_code=404, detail="Не найдена")
    await AccommodationsUsageRepositories.delete(id=accommodations_usage_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/{accommodations_usage_id}")
async def update_accommodations_usage(
    accommodations_usage_id: int,
    SNewAccommodations: SNewAccommodationsUsage,  
    ):
    accommodations_usage = await AccommodationsUsageRepositories.find_by_id(id=accommodations_usage_id)
    if not accommodations_usage:
        raise HTTPException(status_code=404, detail="Не найден")
    await AccommodationsUsageRepositories.update(id=accommodations_usage_id, **SNewAccommodations.model_dump())
    return {"detail": "Успешно изменёно"}
