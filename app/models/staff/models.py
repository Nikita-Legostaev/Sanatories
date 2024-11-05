from sqlalchemy import Integer, String, Date
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Staff(Base):
    __tablename__='staff'

    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    fullname: Mapped[str]
    position: Mapped[str]
    phone: Mapped[str]

    