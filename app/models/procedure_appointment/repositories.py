from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.procedure_appointment.models import Procedure_appointment
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class ProcedureAppointmentRepositories(BaseRepositories):
    model = Procedure_appointment