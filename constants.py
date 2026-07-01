from dotenv import load_dotenv
import os

from enum import Enum

from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection

load_dotenv()

DELAY_SECONDS = 1
NANOSECONDS_CONVERSION_TO_SECONDS = 1_000_000_000
TRUELY_RANDOM_16_DIGIT_ID_START_VAR = 1000000000000000
TRUELY_RANDOM_16_DIGIT_ID_END_VAR = 9999999999999999
QOS_FILE = "rticonnector/Configuration/BarakQosProfile.xml"
DETECTION = P_Tactical_Sensor_PSM_C_Detection()
CHANCE_FOR_ID = 0.5
ENGINE_STRING = "TRUNCATE TABLE detections RESTART IDENTITY"
DATABASE_URL_DEFAULT = "postgresql+psycopg2://postgres:postgres@localhost:5432/dds_project"
DATABASE_URL = os.getenv("DATABASE_URL", DATABASE_URL_DEFAULT)


class ClassificationName(Enum):
    NOGA = "NOGA"
    ATR = "ATR"
    WINDOAT = "WINDOAT"
    AT = "AT"


class Random16DigitID(Enum):
    ONE_NUMBER = 3001697090449141
    SECOND_NUMBER = 13533879590735665
    THIRD_NUMBER = 1691298520696870
