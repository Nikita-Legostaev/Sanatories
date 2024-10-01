from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class RoomStatus(Base):
    __tablename__ = 'room_status'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'), nullable=True)
    booking_id: Mapped[int] = mapped_column(ForeignKey('bookings.id'), nullable=True)
    status: Mapped[str]  