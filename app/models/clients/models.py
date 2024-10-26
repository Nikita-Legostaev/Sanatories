from sqlalchemy import Integer, String, Date
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Clients(Base):
    __tablename__='clients'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 
    fullname: Mapped[str]
    birth_date: Mapped[Date] = mapped_column(type_=Date)
    email: Mapped[str]
    address: Mapped[str]
