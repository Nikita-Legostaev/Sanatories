from sqlalchemy import Integer, String, Date
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Accommodations(Base):
    __tablename__='accommodations'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 
    room_type: Mapped[str]
    capacity: Mapped[int]
    daily_rate: Mapped[int]
