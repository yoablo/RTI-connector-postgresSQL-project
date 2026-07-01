from enum import Enum

from rticonnector.idl_types.Maintenance_PSM import (
    P_Maintenance_PSM_C_Resource_Specification,
)
from rticonnector.idl_types.Mount_PSM import P_Mount_PSM_C_Rot_Mount
from rticonnector.idl_types.Navigation_PSM import P_Navigation_PSM_C_Position
from rticonnector.idl_types.Tactical_Sensor_PSM import (
    P_Tactical_Sensor_PSM_C_Detection,
    P_Tactical_Sensor_PSM_C_Detection_Aps,
    P_Tactical_Sensor_PSM_C_Detection_Optronics,
    P_Tactical_Sensor_PSM_C_Tactical_Sensor,
    P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification,
    P_Tactical_Sensor_PSM_C_Detection_C4I,
    P_Tactical_Sensor_PSM_C_C4I_Entity,
    P_Tactical_Sensor_PSM_C_Detection_Fusion,
)


class TopicEnum(Enum):
    DETECTION = (0,)
    DETECTION_APS = (1,)
    DETECTION_OPTRONICS = (2,)
    DETECTION_C4I = (3,)
    POSITION = (4,)
    RESOURCE_SPECIFICATION = (5,)
    ROT_MOUNT = (6,)
    TACTICAL_SENSOR = (7,)
    TACTICAL_SENSOR_SPECIFICATION = (8,)
    C4I_ENTITY = (9,)
    DETECTION_FUSION = 10


class TopicData:
    def __init__(self, topic_name, topic_struct):
        self.topic_name = topic_name
        self.topic_struct = topic_struct


topic_data_dict = {
    TopicEnum.DETECTION: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection", P_Tactical_Sensor_PSM_C_Detection
    ),
    TopicEnum.DETECTION_APS: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection_Aps", P_Tactical_Sensor_PSM_C_Detection_Aps
    ),
    TopicEnum.DETECTION_OPTRONICS: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection_Optronics",
        P_Tactical_Sensor_PSM_C_Detection_Optronics,
    ),
    TopicEnum.DETECTION_C4I: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection_C4I", P_Tactical_Sensor_PSM_C_Detection_C4I
    ),
    TopicEnum.POSITION: TopicData(
        "P_Navigation_PSM::C_Position", P_Navigation_PSM_C_Position
    ),
    TopicEnum.RESOURCE_SPECIFICATION: TopicData(
        "P_Maintenance_PSM::C_Resource_Specification",
        P_Maintenance_PSM_C_Resource_Specification,
    ),
    TopicEnum.ROT_MOUNT: TopicData("P_Mount_PSM::C_Rot_Mount", P_Mount_PSM_C_Rot_Mount),
    TopicEnum.TACTICAL_SENSOR: TopicData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor",
        P_Tactical_Sensor_PSM_C_Tactical_Sensor,
    ),
    TopicEnum.TACTICAL_SENSOR_SPECIFICATION: TopicData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor_Specification",
        P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification,
    ),
    TopicEnum.C4I_ENTITY: TopicData(
        "P_Tactical_Sensor_PSM::C_C4I_Entity", P_Tactical_Sensor_PSM_C_C4I_Entity
    ),
    TopicEnum.DETECTION_FUSION: TopicData(
        "P_Tactical_Sensor_PSM::C_Detection_Fusion",
        P_Tactical_Sensor_PSM_C_Detection_Fusion,
    ),
}
