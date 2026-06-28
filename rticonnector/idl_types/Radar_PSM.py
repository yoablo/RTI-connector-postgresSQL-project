# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Radar_PSM.idl
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

P_Radar_PSM = idl.get_module("P_Radar_PSM")


@idl.enum
class P_Radar_PSM_T_Mode(IntEnum):
    L_Mode_SCAN = 0
    L_Mode_LOCK = 1


P_Radar_PSM.T_Mode = P_Radar_PSM_T_Mode


@idl.enum
class P_Radar_PSM_T_Mission(IntEnum):
    L_Mission_GS = 0
    L_Mission_AS = 1
    L_Mission_GSAS = 2


P_Radar_PSM.T_Mission = P_Radar_PSM_T_Mission


@idl.enum
class P_Radar_PSM_T_MissionPurpose(IntEnum):
    L_MissionPurpose_MISSION_1 = 0
    L_MissionPurpose_MISSION_2 = 1
    L_MissionPurpose_MISSION_3 = 2
    L_MissionPurpose_MISSION_4 = 3
    L_MissionPurpose_MISSION_5 = 4
    L_MissionPurpose_MISSION_6 = 5


P_Radar_PSM.T_MissionPurpose = P_Radar_PSM_T_MissionPurpose


@idl.enum
class P_Radar_PSM_T_State(IntEnum):
    L_State_OFF = 0
    L_State_INIT = 1
    L_State_STANDBY = 2
    L_State_OPERATE = 3
    L_State_MAINTENANCE = 4


P_Radar_PSM.T_State = P_Radar_PSM_T_State


@idl.enum
class P_Radar_PSM_T_Request(IntEnum):
    L_Request_STT = 0
    L_Request_EMR = 1


P_Radar_PSM.T_Request = P_Radar_PSM_T_Request


@idl.enum
class P_Radar_PSM_T_Priority(IntEnum):
    L_Priority_EOS = 0
    L_Priority_EOA = 1
    L_Priority_IMD = 2
    L_Priority_EMR = 3


P_Radar_PSM.T_Priority = P_Radar_PSM_T_Priority


@idl.enum
class P_Radar_PSM_T_InstallStatus(IntEnum):
    L_InstallStatus_NONE = 0
    L_InstallStatus_IN_PROGRESS = 1
    L_InstallStatus_FAILED = 2
    L_InstallStatus_SUCCEEDED = 3


P_Radar_PSM.T_InstallStatus = P_Radar_PSM_T_InstallStatus


@idl.enum
class P_Radar_PSM_T_AntenaLocation(IntEnum):
    L_AntenaLocation_FORWARD_RIGHT = 0
    L_AntenaLocation_BACK_RIGHT = 1
    L_AntenaLocation_BACK_LEFT = 2
    L_AntenaLocation_FORWARD_LEFT = 3


P_Radar_PSM.T_AntenaLocation = P_Radar_PSM_T_AntenaLocation


@idl.enum
class P_Radar_PSM_T_AntenaType(IntEnum):
    L_AntenaType_M_TYPE = 0
    L_AntenaType_E_TYPE = 1


P_Radar_PSM.T_AntenaType = P_Radar_PSM_T_AntenaType


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Radar_PSM::T_SearchRadarStatus")],
    member_annotations={
        "A_transmitRF": [
            idl.id(36088711),
        ],
        "A_ant1status": [
            idl.id(158624287),
        ],
        "A_ant2status": [
            idl.id(4316863),
        ],
        "A_ant3status": [
            idl.id(100586280),
        ],
        "A_ant4status": [
            idl.id(176791672),
        ],
    },
)
class P_Radar_PSM_T_SearchRadarStatus:
    A_transmitRF: bool = False
    A_ant1status: bool = False
    A_ant2status: bool = False
    A_ant3status: bool = False
    A_ant4status: bool = False


P_Radar_PSM.T_SearchRadarStatus = P_Radar_PSM_T_SearchRadarStatus


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Radar_PSM::C_Radar_System_Specification"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_rangeSupport": [
            idl.id(8397463),
        ],
        "A_targetSizeSupport": [
            idl.id(32294457),
        ],
        "A_accuracySupport": [
            idl.id(114850561),
        ],
        "A_setDetectorStateSupport": [
            idl.id(5997863),
        ],
        "A_snapshotSupport": [
            idl.id(126899836),
        ],
        "A_linearInstallationOffset": [
            idl.id(82849345),
        ],
        "A_rotationalInstallationOffset": [
            idl.id(69427824),
        ],
        "A_rcsReductionSupport": [
            idl.id(193017008),
        ],
    },
)
class P_Radar_PSM_C_Radar_System_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_rangeSupport: bool = False
    A_targetSizeSupport: bool = False
    A_accuracySupport: bool = False
    A_setDetectorStateSupport: bool = False
    A_snapshotSupport: bool = False
    A_linearInstallationOffset: P_LDM_Common.T_LinearOffset = field(
        default_factory=P_LDM_Common.T_LinearOffset
    )
    A_rotationalInstallationOffset: P_LDM_Common.T_RotationalOffset = field(
        default_factory=P_LDM_Common.T_RotationalOffset
    )
    A_rcsReductionSupport: bool = False


P_Radar_PSM.C_Radar_System_Specification = P_Radar_PSM_C_Radar_System_Specification


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Radar_PSM::C_Radar_Status")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_rdrID": [
            idl.id(127573083),
        ],
    },
)
class P_Radar_PSM_C_Radar_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_rdrID: idl.int32 = 0


P_Radar_PSM.C_Radar_Status = P_Radar_PSM_C_Radar_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Radar_PSM::C_Unified_Radar_Status"),
    ],
    member_annotations={
        "A_state": [
            idl.id(90057368),
        ],
        "A_missionCategory": [
            idl.id(179661941),
        ],
        "A_tx": [
            idl.id(230735362),
        ],
        "A_freqIndex": [
            idl.id(204327783),
        ],
        "A_searchStatus": [
            idl.id(178074502),
        ],
    },
)
class P_Radar_PSM_C_Unified_Radar_Status(P_Radar_PSM.C_Radar_Status):
    A_state: P_Radar_PSM.T_State = P_Radar_PSM.T_State.L_State_OFF
    A_missionCategory: P_Radar_PSM.T_MissionPurpose = (
        P_Radar_PSM.T_MissionPurpose.L_MissionPurpose_MISSION_1
    )
    A_tx: bool = False
    A_freqIndex: idl.int32 = 0
    A_searchStatus: P_Radar_PSM.T_SearchRadarStatus = field(
        default_factory=P_Radar_PSM.T_SearchRadarStatus
    )


P_Radar_PSM.C_Unified_Radar_Status = P_Radar_PSM_C_Unified_Radar_Status


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Radar_PSM::C_Maintenance_Status")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_installStatus": [
            idl.id(246399055),
        ],
        "A_bitInProcess": [
            idl.id(96571324),
        ],
    },
)
class P_Radar_PSM_C_Maintenance_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_installStatus: P_Radar_PSM.T_InstallStatus = (
        P_Radar_PSM.T_InstallStatus.L_InstallStatus_NONE
    )
    A_bitInProcess: bool = False


P_Radar_PSM.C_Maintenance_Status = P_Radar_PSM_C_Maintenance_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Radar_PSM::C_Radar_System_Target_Cmd"),
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
        "A_request": [
            idl.id(4951193),
        ],
        "A_mtg": [
            idl.id(258043443),
        ],
        "A_sPriority": [
            idl.id(16652445),
        ],
        "A_direction": [
            idl.id(4705490),
        ],
        "A_doppler": [
            idl.id(227270197),
        ],
    },
)
class P_Radar_PSM_C_Radar_System_Target_Cmd:
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
    A_request: P_Radar_PSM.T_Request = P_Radar_PSM.T_Request.L_Request_STT
    A_mtg: idl.int32 = 0
    A_sPriority: P_Radar_PSM.T_Priority = P_Radar_PSM.T_Priority.L_Priority_EOS
    A_direction: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D
    )
    A_doppler: float = 0.0


P_Radar_PSM.C_Radar_System_Target_Cmd = P_Radar_PSM_C_Radar_System_Target_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Radar_PSM::C_Radar_System_MissionDef_Cmd"),
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
        "A_rdrId": [
            idl.id(122259186),
        ],
        "A_state": [
            idl.id(90057368),
        ],
        "A_missionCategory": [
            idl.id(179661941),
        ],
        "A_tx": [
            idl.id(230735362),
        ],
        "A_freqIndex": [
            idl.id(204327783),
        ],
    },
)
class P_Radar_PSM_C_Radar_System_MissionDef_Cmd:
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
    A_rdrId: idl.int32 = 0
    A_state: P_Radar_PSM.T_State = P_Radar_PSM.T_State.L_State_OFF
    A_missionCategory: P_Radar_PSM.T_MissionPurpose = (
        P_Radar_PSM.T_MissionPurpose.L_MissionPurpose_MISSION_1
    )
    A_tx: bool = False
    A_freqIndex: idl.int32 = 0


P_Radar_PSM.C_Radar_System_MissionDef_Cmd = P_Radar_PSM_C_Radar_System_MissionDef_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Radar_PSM::C_Radar_Platform_Mdp_Cmd"),
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
        "A_antenaId": [
            idl.id(135420166),
        ],
        "A_antenaType": [
            idl.id(62992772),
        ],
        "A_stages": [idl.id(68178022), idl.bound(5)],
    },
)
class P_Radar_PSM_C_Radar_Platform_Mdp_Cmd:
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
    A_antenaId: P_Radar_PSM.T_AntenaLocation = (
        P_Radar_PSM.T_AntenaLocation.L_AntenaLocation_FORWARD_RIGHT
    )
    A_antenaType: P_Radar_PSM.T_AntenaType = (
        P_Radar_PSM.T_AntenaType.L_AntenaType_M_TYPE
    )
    A_stages: Sequence[idl.uint8] = field(default_factory=idl.array_factory(idl.uint8))


P_Radar_PSM.C_Radar_Platform_Mdp_Cmd = P_Radar_PSM_C_Radar_Platform_Mdp_Cmd
