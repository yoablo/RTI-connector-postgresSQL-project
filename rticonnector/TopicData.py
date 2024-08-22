from enum import Enum

from rticonnector.idl_types.Detection import P_Tactical_Sensor_PSM_C_Detection
from rticonnector.idl_types.DetectionAps import P_Tactical_Sensor_PSM_C_Detection_Aps
from rticonnector.idl_types.DetectionOptronics import P_Tactical_Sensor_PSM_C_Detection_Optronics
from rticonnector.idl_types.Position import P_Navigation_PSM_C_Position
from rticonnector.idl_types.ResourceSpecification import P_Maintenance_PSM_C_Resource_Specification
from rticonnector.idl_types.RotMount import P_Mount_PSM_C_Rot_Mount
from rticonnector.idl_types.TacticalSensor import P_Tactical_Sensor_PSM_C_Tactical_Sensor
from rticonnector.idl_types.TacticalSensorSpecification import P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification


#TODO change the name of the class to TopicEnum
class StructEnum(Enum):
    DETECTION = 0,
    DETECTION_APS = 1,
    DETECTION_OPTRONICS = 2,
    POSITION = 3,
    RESOURCE_SPECIFICATION = 4,
    ROT_MOUNT = 5,
    TACTICAL_SENSOR = 6,
    TACTICAL_SENSOR_SPECIFICATION = 7


class StructData:
    def __init__(self, topic_name, topic_struct):
        self.topic_name = topic_name
        self.topic_struct = topic_struct


topic_data_dict = {
    StructEnum.DETECTION: StructData(
        "P_Tactical_Sensor_PSM::C_Detection", P_Tactical_Sensor_PSM_C_Detection),
    StructEnum.DETECTION_APS: StructData(
        "P_Tactical_Sensor_PSM::C_Detection_Aps", P_Tactical_Sensor_PSM_C_Detection_Aps),
    StructEnum.DETECTION_OPTRONICS: StructData(
        "P_Tactical_Sensor_PSM::C_Detection_Optronics", P_Tactical_Sensor_PSM_C_Detection_Optronics),
    StructEnum.POSITION: StructData(
        "P_Navigation_PSM::C_Position", P_Navigation_PSM_C_Position),
    StructEnum.RESOURCE_SPECIFICATION: StructData(
        "P_Maintenance_PSM::C_Resource_Specification", P_Maintenance_PSM_C_Resource_Specification),
    StructEnum.ROT_MOUNT: StructData(
        "P_Mount_PSM::C_Rot_Mount", P_Mount_PSM_C_Rot_Mount),
    StructEnum.TACTICAL_SENSOR: StructData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor", P_Tactical_Sensor_PSM_C_Tactical_Sensor),
    StructEnum.TACTICAL_SENSOR_SPECIFICATION: StructData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor_Specification", P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification)
}
