from app.repositories.base import BaseRepositories
from app.models.rooms.models import Rooms



class RoomsRepositories(BaseRepositories):
    model = Rooms