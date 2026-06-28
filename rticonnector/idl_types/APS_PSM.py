# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from APS_PSM.idl
# using RTI Code Generator (rtiddsgen) version 4.3.0.
# The rtiddsgen tool is part of the RTI Connext DDS distribution.
# For more information, type 'rtiddsgen -help' at a command shell
# or consult the Code Generator User's Manual.

from dataclasses import field
from typing import Union, Sequence, Optional
import rti.idl as idl
from enum import IntEnum
import sys
import os

from rticonnector.idl_types.LDM_Common import *

P_APS_PSM = idl.get_module("P_APS_PSM")


@idl.enum
class P_APS_PSM_T_OperationalMode(IntEnum):
    L_OperationalMode_STANDBY = 0
    L_OperationalMode_READY = 1
    L_OperationalMode_ARMED = 2
    L_OperationalMode_INITIALIZATION = 3
    L_OperationalMode_FAULT = 4
    L_OperationalMode_DEFENSE = 5
    L_OperationalMode_TRAINING = 6
    L_OperationalMode_DEBRIEFING = 7
    L_OperationalMode_MAINTENANCE = 8
    L_OperationalMode_IBIT = 9
    L_OperationalMode_CALIBRATION = 10


P_APS_PSM.T_OperationalMode = P_APS_PSM_T_OperationalMode


@idl.enum
class P_APS_PSM_T_AreaPropriety(IntEnum):
    L_AreaPropriety_PROPER = 0
    L_AreaPropriety_FAULTY = 1
    L_AreaPropriety_NOT_EXIST = 2


P_APS_PSM.T_AreaPropriety = P_APS_PSM_T_AreaPropriety


@idl.enum
class P_APS_PSM_T_EffectorType(IntEnum):
    L_EffectorType_FAULT = 0
    L_EffectorType_EMPTY = 1
    L_EffectorType_LIVE_AMMUNITION = 2
    L_EffectorType_INERTIAL = 3
    L_EffectorType_NOT_EXIST = 4
    L_EffectorType_PROTECT_COVER = 5
    L_EffectorType_UNKNOWN = 6
    L_EffectorType_MISFIRE = 7


P_APS_PSM.T_EffectorType = P_APS_PSM_T_EffectorType


@idl.enum
class P_APS_PSM_T_ComponentStatus(IntEnum):
    L_ComponentStatus_FAULT = 0
    L_ComponentStatus_OK = 1
    L_ComponentStatus_NOT_EXIST = 2
    L_ComponentStatus_BOEING = 3
    L_ComponentStatus_CLOSE = 4
    L_ComponentStatus_OPEN = 5
    L_ComponentStatus_MIDDLE = 6
    L_ComponentStatus_UNKNOWN = 7
    L_ComponentStatus_MISFIRE = 8


P_APS_PSM.T_ComponentStatus = P_APS_PSM_T_ComponentStatus


@idl.enum
class P_APS_PSM_T_CoverStatus(IntEnum):
    L_CoverStatus_CLOSE = 0
    L_CoverStatus_OPEN = 1
    L_CoverStatus_MIDDLE = 2
    L_CoverStatus_BOEING = 3
    L_CoverStatus_FAULT = 4
    L_CoverStatus_NOT_EXIST = 5


P_APS_PSM.T_CoverStatus = P_APS_PSM_T_CoverStatus


@idl.enum
class P_APS_PSM_T_SafetyStatus(IntEnum):
    L_SafetyStatus_SAFE = 0
    L_SafetyStatus_ARMED = 1


P_APS_PSM.T_SafetyStatus = P_APS_PSM_T_SafetyStatus


@idl.enum
class P_APS_PSM_T_MainSwitchStatus(IntEnum):
    L_MainSwitchStatus_OFF = 0
    L_MainSwitchStatus_READY = 1
    L_MainSwitchStatus_SCAN = 2


P_APS_PSM.T_MainSwitchStatus = P_APS_PSM_T_MainSwitchStatus


@idl.enum
class P_APS_PSM_T_Operation(IntEnum):
    L_Operation_LOAD = 0
    L_Operation_FULL_LOAD = 1
    L_Operation_COVER_CLOSE = 2
    L_Operation_COVER_OPEN = 3
    L_Operation_COVER_SLOW_OPEN = 4
    L_Operation_LAUNCHER_HOME = 5
    L_Operation_LOADER_OPEN = 6
    L_Operation_LOADER_CLOSE = 7
    L_Operation_LOADER_BACK = 8
    L_Operation_COVER_FAST_OPEN = 9
    L_Operation_LOADER_SLOW_MODE = 10


P_APS_PSM.T_Operation = P_APS_PSM_T_Operation


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_Post_Event_Info")],
    member_annotations={
        "A_identification": [
            idl.id(268347597),
        ],
        "A_revelationTime": [
            idl.id(197862764),
        ],
        "A_pathLocation": [
            idl.id(197913135),
        ],
        "A_pathSpeed": [
            idl.id(150738411),
        ],
    },
)
class P_APS_PSM_T_Post_Event_Info:
    A_identification: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_revelationTime: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_pathLocation: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D
    )
    A_pathSpeed: float = 0.0


P_APS_PSM.T_Post_Event_Info = P_APS_PSM_T_Post_Event_Info


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_ThreatPoint")],
    member_annotations={
        "A_detectTime": [
            idl.id(66999595),
        ],
        "A_threatLocation": [
            idl.id(244204931),
        ],
        "A_velocity": [
            idl.id(208188061),
        ],
    },
)
class P_APS_PSM_T_ThreatPoint:
    A_detectTime: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_threatLocation: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D
    )
    A_velocity: P_LDM_Common.T_Vector_3D = field(
        default_factory=P_LDM_Common.T_Vector_3D
    )


P_APS_PSM.T_ThreatPoint = P_APS_PSM_T_ThreatPoint


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_EosStatus")],
    member_annotations={
        "A_frontRight": [
            idl.id(161904839),
        ],
        "A_backRight": [
            idl.id(72147916),
        ],
        "A_backLeft": [
            idl.id(185670500),
        ],
        "A_frontLeft": [
            idl.id(213795472),
        ],
    },
)
class P_APS_PSM_T_EosStatus:
    A_frontRight: P_APS_PSM.T_AreaPropriety = (
        P_APS_PSM.T_AreaPropriety.L_AreaPropriety_PROPER
    )
    A_backRight: P_APS_PSM.T_AreaPropriety = (
        P_APS_PSM.T_AreaPropriety.L_AreaPropriety_PROPER
    )
    A_backLeft: P_APS_PSM.T_AreaPropriety = (
        P_APS_PSM.T_AreaPropriety.L_AreaPropriety_PROPER
    )
    A_frontLeft: P_APS_PSM.T_AreaPropriety = (
        P_APS_PSM.T_AreaPropriety.L_AreaPropriety_PROPER
    )


P_APS_PSM.T_EosStatus = P_APS_PSM_T_EosStatus


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_DefenseParameters")],
    member_annotations={
        "A_parameter1": [
            idl.id(17918493),
        ],
        "A_parameter2": [
            idl.id(152680698),
        ],
        "A_parameter3": [
            idl.id(61940478),
        ],
        "A_parameter4": [
            idl.id(69184909),
        ],
        "A_parameter5": [
            idl.id(238164571),
        ],
    },
)
class P_APS_PSM_T_DefenseParameters:
    A_parameter1: idl.uint8 = 0
    A_parameter2: idl.uint8 = 0
    A_parameter3: idl.uint8 = 0
    A_parameter4: idl.uint8 = 0
    A_parameter5: idl.uint8 = 0


P_APS_PSM.T_DefenseParameters = P_APS_PSM_T_DefenseParameters


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_Launcher")],
    member_annotations={
        "A_status": [
            idl.id(207505413),
        ],
        "A_contents": [idl.id(77194397), idl.bound(2)],
    },
)
class P_APS_PSM_T_Launcher:
    A_status: P_APS_PSM.T_ComponentStatus = (
        P_APS_PSM.T_ComponentStatus.L_ComponentStatus_FAULT
    )
    A_contents: Sequence[P_APS_PSM.T_EffectorType] = field(default_factory=list)


P_APS_PSM.T_Launcher = P_APS_PSM_T_Launcher


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_APS_Specifications")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_numberOfDefenseParameters": [
            idl.id(17060404),
        ],
        "A_defenseParametersDescriptors": [idl.id(175969785), idl.bound(32)],
        "A_numberOfScanAreas": [
            idl.id(40781558),
        ],
        "A_numberOfDefenseAreas": [
            idl.id(108012212),
        ],
        "A_numberOfSoftDefenseAreas": [
            idl.id(108418045),
        ],
    },
)
class P_APS_PSM_C_APS_Specifications:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_numberOfDefenseParameters: idl.uint8 = 0
    A_defenseParametersDescriptors: Sequence[P_LDM_Common.T_ShortString] = field(
        default_factory=list
    )
    A_numberOfScanAreas: idl.uint8 = 0
    A_numberOfDefenseAreas: idl.uint8 = 0
    A_numberOfSoftDefenseAreas: idl.uint8 = 0


P_APS_PSM.C_APS_Specifications = P_APS_PSM_C_APS_Specifications


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Path_Info")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_detectionUniqueID": [
            idl.key,
            idl.id(246744424),
        ],
        "A_points": [idl.id(265231546), idl.bound(32)],
        "A_origin": [
            idl.id(132647116),
        ],
        "A_crossEstimation": [
            idl.id(198115436),
        ],
    },
)
class P_APS_PSM_C_Path_Info:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_detectionUniqueID: P_LDM_Common.T_Uuid = field(
        default_factory=P_LDM_Common.T_Uuid
    )
    A_points: Sequence[P_APS_PSM.T_Post_Event_Info] = field(default_factory=list)
    A_origin: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D
    )
    A_crossEstimation: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D
    )


P_APS_PSM.C_Path_Info = P_APS_PSM_C_Path_Info


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_APS_PSM::C_Defense_Parameters_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_defenseParameters": [
            idl.id(194084544),
        ],
        "A_validity": [
            idl.id(230047821),
        ],
    },
)
class P_APS_PSM_C_Defense_Parameters_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_defenseParameters: idl.int32 = 0
    A_validity: idl.int32 = 0


P_APS_PSM.C_Defense_Parameters_Status = P_APS_PSM_C_Defense_Parameters_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_APS_PSM::C_Defense_Parameters_Values"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_defenseParameters": [
            idl.id(194084544),
        ],
    },
)
class P_APS_PSM_C_Defense_Parameters_Values:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_defenseParameters: P_APS_PSM.T_DefenseParameters = field(
        default_factory=P_APS_PSM.T_DefenseParameters
    )


P_APS_PSM.C_Defense_Parameters_Values = P_APS_PSM_C_Defense_Parameters_Values


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_APS_PSM::C_Readiness_Operational_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_operationalMode": [
            idl.id(47535655),
        ],
        "A_scanAreas": [idl.id(134065511), idl.bound(4)],
        "A_defenseAreas": [idl.id(16057282), idl.bound(4)],
        "A_softDefenseAreas": [idl.id(250900737), idl.bound(4)],
        "A_eosStatus": [idl.id(140728762), idl.bound(4)],
        "A_launchersContent": [idl.id(54801876), idl.bound(4)],
        "A_antenasStatus": [idl.id(71906581), idl.bound(4)],
        "A_launchersStatus": [idl.id(198201773), idl.bound(4)],
        "A_safetyStatus": [
            idl.id(34709806),
        ],
        "A_mainSwitch": [
            idl.id(157490383),
        ],
    },
)
class P_APS_PSM_C_Readiness_Operational_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_operationalMode: P_APS_PSM.T_OperationalMode = (
        P_APS_PSM.T_OperationalMode.L_OperationalMode_STANDBY
    )
    A_scanAreas: Sequence[P_APS_PSM.T_AreaPropriety] = field(default_factory=list)
    A_defenseAreas: Sequence[P_APS_PSM.T_AreaPropriety] = field(default_factory=list)
    A_softDefenseAreas: Sequence[P_APS_PSM.T_AreaPropriety] = field(
        default_factory=list
    )
    A_eosStatus: Sequence[P_APS_PSM.T_ComponentStatus] = field(default_factory=list)
    A_launchersContent: Sequence[P_APS_PSM.T_EffectorType] = field(default_factory=list)
    A_antenasStatus: Sequence[P_APS_PSM.T_ComponentStatus] = field(default_factory=list)
    A_launchersStatus: Sequence[P_APS_PSM.T_ComponentStatus] = field(
        default_factory=list
    )
    A_safetyStatus: P_APS_PSM.T_SafetyStatus = (
        P_APS_PSM.T_SafetyStatus.L_SafetyStatus_SAFE
    )
    A_mainSwitch: P_APS_PSM.T_MainSwitchStatus = (
        P_APS_PSM.T_MainSwitchStatus.L_MainSwitchStatus_OFF
    )


P_APS_PSM.C_Readiness_Operational_Status = P_APS_PSM_C_Readiness_Operational_Status


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Operational_Readiness")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_operationalMode": [
            idl.id(47535655),
        ],
        "A_scanAreas": [idl.id(134065511), idl.bound(4)],
        "A_defenseAreas": [idl.id(16057282), idl.bound(4)],
        "A_softDefenseAreas": [idl.id(250900737), idl.bound(4)],
        "A_eosStatus": [idl.id(140728762), idl.bound(4)],
        "A_launchers": [idl.id(192630285), idl.bound(2)],
        "A_antenasStatus": [idl.id(71906581), idl.bound(4)],
        "A_safetyStatus": [
            idl.id(34709806),
        ],
        "A_mainSwitch": [
            idl.id(157490383),
        ],
    },
)
class P_APS_PSM_C_Operational_Readiness:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_operationalMode: P_APS_PSM.T_OperationalMode = (
        P_APS_PSM.T_OperationalMode.L_OperationalMode_STANDBY
    )
    A_scanAreas: Sequence[P_APS_PSM.T_AreaPropriety] = field(default_factory=list)
    A_defenseAreas: Sequence[P_APS_PSM.T_AreaPropriety] = field(default_factory=list)
    A_softDefenseAreas: Sequence[P_APS_PSM.T_AreaPropriety] = field(
        default_factory=list
    )
    A_eosStatus: Sequence[P_APS_PSM.T_ComponentStatus] = field(default_factory=list)
    A_launchers: Sequence[P_APS_PSM.T_Launcher] = field(default_factory=list)
    A_antenasStatus: Sequence[P_APS_PSM.T_ComponentStatus] = field(default_factory=list)
    A_safetyStatus: P_APS_PSM.T_SafetyStatus = (
        P_APS_PSM.T_SafetyStatus.L_SafetyStatus_SAFE
    )
    A_mainSwitch: P_APS_PSM.T_MainSwitchStatus = (
        P_APS_PSM.T_MainSwitchStatus.L_MainSwitchStatus_OFF
    )


P_APS_PSM.C_Operational_Readiness = P_APS_PSM_C_Operational_Readiness


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Default_Defense_Cmd")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
    },
)
class P_APS_PSM_C_Default_Defense_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False


P_APS_PSM.C_Default_Defense_Cmd = P_APS_PSM_C_Default_Defense_Cmd


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Set_Platform_Type_Cmd")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
        "A_platform": [
            idl.id(29421584),
        ],
        "A_platformSubType": [
            idl.id(9101197),
        ],
    },
)
class P_APS_PSM_C_Set_Platform_Type_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False
    A_platform: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_platformSubType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )


P_APS_PSM.C_Set_Platform_Type_Cmd = P_APS_PSM_C_Set_Platform_Type_Cmd


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Set_Operation_Cmd")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
        "A_operation": [
            idl.id(127010964),
        ],
    },
)
class P_APS_PSM_C_Set_Operation_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False
    A_operation: P_APS_PSM.T_Operation = P_APS_PSM.T_Operation.L_Operation_LOAD


P_APS_PSM.C_Set_Operation_Cmd = P_APS_PSM_C_Set_Operation_Cmd


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Set_Readiness_Cmd")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
        "A_readinessMode": [
            idl.id(256066282),
        ],
    },
)
class P_APS_PSM_C_Set_Readiness_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False
    A_readinessMode: P_APS_PSM.T_OperationalMode = (
        P_APS_PSM.T_OperationalMode.L_OperationalMode_STANDBY
    )


P_APS_PSM.C_Set_Readiness_Cmd = P_APS_PSM_C_Set_Readiness_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_APS_PSM::C_Set_DefenseParameters_Values_Cmd"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
        "A_defenseParameters": [
            idl.id(194084544),
        ],
    },
)
class P_APS_PSM_C_Set_DefenseParameters_Values_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False
    A_defenseParameters: P_APS_PSM.T_DefenseParameters = field(
        default_factory=P_APS_PSM.T_DefenseParameters
    )


P_APS_PSM.C_Set_DefenseParameters_Values_Cmd = (
    P_APS_PSM_C_Set_DefenseParameters_Values_Cmd
)


@idl.enum
class P_APS_PSM_T_RelativeAxis(IntEnum):
    L_RelativeAxis_NO_CHANGE = 0
    L_RelativeAxis_TURRET = 1
    L_RelativeAxis_HULL = 2
    L_RelativeAxis_NORTH = 3
    L_RelativeAxis_CMS = 4


P_APS_PSM.T_RelativeAxis = P_APS_PSM_T_RelativeAxis


@idl.enum
class P_APS_PSM_T_AreasMode(IntEnum):
    L_AreasMode_HOME = 0
    L_AreasMode_FIELD = 1
    L_AreasMode_UNKNOWN = 2


P_APS_PSM.T_AreasMode = P_APS_PSM_T_AreasMode


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_ThreatData")],
    member_annotations={
        "A_threatID": [
            idl.id(241586546),
        ],
        "A_threatType": [
            idl.id(42452415),
        ],
        "A_isDetectedByEOS": [
            idl.id(119038996),
        ],
        "A_isDetectedBySR": [
            idl.id(121962734),
        ],
        "A_isDetectedByPearl": [
            idl.id(75379114),
        ],
    },
)
class P_APS_PSM_T_ThreatData:
    A_threatID: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_threatType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_isDetectedByEOS: bool = False
    A_isDetectedBySR: bool = False
    A_isDetectedByPearl: bool = False


P_APS_PSM.T_ThreatData = P_APS_PSM_T_ThreatData


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_JumboStatus")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_JumboID": [
            idl.id(17979367),
        ],
        "A_JumboAz": [
            idl.id(148856826),
        ],
        "A_JumboAzSTD": [
            idl.id(259407505),
        ],
        "A_JumboEl": [
            idl.id(159425565),
        ],
        "A_param": [
            idl.id(86364000),
        ],
    },
)
class P_APS_PSM_C_JumboStatus:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_JumboID: idl.int32 = 0
    A_JumboAz: float = 0.0
    A_JumboAzSTD: float = 0.0
    A_JumboEl: float = 0.0
    A_param: idl.int32 = 0


P_APS_PSM.C_JumboStatus = P_APS_PSM_C_JumboStatus


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_NumFslThreats")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_threatID": [
            idl.id(241586546),
        ],
        "A_pencil": [
            idl.id(260771610),
        ],
    },
)
class P_APS_PSM_C_NumFslThreats:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_threatID: idl.int32 = 0
    A_pencil: idl.uint8 = 0


P_APS_PSM.C_NumFslThreats = P_APS_PSM_C_NumFslThreats


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Aps_Status_Extended")],
    member_annotations={
        "A_loadersContent": [idl.id(122719368), idl.bound(2)],
        "A_loadersStatus": [idl.id(114972955), idl.bound(2)],
        "A_covers": [idl.id(10068475), idl.bound(2)],
        "A_relativeAxis": [
            idl.id(195026304),
        ],
        "A_buildArea": [
            idl.id(67048405),
        ],
    },
)
class P_APS_PSM_C_Aps_Status_Extended(P_APS_PSM.C_Readiness_Operational_Status):
    A_loadersContent: Sequence[P_APS_PSM.T_EffectorType] = field(default_factory=list)
    A_loadersStatus: Sequence[P_APS_PSM.T_ComponentStatus] = field(default_factory=list)
    A_covers: Sequence[P_APS_PSM.T_ComponentStatus] = field(default_factory=list)
    A_relativeAxis: P_APS_PSM.T_RelativeAxis = (
        P_APS_PSM.T_RelativeAxis.L_RelativeAxis_NO_CHANGE
    )
    A_buildArea: P_APS_PSM.T_AreasMode = P_APS_PSM.T_AreasMode.L_AreasMode_HOME


P_APS_PSM.C_Aps_Status_Extended = P_APS_PSM_C_Aps_Status_Extended


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Set_InstallAngles_Cmd")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
        "A_numOfPoints": [
            idl.id(30334857),
        ],
        "A_points": [idl.id(265231546), idl.bound(32)],
    },
)
class P_APS_PSM_C_Set_InstallAngles_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False
    A_numOfPoints: idl.uint8 = 0
    A_points: Sequence[P_LDM_Common.T_Attitude] = field(default_factory=list)


P_APS_PSM.C_Set_InstallAngles_Cmd = P_APS_PSM_C_Set_InstallAngles_Cmd


@idl.enum
class P_APS_PSM_T_MainOp(IntEnum):
    L_MainOp_IBIT = 0
    L_MainOp_IBIT_REPORT_REQ = 1
    L_MainOp_SYS_CALIB = 2
    L_MainOp_FULL_LOAD_R = 3
    L_MainOp_FULL_LOAD_L = 4
    L_MainOp_SR_INSTALL_CALIB = 5
    L_MainOp_COVER_SLOW_OPEN_R = 6
    L_MainOp_COVER_SLOW_OPEN_L = 7
    L_MainOp_COVER_CLOSE_R = 8
    L_MainOp_COVER_CLOSE_L = 9
    L_MainOp_LAUNCHER_R_HOME = 10
    L_MainOp_LAUNCHER_R_SERVICE = 11
    L_MainOp_LAUNCHER_L_HOME = 12
    L_MainOp_LAUNCHER_L_SERVICE = 13
    L_MainOp_CALIB_DATA_REQ = 14
    L_MainOp_COVER_DATA_REQ = 15
    L_MainOp_GET_WINDCOAT_OPERATIONS_DATES = 16
    L_MainOp_GET_SYSTEM_VERSION = 17
    L_MainOp_SYS_CALIB_PHASE = 18
    L_MainOp_LOADER_OPEN_R = 19
    L_MainOp_LOADER_OPEN_L = 20
    L_MainOp_LOADER_CLOSE_R = 21
    L_MainOp_LOADER_CLOSE_L = 22
    L_MainOp_IBIT_BL_LOADER_L = 23
    L_MainOp_IBIT_BL_LOADER_R = 24
    L_MainOp_LOADER_R_BACK = 25
    L_MainOp_LOADER_L_BACK = 26
    L_MainOp_COVER_FAST_OPEN_R = 27
    L_MainOp_COVER_FAST_OPEN_L = 28
    L_MainOp_LOADER_R_SLOW_MODE = 29
    L_MainOp_LOADER_L_SLOW_MODE = 30


P_APS_PSM.T_MainOp = P_APS_PSM_T_MainOp


@idl.enum
class P_APS_PSM_T_MaintActionStatus(IntEnum):
    L_MaintActionStatus_SUCCESS = 0
    L_MaintActionStatus_FAIL = 1
    L_MaintActionStatus_WAITING = 2
    L_MaintActionStatus_IN_PROGRESS = 3


P_APS_PSM.T_MaintActionStatus = P_APS_PSM_T_MaintActionStatus


@idl.enum
class P_APS_PSM_T_Action(IntEnum):
    L_Action_START = 0
    L_Action_ABORT = 1
    L_Action_RETRY = 2
    L_Action_CONTINUE = 3


P_APS_PSM.T_Action = P_APS_PSM_T_Action


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_CalibEos")],
    member_annotations={
        "A_int_fr": [
            idl.id(131913229),
        ],
        "A_int_br": [
            idl.id(9443332),
        ],
        "A_int_bl": [
            idl.id(166679096),
        ],
        "A_int_fl": [
            idl.id(119785758),
        ],
        "A_ext_fr": [
            idl.id(114227980),
        ],
        "A_ext_br": [
            idl.id(32826569),
        ],
        "A_ext_bl": [
            idl.id(216696934),
        ],
        "A_ext_fl": [
            idl.id(33037673),
        ],
    },
)
class P_APS_PSM_T_CalibEos:
    A_int_fr: bool = False
    A_int_br: bool = False
    A_int_bl: bool = False
    A_int_fl: bool = False
    A_ext_fr: bool = False
    A_ext_br: bool = False
    A_ext_bl: bool = False
    A_ext_fl: bool = False


P_APS_PSM.T_CalibEos = P_APS_PSM_T_CalibEos


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::T_CalibSystems")],
    member_annotations={
        "A_sr_fr": [
            idl.id(67624852),
        ],
        "A_sr_fl": [
            idl.id(25864134),
        ],
        "A_sr_br": [
            idl.id(216229760),
        ],
        "A_sr_bl": [
            idl.id(244135086),
        ],
        "A_launcher_r": [
            idl.id(22396810),
        ],
        "A_launcher_l": [
            idl.id(57563729),
        ],
    },
)
class P_APS_PSM_T_CalibSystems:
    A_sr_fr: bool = False
    A_sr_fl: bool = False
    A_sr_br: bool = False
    A_sr_bl: bool = False
    A_launcher_r: bool = False
    A_launcher_l: bool = False


P_APS_PSM.T_CalibSystems = P_APS_PSM_T_CalibSystems


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_APS_Status")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_operation": [
            idl.id(127010964),
        ],
        "A_status": [
            idl.id(207505413),
        ],
        "A_reason": [
            idl.id(244844774),
        ],
    },
)
class P_APS_PSM_C_APS_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_operation: P_APS_PSM.T_MainOp = P_APS_PSM.T_MainOp.L_MainOp_IBIT
    A_status: P_APS_PSM.T_MaintActionStatus = (
        P_APS_PSM.T_MaintActionStatus.L_MaintActionStatus_SUCCESS
    )
    A_reason: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )


P_APS_PSM.C_APS_Status = P_APS_PSM_C_APS_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_APS_PSM::C_Calibration_APS_Status"),
    ],
    member_annotations={
        "A_calibEos": [
            idl.id(65140487),
        ],
        "A_calibSystems": [
            idl.id(260072533),
        ],
    },
)
class P_APS_PSM_C_Calibration_APS_Status(P_APS_PSM.C_APS_Status):
    A_calibEos: P_APS_PSM.T_CalibEos = field(default_factory=P_APS_PSM.T_CalibEos)
    A_calibSystems: P_APS_PSM.T_CalibSystems = field(
        default_factory=P_APS_PSM.T_CalibSystems
    )


P_APS_PSM.C_Calibration_APS_Status = P_APS_PSM_C_Calibration_APS_Status


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_APS_PSM::C_Set_APS_Operation_Cmd")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_recipientID": [
            idl.key,
            idl.id(214190224),
        ],
        "A_referenceNum": [
            idl.id(249600164),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_responseNotRequired": [
            idl.id(193715237),
        ],
        "A_operation": [
            idl.id(127010964),
        ],
        "A_maintenanceAction": [
            idl.id(127397250),
        ],
        "A_maskedUnits": [idl.id(174038674), idl.bound(64)],
    },
)
class P_APS_PSM_C_Set_APS_Operation_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_recipientID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_responseNotRequired: bool = False
    A_operation: P_APS_PSM.T_MainOp = P_APS_PSM.T_MainOp.L_MainOp_IBIT
    A_maintenanceAction: P_APS_PSM.T_Action = P_APS_PSM.T_Action.L_Action_START
    A_maskedUnits: Sequence[P_LDM_Common.T_ShortString] = field(default_factory=list)


P_APS_PSM.C_Set_APS_Operation_Cmd = P_APS_PSM_C_Set_APS_Operation_Cmd
