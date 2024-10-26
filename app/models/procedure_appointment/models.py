from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Procedure_appointment(Base):
    __tablename__='procedure_appointment'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    procedure_id: Mapped[int] = mapped_column(ForeignKey("procedures.id"))
    staff_id: Mapped[int] = mapped_column(ForeignKey("staff.id"))
    date: Mapped[Date] = mapped_column(type_=Date)