# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from DetectionAps.idl
# using RTI Code Generator (rtiddsgen) version 4.3.0.
# The rtiddsgen tool is part of the RTI Connext DDS distribution.
# For more information, type 'rtiddsgen -help' at a command shell
# or consult the Code Generator User's Manual.

from dataclasses import field
from typing import Sequence, Optional
import rti.idl as idl
from enum import IntEnum

from idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet
from idl_types.Detection import P_Tactical_Sensor_PSM as P_Tactical_Sensor_PSM_Object

P_LDM_Common = P_LDM_Common_Objet
P_Tactical_Sensor_PSM = P_Tactical_Sensor_PSM_Object


@idl.alias(
    annotations=[idl.bound(20), ]
)
class P_LDM_Common_T_ShortString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_ShortString = P_LDM_Common_T_ShortString


@idl.enum
class P_Tactical_Sensor_PSM_T_ThreatFamily(IntEnum):
    L_ThreatFamily_UNKNOWN = 0
    L_ThreatFamily_MARNAT = 1
    L_ThreatFamily_TOLAR = 2
    L_ThreatFamily_TANK_BULLET = 3
    L_ThreatFamily_TANNAT = 4
    L_ThreatFamily_OTHER = 5


P_Tactical_Sensor_PSM.T_ThreatFamily = P_Tactical_Sensor_PSM_T_ThreatFamily


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_ThreatData")],
    member_annotations={
        'A_threatID': [idl.id(241586546), ],
        'A_threatType': [idl.id(42452415), ],
        'A_isDetectedByEOS': [idl.id(119038996), ],
        'A_isDetectedBySR': [idl.id(121962734), ],
        'A_isDetectedByPearl': [idl.id(75379114), ],
    }
)
class P_Tactical_Sensor_PSM_T_ThreatData:
    A_threatID: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_threatType: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)
    A_isDetectedByEOS: bool = False
    A_isDetectedBySR: bool = False
    A_isDetectedByPearl: bool = False


P_Tactical_Sensor_PSM.T_ThreatData = P_Tactical_Sensor_PSM_T_ThreatData


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_AronlodThreat")],
    member_annotations={
        'A_orientation': [idl.id(153422287), ],
        'A_distance': [idl.id(178978473), ],
        'A_pencils': [idl.id(135574486), ],
        'A_threatPencils': [idl.id(162902902), idl.bound(32)],
    }
)
class P_Tactical_Sensor_PSM_T_AronlodThreat:
    A_orientation: float = 0.0
    A_distance: float = 0.0
    A_pencils: idl.uint8 = 0
    A_threatPencils: Sequence[P_Tactical_Sensor_PSM.T_ThreatData] = field(default_factory=list)


P_Tactical_Sensor_PSM.T_AronlodThreat = P_Tactical_Sensor_PSM_T_AronlodThreat


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Aps")],
    member_annotations={
        'A_timeToGo': [idl.id(16001726), ],
        'A_affecting': [idl.id(63400329), ],
        'A_threatFamily': [idl.id(71472818), ],
        'A_threatAronlod': [idl.id(38827912), ],
        'A_actionStatus': [idl.id(170861292), ],
        'A_threatHitPoint': [idl.id(27758138), ],
        'A_threatRefinementInfo': [idl.id(140347192), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Aps(P_Tactical_Sensor_PSM.C_Detection):
    A_timeToGo: P_LDM_Common.T_Duration = field(default_factory=P_LDM_Common.T_Duration)
    A_affecting: bool = False
    A_threatFamily: P_Tactical_Sensor_PSM.T_ThreatFamily = P_Tactical_Sensor_PSM.T_ThreatFamily.L_ThreatFamily_UNKNOWN
    A_threatAronlod: Optional[P_Tactical_Sensor_PSM.T_AronlodThreat] = None
    A_actionStatus: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)
    A_threatHitPoint: P_LDM_Common.T_Coordinate3D = field(default_factory=P_LDM_Common.T_Coordinate3D)
    A_threatRefinementInfo: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)


P_Tactical_Sensor_PSM.C_Detection_Aps = P_Tactical_Sensor_PSM_C_Detection_Aps
