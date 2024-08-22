from enum import Enum

from rticonnector.idl_types.Detection import P_Tactical_Sensor_PSM_C_Detection
from rticonnector.idl_types.DetectionAps import P_Tactical_Sensor_PSM_C_Detection_Aps
from rticonnector.idl_types.DetectionOptronics import P_Tactical_Sensor_PSM_C_Detection_Optronics
from rticonnector.idl_types.Position import P_Navigation_PSM_C_Position
from rticonnector.idl_types.ResourceSpecification import P_Maintenance_PSM_C_Resource_Specification
from rticonnector.idl_types.RotMount import P_Mount_PSM_C_Rot_Mount
from rticonnector.idl_types.TacticalSensor import P_Tactical_Sensor_PSM_C_Tactical_Sensor
from rticonnector.idl_types.TacticalSensorSpecification import P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification


class TopicEnum(Enum):
    DETECTION = 0,
    DETECTION_APS = 1,
    DETECTION_OPTRONICS = 2,
    POSITION = 3,
    RESOURCE_SPECIFICATION = 4,
    ROT_MOUNT = 5,
    TACTICAL_SENSOR = 6,
    TACTICAL_SENSOR_SPECIFICATION = 7


class TopicData:
    def __init__(self, topic_name, topic_struct):
        self.topic_name = topic_name
        self.topic_struct = topic_struct


topic_data_dict = {
    TopicEnum.DETECTION: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection", P_Tactical_Sensor_PSM_C_Detection),
    TopicEnum.DETECTION_APS: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection_Aps", P_Tactical_Sensor_PSM_C_Detection_Aps),
    TopicEnum.DETECTION_OPTRONICS: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection_Optronics", P_Tactical_Sensor_PSM_C_Detection_Optronics),
    TopicEnum.POSITION: TopicData(
        "P_Navigation_PSM::C_Position", P_Navigation_PSM_C_Position),
    TopicEnum.RESOURCE_SPECIFICATION: TopicData(
        "P_Maintenance_PSM::C_Resource_Specification", P_Maintenance_PSM_C_Resource_Specification),
    TopicEnum.ROT_MOUNT: TopicData(
        "P_Mount_PSM::C_Rot_Mount", P_Mount_PSM_C_Rot_Mount),
    TopicEnum.TACTICAL_SENSOR: TopicData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor", P_Tactical_Sensor_PSM_C_Tactical_Sensor),
    TopicEnum.TACTICAL_SENSOR_SPECIFICATION: TopicData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor_Specification", P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification)
}
