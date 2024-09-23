from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Accommodations_usage(Base):
    __tablename__='accommodations_usage'

    id: Mapped[int] = mapped_column(primary_key=True) 
    accommodations_id: Mapped[int] = mapped_column(ForeignKey("accommodations.id"))
    room_type: Mapped[str]
    start_data: Mapped[Date] = mapped_column(type_=Date)
    end_data: Mapped[Date] = mapped_column(type_=Date)
    capacity: Mapped[int]