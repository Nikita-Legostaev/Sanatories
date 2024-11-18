from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.clients.views import router as client_view
from app.models.bookings.views import router as bookings_view
from app.models.accommodations.views import router as accommodations_view
from app.models.rooms.views import router as rooms_view
from app.models.staff.views import router as staff_view
from app.models.procedures.views import router as procedures_view
from app.models.room_usage.views import router as room_usage_view
from app.models.procedure_appointment.views import router as procedure_appointment_view
from app.models.accommodations_usage.views import router as accommodations_usage_view
from app.models.room_status.views import router as room_status_router

from app.pages.router import router as page_views

app = FastAPI()

app.include_router(client_view)
app.include_router(bookings_view)
app.include_router(rooms_view)
app.include_router(accommodations_view)
app.include_router(staff_view)
app.include_router(procedures_view)
app.include_router(room_usage_view)
app.include_router(procedure_appointment_view)
app.include_router(accommodations_usage_view)
app.include_router(room_status_router) 
app.include_router(page_views)




