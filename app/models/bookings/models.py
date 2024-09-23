from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Bookings(Base):
    __tablename__='bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    accommodation_id: Mapped[int] = mapped_column(ForeignKey("accommodations.id"))
    check_in_date: Mapped[Date] = mapped_column(type_=Date)
    check_out_date: Mapped[Date] = mapped_column(type_=Date)
    status: Mapped[int]