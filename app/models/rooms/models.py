from sqlalchemy import Integer, String, Date
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Rooms(Base):
    __tablename__='rooms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    purpose: Mapped[str]
    capacity: Mapped[int]