from enum import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String
from rticonnector import topic_data
from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection

DELAY_SECONDS = 1
NANOSECONDS_CONVERSION_TO_SECONDS = 1_000_000_000
TRUELY_RANDOM_16_DIGIT_ID_START_VAR = 1000000000000000
TRUELY_RANDOM_16_DIGIT_ID_END_VAR = 9999999999999999
QOS_FILE = "rticonnector/Configuration/BarakQosProfile.xml"
TOPIC1 = topic_data.TopicEnum.DETECTION
DETECTION1 = P_Tactical_Sensor_PSM_C_Detection()
CHANCE_FOR_ID = 0.5
ENGINE_STRING = "TRUNCATE TABLE detections RESTART IDENTITY"


class classification_name(Enum):
    NOGA = "NOGA"
    ATR = "ATR"
    WINDOAT = "WINDOAT"
    AT = "AT"


class Random_16_Digit_ID(Enum):
    num_1 = 3001697090449141
    num_2 = 13533879590735665
    num_3 = 1691298520696870


class Base(DeclarativeBase):
    pass


class DetectionRecord(Base):
    __tablename__ = "detections"

    table_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    msb: Mapped[int] = mapped_column(BigInteger)
    lsb: Mapped[int] = mapped_column(BigInteger)

    seconds: Mapped[int] = mapped_column(BigInteger)
    class_name: Mapped[str] = mapped_column(String)
