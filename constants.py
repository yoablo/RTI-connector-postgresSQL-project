from dotenv import load_dotenv
from os import getenv
from enum import Enum
from redis import Redis

load_dotenv(override = False)


class ClassificationName(Enum):
    NOGA = "NOGA"
    ATR = "ATR"
    WINDCOAT = "WINDCOAT"
    AT = "AT"


class Random16DigitID(Enum):
    ONE_NUMBER = 3001697090449141
    SECOND_NUMBER = 13533879590735665
    THIRD_NUMBER = 1691298520696870


class SystemStateConstants(Enum):
    ALL_DETECTIONS = 0
    CRITICAL_DETECTIONS = 1


DELAY_SECONDS = 1
NANOSECONDS_CONVERSION_TO_SECONDS = 1_000_000_000
TRUELY_RANDOM_16_DIGIT_ID_START_VAR = 1000000000000000
TRUELY_RANDOM_16_DIGIT_ID_END_VAR = 9999999999999999
QOS_FILE = "rticonnector/Configuration/BarakQosProfile.xml"
CHANCE_FOR_ID = 0.5
ENGINE_STRING = "TRUNCATE TABLE detections RESTART IDENTITY"

DB_HOST = getenv("DB_HOST", "localhost")
DB_PORT = getenv("DB_PORT", "5432")
DATABASE_URL_DEFAULT = f"postgresql+psycopg2://postgres:postgres@{DB_HOST}:{DB_PORT}/dds_project"
DATABASE_URL = getenv("DATABASE_URL", DATABASE_URL_DEFAULT)

SYSTEM_MOD_VARIABLE = "system_mod_variable"
DEFAULT_SYSTEM_MOD_VARIABLE = SystemStateConstants.CRITICAL_DETECTIONS.value
DETECTION_SOURCEID_PLATFORMID = 1
DETECTION_SOURCEID_SYSTEMID = 14
DETECTION_SOURCEID_MODULEID = 9
FASTAPI_SERVER_HOST = getenv("FASTAPI_HOST", "127.0.0.1")
FASTAPI_SERVER_PORT = int(getenv("FASTAPI_PORT", "8000"))

REDIS_CLIENT = Redis(
    host = getenv("REDIS_HOST", "localhost"),
    port = int(getenv("REDIS_PORT", "6379")),
    decode_responses = False,
)
