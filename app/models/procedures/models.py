from sqlalchemy import Integer, String, Date
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Procedures(Base):
    __tablename__='procedures'

    id: Mapped[int] = mapped_column(primary_key=True)
    procedure_name: Mapped[str]
    description: Mapped[str]
    cost: Mapped[int]

    