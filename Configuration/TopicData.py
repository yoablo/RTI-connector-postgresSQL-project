from enum import Enum

from auto_idl_types.Detection import P_Tactical_Sensor_PSM_C_Detection
from auto_idl_types.DetectionAps import P_Tactical_Sensor_PSM_C_Detection_Aps
from auto_idl_types.DetectionOptronics import P_Tactical_Sensor_PSM_C_Detection_Optronics
from auto_idl_types.Position import P_Navigation_PSM_C_Position
from auto_idl_types.ResourceSpecification import P_Maintenance_PSM_C_Resource_Specification
from auto_idl_types.RotMount import P_Mount_PSM_C_Rot_Mount
from auto_idl_types.TacticalSensor import P_Tactical_Sensor_PSM_C_Tactical_Sensor
from auto_idl_types.TacticalSensorSpecification import P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification


class structEnum(Enum):
    Detection = 0,
    Detection_Aps = 1,
    Detection_Optronics = 2,
    Position = 3,
    Resource_Specification = 4,
    Rot_Mount = 5,
    Tactical_Sensor = 6,
    Tactical_Sensor_Specification = 7


class StructData:
    def __init__(self, topic_name, struct_type):
        self.topic_name = topic_name
        self.struct_type = struct_type


topic_data_dict = {
    structEnum.Detection: StructData(
        "P_Tactical_Sensor_PSM::C_Detection", P_Tactical_Sensor_PSM_C_Detection),
    structEnum.Detection_Aps: StructData(
        "P_Tactical_Sensor_PSM::C_Detection_Aps", P_Tactical_Sensor_PSM_C_Detection_Aps),
    structEnum.Detection_Optronics: StructData(
        "P_Tactical_Sensor_PSM::C_Detection_Optronics", P_Tactical_Sensor_PSM_C_Detection_Optronics),
    structEnum.Position: StructData(
        "P_Navigation_PSM::C_Position", P_Navigation_PSM_C_Position),
    structEnum.Resource_Specification: StructData(
        "P_Maintenance_PSM::C_Resource_Specification", P_Maintenance_PSM_C_Resource_Specification),
    structEnum.Rot_Mount: StructData(
        "P_Mount_PSM::C_Rot_Mount", P_Mount_PSM_C_Rot_Mount),
    structEnum.Tactical_Sensor: StructData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor", P_Tactical_Sensor_PSM_C_Tactical_Sensor),
    structEnum.Tactical_Sensor_Specification: StructData(
        "P_Tactical_Sensor_PSM::C_Tactical_Sensor_Specification", P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification)
}
