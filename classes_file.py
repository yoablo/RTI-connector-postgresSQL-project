from enum import Enum

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String


class ClassificationName(Enum):
    NOGA = "NOGA"
    ATR = "ATR"
    WINDOAT = "WINDOAT"
    AT = "AT"


class Random16DigitID(Enum):
    ONE_NUMBER = 3001697090449141
    SECOND_NUMBER = 13533879590735665
    THIRD_NUMBER = 1691298520696870


class Base(DeclarativeBase):
    pass


class DetectionRecord(Base):
    __tablename__ = "detections"

    table_id: Mapped[int] = mapped_column(Integer, primary_key = True)

    msb: Mapped[int] = mapped_column(BigInteger)
    lsb: Mapped[int] = mapped_column(BigInteger)
    seconds: Mapped[int] = mapped_column(BigInteger)
    class_name: Mapped[str] = mapped_column(String)
