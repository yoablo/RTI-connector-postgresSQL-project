from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String


class Base(DeclarativeBase):
    pass


class DetectionRecord(Base):
    __tablename__ = "detections"

    table_id: Mapped[int] = mapped_column(Integer, primary_key = True)

    msb: Mapped[int] = mapped_column(BigInteger)
    lsb: Mapped[int] = mapped_column(BigInteger)
    seconds: Mapped[int] = mapped_column(BigInteger)
    class_name: Mapped[str] = mapped_column(String)
