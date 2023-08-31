from sqlalchemy import orm
from sqlalchemy import Integer, String


class Base(orm.DeclarativeBase):
    """abstract model for all classes"""

    id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        autoincrement=True
    )


class Hotel(Base):
    """hotel database model"""

    __tablename__ = 'hotel'

    name: orm.Mapped[str] = orm.mapped_column(String(length=127))
    phone: orm.Mapped[int] = orm.mapped_column(Integer)
    stars: orm.Mapped[int] = orm.mapped_column(Integer)
