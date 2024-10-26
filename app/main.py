from fastapi import FastAPI
from app.models.clients.views import router as client_view
from app.models.bookings.views import router as bookings_view
from app.models.rooms.views import router as rooms_view

app = FastAPI()

app.include_router(client_view)
app.include_router(bookings_view)
app.include_router(rooms_view)

