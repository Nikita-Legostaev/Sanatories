from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.clients.views import get_all_clients
from app.models.rooms.views import get_all_rooms 
from app.models.staff.views import get_all_staff
from app.models.accommodations.views import get_all_accommodations
from app.models.procedure_appointment.views import get_all_procedure_appointment
from app.models.accommodations_usage.views import get_all_accommodations_usage
from app.models.bookings.views import get_all_bookings
from app.models.procedures.views import get_all_procedure
from app.models.room_usage.views import get_all_room_usage
from app.models.clients.views import all_count

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/clients')
async def get_students_html(request: Request, clients=Depends(get_all_clients)):
    return templates.TemplateResponse(name='clients.html', context={'request': request, 'clients': clients})

@router.get('/rooms')
async def get_rooms_html(request: Request, rooms=Depends(get_all_rooms)):
    return templates.TemplateResponse(name='rooms.html', context={'request': request, 'rooms': rooms})

@router.get('/staff')
async def get_staff_html(request: Request, staff=Depends(get_all_staff)):
    return templates.TemplateResponse(name='staff.html', context={'request': request, 'staff': staff})

@router.get('/accommodations')
async def get_accommodations_html(request: Request, accommodations=Depends(get_all_accommodations)):
    return templates.TemplateResponse(name='accommodations.html', context={'request': request, 'accommodations': accommodations})

@router.get('/procedure_appointment')
async def get_procedure_appointment_html(request: Request, procedure_appointment=Depends(get_all_procedure_appointment)):
    return templates.TemplateResponse(name='procedure_appointment.html', context={'request': request, 'procedure_appointment': procedure_appointment})

@router.get('/accommodations_usage')
async def get_accommodations_usage_html(request: Request, accommodations_usage=Depends(get_all_accommodations_usage)):
    return templates.TemplateResponse(name='accommodations_usage.html', context={'request': request, 'accommodations_usage': accommodations_usage})

@router.get('/bookings')
async def get_bookings_html(request: Request, bookings=Depends(get_all_bookings)):
    return templates.TemplateResponse(name='bookings.html', context={'request': request, 'bookings': bookings})

@router.get('/procedures')
async def get_procedures_html(request: Request, procedures=Depends(get_all_procedure)):
    return templates.TemplateResponse(name='procedures.html', context={'request': request, 'procedures': procedures})

@router.get('/room_usage')
async def get_room_usage_html(request: Request, room_usage=Depends(get_all_room_usage)):
    return templates.TemplateResponse(name='room_usage.html', context={'request': request, 'room_usage': room_usage})


@router.get("/count_records")
async def count_records(request: Request, all_count=Depends(all_count)):
    return templates.TemplateResponse("count_records.html", {"request": request, "all_count": all_count})