from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.accommodations_usage.model import Accommodations_usage 
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class AccommodationsUsageRepositories(BaseRepositories):
    model = Accommodations_usage