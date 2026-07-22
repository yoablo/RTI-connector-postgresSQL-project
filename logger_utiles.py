from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection
from loguru import logger


def log_source_ID_change(text: str,detection: P_Tactical_Sensor_PSM_C_Detection):
    logger.info(f"!!!!! {text}: {detection.A_sourceID.A_platformId}.{detection.A_sourceID.A_systemId}.{detection.A_sourceID.A_moduleId}")

def log_Receiving_and_publishing(text: str, detection: P_Tactical_Sensor_PSM_C_Detection, more_info: str):
    logger.info(f"{text}: {detection.A_detectionUniqueID.A_msb} , {detection.A_detectionUniqueID.A_lsb}, {more_info}")