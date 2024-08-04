# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from DetectionOptronics.idl
# using RTI Code Generator (rtiddsgen) version 4.3.0.
# The rtiddsgen tool is part of the RTI Connext DDS distribution.
# For more information, type 'rtiddsgen -help' at a command shell
# or consult the Code Generator User's Manual.

from dataclasses import field
import rti.idl as idl
from auto_idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet
from auto_idl_types.Detection import P_Tactical_Sensor_PSM as P_Tactical_Sensor_PSM_Object, P_Tactical_Sensor_PSM_C_Detection

P_LDM_Common = P_LDM_Common_Objet

P_Tactical_Sensor_PSM = P_Tactical_Sensor_PSM_Object


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Optronics")],
    member_annotations={
        'A_opticalErrorRadius': [idl.id(38790974), ],
        'A_absoluteDirectionAvailable': [idl.id(57211100), ],
        'A_sensorLOS': [idl.id(139547978), ],
        'A_sensorLOSAccuracy': [idl.id(254391707), ],
        'A_videoDataAvailable': [idl.id(35928540), ],
        'A_videoStreamSourceID': [idl.id(152966567), ],
        'A_detectionCenterVideoLocation': [idl.id(83507131), ],
        'A_detectionSizeOnVideo': [idl.id(99643024), ],
        'A_detectionVideoAccuracy': [idl.id(216440692), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Optronics(P_Tactical_Sensor_PSM_C_Detection):
    A_opticalErrorRadius: float = 0.0
    A_absoluteDirectionAvailable: bool = False
    A_sensorLOS: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_sensorLOSAccuracy: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_videoDataAvailable: bool = False
    A_videoStreamSourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_detectionCenterVideoLocation: P_LDM_Common.T_VideoPosition = field(
        default_factory=P_LDM_Common.T_VideoPosition)
    A_detectionSizeOnVideo: P_LDM_Common.T_VideoPosition = field(
        default_factory=P_LDM_Common.T_VideoPosition)
    A_detectionVideoAccuracy: P_LDM_Common.T_VideoPosition = field(
        default_factory=P_LDM_Common.T_VideoPosition)


P_Tactical_Sensor_PSM.C_Detection_Optronics = P_Tactical_Sensor_PSM_C_Detection_Optronics


class P_LDM_Common_T_Identifier:
    def __init__(self, A_platformId: int, A_systemId: int, A_moduleId: int):
        self.A_platformId = A_platformId
        self.A_systemId = A_systemId
        self.A_moduleId = A_moduleId
