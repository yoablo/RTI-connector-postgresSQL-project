from enum import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String
from rticonnector import topic_data
from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection

delay_seconds = 1
nanoseconds_conversion_to_seconds = 1_000_000_000
truely_random_16_digit_ID_start_var = 1000000000000000
truely_random_16_digit_ID_end_var = 9999999999999999
qos_file = "rticonnector/Configuration/BarakQosProfile.xml"
topic1 = topic_data.TopicEnum.DETECTION
detection1 = P_Tactical_Sensor_PSM_C_Detection()
chance_for_ID = 0.5
engine_string = "TRUNCATE TABLE detections RESTART IDENTITY"


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
