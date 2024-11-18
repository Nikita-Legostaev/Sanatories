from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.room_usage.models import Room_usage 
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class RoomUsageRepositories(BaseRepositories):
    model = Room_usage