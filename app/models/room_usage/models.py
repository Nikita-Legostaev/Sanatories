from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Room_usage(Base):
    __tablename__='room_usage'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    procedure_id: Mapped[int] = mapped_column(ForeignKey("procedures.id"))
    staff_id: Mapped[int] = mapped_column(ForeignKey("staff.id"))
    date: Mapped[Date] = mapped_column(type_=Date)
