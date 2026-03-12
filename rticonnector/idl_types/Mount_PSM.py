
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Mount_PSM.idl
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

P_Mount_PSM = idl.get_module("P_Mount_PSM")

P_Mount_PSM_T_ManualAzimuthVelocity = idl.int16

P_Mount_PSM.T_ManualAzimuthVelocity = P_Mount_PSM_T_ManualAzimuthVelocity

P_Mount_PSM_T_ManualElevationVelocity = idl.int16

P_Mount_PSM.T_ManualElevationVelocity = P_Mount_PSM_T_ManualElevationVelocity

@idl.alias(
    annotations = [idl.bound(30),]
)
class P_Mount_PSM_T_PresetAnglesArray:
    value: Sequence[P_LDM_Common.T_RotationalPosition] = field(default_factory = list)

P_Mount_PSM.T_PresetAnglesArray = P_Mount_PSM_T_PresetAnglesArray

@idl.enum
class P_Mount_PSM_T_ProcessState(IntEnum):
    L_ProcessState_OFF = 0
    L_ProcessState_IN_PROGRESS = 1
    L_ProcessState_COMPLETED = 2
    L_ProcessState_FAILED = 3

P_Mount_PSM.T_ProcessState = P_Mount_PSM_T_ProcessState

@idl.enum
class P_Mount_PSM_T_MountWorkMode(IntEnum):
    L_MountWorkMode_INIT = 0
    L_MountWorkMode_OPER = 1
    L_MountWorkMode_MAINT = 2

P_Mount_PSM.T_MountWorkMode = P_Mount_PSM_T_MountWorkMode

@idl.enum
class P_Mount_PSM_T_EnslavementMode(IntEnum):
    L_EnslavementMode_INDEPENDENT = 0
    L_EnslavementMode_ENSLAVED = 1
    L_EnslavementMode_MECHANICAL = 2

P_Mount_PSM.T_EnslavementMode = P_Mount_PSM_T_EnslavementMode

@idl.enum
class P_Mount_PSM_T_StabilizationMode(IntEnum):
    L_StabilizationMode_MANUAL = 0
    L_StabilizationMode_POWER = 1
    L_StabilizationMode_STABILIZATION = 2

P_Mount_PSM.T_StabilizationMode = P_Mount_PSM_T_StabilizationMode

@idl.enum
class P_Mount_PSM_T_IndexProcessMode(IntEnum):
    L_IndexProcessMode_NOT_ACTIVE = 0
    L_IndexProcessMode_IN_PROCESS = 1
    L_IndexProcessMode_ERROR = 2

P_Mount_PSM.T_IndexProcessMode = P_Mount_PSM_T_IndexProcessMode

@idl.enum
class P_Mount_PSM_T_MaintenanceMode(IntEnum):
    L_MaintenanceMode_CALIBRATION = 0
    L_MaintenanceMode_BURNING = 1
    L_MaintenanceMode_OTHER = 2

P_Mount_PSM.T_MaintenanceMode = P_Mount_PSM_T_MaintenanceMode

@idl.enum
class P_Mount_PSM_T_CalibrationMode(IntEnum):
    L_CalibrationMode_NONE = 0
    L_CalibrationMode_BS = 1
    L_CalibrationMode_LIMITS = 2
    L_CalibrationMode_DRIFT_COMP = 3
    L_CalibrationMode_OTHER = 4

P_Mount_PSM.T_CalibrationMode = P_Mount_PSM_T_CalibrationMode

@idl.enum
class P_Mount_PSM_T_MountSystem_Mode(IntEnum):
    L_MountSystem_Mode_INIT = 0
    L_MountSystem_Mode_GYRO_STAB = 1
    L_MountSystem_Mode_POINT_STAB = 2
    L_MountSystem_Mode_SLAVE = 3
    L_MountSystem_Mode_POSITION = 4
    L_MountSystem_Mode_DRIFT_COMP = 5
    L_MountSystem_Mode_BRING_TO = 6
    L_MountSystem_Mode_TRACK = 7
    L_MountSystem_Mode_STANDBY = 8
    L_MountSystem_Mode_IBIT = 9
    L_MountSystem_Mode_TV_BORESIGHT = 10
    L_MountSystem_Mode_EXCEPTION = 11

P_Mount_PSM.T_MountSystem_Mode = P_Mount_PSM_T_MountSystem_Mode

@idl.enum
class P_Mount_PSM_T_PredefinedPosition(IntEnum):
    L_PredefinedPosition_LOAD = 0
    L_PredefinedPosition_HOME = 1
    L_PredefinedPosition_LOCK = 2

P_Mount_PSM.T_PredefinedPosition = P_Mount_PSM_T_PredefinedPosition

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Mount_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_moveToPosSupport': [idl.id(6885879), ],
        'A_moveToRelativePosSupport': [idl.id(154179029), ],
        'A_manualMoveSupport': [idl.id(134128559), ],
        'A_scanSupport': [idl.id(117148995), ],
        'A_lmcSupport': [idl.id(78246304), ],
        'A_indexProcessSupport': [idl.id(153789327), ],
        'A_presetBringToPosSupport': [idl.id(19561599), ],
        'A_enslavingMountsSupport': [idl.id(10854447), idl.bound(10)],
        'A_stabilizationModeSupport': [idl.id(104304729), idl.bound(3)],
        'A_movementInhibitZoneSupport': [idl.id(105149319), ],
        'A_preDefinedPositionsSupport': [idl.id(31755193), idl.bound(10)],
    }
)
class P_Mount_PSM_C_Mount_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_moveToPosSupport: bool = False
    A_moveToRelativePosSupport: bool = False
    A_manualMoveSupport: bool = False
    A_scanSupport: bool = False
    A_lmcSupport: bool = False
    A_indexProcessSupport: bool = False
    A_presetBringToPosSupport: P_Mount_PSM.T_PresetAnglesArray = field(default_factory = P_Mount_PSM.T_PresetAnglesArray)
    A_enslavingMountsSupport: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_stabilizationModeSupport: Sequence[P_Mount_PSM.T_StabilizationMode] = field(default_factory = list)
    A_movementInhibitZoneSupport: bool = False
    A_preDefinedPositionsSupport: Sequence[P_Mount_PSM.T_PredefinedPosition] = field(default_factory = list)

P_Mount_PSM.C_Mount_Specification = P_Mount_PSM_C_Mount_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_mountPosition': [idl.id(87554151), ],
        'A_absolutePosition': [idl.id(16428286), ],
        'A_attitudeToNorthPosition': [idl.id(77955496), ],
        'A_scanState': [idl.id(231740354), ],
        'A_bringToState': [idl.id(82168132), ],
        'A_bringToPreset': [idl.id(164285904), ],
        'A_enslavementMode': [idl.id(125824979), ],
        'A_enslavedTo': [idl.id(56539008), ],
        'A_workMode': [idl.id(177658374), ],
        'A_lmcState': [idl.id(93868992), ],
        'A_stabilizationState': [idl.id(7339653), ],
        'A_inMovementInhibitZone': [idl.id(259448016), ],
        'A_traverseMode': [idl.id(69652467), ],
        'A_isMovmentEnabled': [idl.id(255144296), ],
        'A_minElevation': [idl.id(206267848), ],
        'A_maxElevation': [idl.id(258971329), ],
    }
)
class P_Mount_PSM_C_Rot_Mount:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_mountPosition: P_LDM_Common.T_RotationalPosition = field(default_factory = P_LDM_Common.T_RotationalPosition)
    A_absolutePosition: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_attitudeToNorthPosition: float = 0.0
    A_scanState: P_Mount_PSM.T_ProcessState = P_Mount_PSM.T_ProcessState.L_ProcessState_OFF
    A_bringToState: P_Mount_PSM.T_ProcessState = P_Mount_PSM.T_ProcessState.L_ProcessState_OFF
    A_bringToPreset: P_LDM_Common.T_RotationalPosition = field(default_factory = P_LDM_Common.T_RotationalPosition)
    A_enslavementMode: P_Mount_PSM.T_EnslavementMode = P_Mount_PSM.T_EnslavementMode.L_EnslavementMode_INDEPENDENT
    A_enslavedTo: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_workMode: P_Mount_PSM.T_MountWorkMode = P_Mount_PSM.T_MountWorkMode.L_MountWorkMode_INIT
    A_lmcState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_stabilizationState: P_Mount_PSM.T_StabilizationMode = P_Mount_PSM.T_StabilizationMode.L_StabilizationMode_MANUAL
    A_inMovementInhibitZone: bool = False
    A_traverseMode: bool = False
    A_isMovmentEnabled: bool = False
    A_minElevation: Optional[float] = None
    A_maxElevation: Optional[float] = None

P_Mount_PSM.C_Rot_Mount = P_Mount_PSM_C_Rot_Mount

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_Index")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_indexState': [idl.id(253710099), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_Index:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_indexState: P_Mount_PSM.T_IndexProcessMode = P_Mount_PSM.T_IndexProcessMode.L_IndexProcessMode_NOT_ACTIVE

P_Mount_PSM.C_Rot_Mount_Index = P_Mount_PSM_C_Rot_Mount_Index

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_Calibration_Status")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_calibrationState': [idl.id(234811921), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_Calibration_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_calibrationState: P_Mount_PSM.T_CalibrationMode = P_Mount_PSM.T_CalibrationMode.L_CalibrationMode_NONE

P_Mount_PSM.C_Rot_Mount_Calibration_Status = P_Mount_PSM_C_Rot_Mount_Calibration_Status

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Mount_Command_Response")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_metadata': [idl.id(88603227), ],
        'A_responseState': [idl.id(203692061), ],
        'A_additionalCode': [idl.id(51197241), ],
    }
)
class P_Mount_PSM_C_Mount_Command_Response:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_metadata: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_responseState: P_LDM_Common.T_Command_Response = P_LDM_Common.T_Command_Response.L_Command_Response_INVALID
    A_additionalCode: idl.int32 = 0

P_Mount_PSM.C_Mount_Command_Response = P_Mount_PSM_C_Mount_Command_Response

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Boresight_Calibration_Response")],
    member_annotations = {
        'A_enslavementMode': [idl.id(125824979), ],
    }
)
class P_Mount_PSM_C_Boresight_Calibration_Response(P_Mount_PSM.C_Mount_Command_Response):
    A_enslavementMode: P_LDM_Common.T_SightEnslavement_Mode = P_LDM_Common.T_SightEnslavement_Mode.L_SightEnslavement_Mode_IDLE

P_Mount_PSM.C_Boresight_Calibration_Response = P_Mount_PSM_C_Boresight_Calibration_Response

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_GS_ModeStatus")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_mode': [idl.id(236875199), ],
    }
)
class P_Mount_PSM_C_GS_ModeStatus:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_mode: P_Mount_PSM.T_MountSystem_Mode = P_Mount_PSM.T_MountSystem_Mode.L_MountSystem_Mode_INIT

P_Mount_PSM.C_GS_ModeStatus = P_Mount_PSM_C_GS_ModeStatus

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Mount_Limits_Status")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_sectorType': [idl.id(49506505), ],
        'A_sectorLimits': [idl.id(143924180), idl.bound(2)],
        'A_sectorAzRef': [idl.id(237128275), ],
    }
)
class P_Mount_PSM_C_Mount_Limits_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_sectorType: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_sectorLimits: Sequence[P_LDM_Common.T_RotationalPosition] = field(default_factory = list)
    A_sectorAzRef: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Mount_PSM.C_Mount_Limits_Status = P_Mount_PSM_C_Mount_Limits_Status

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_BringToRelative_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_relativePosition': [idl.id(90603335), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_BringToRelative_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_relativePosition: P_LDM_Common.T_RotationalPosition = field(default_factory = P_LDM_Common.T_RotationalPosition)

P_Mount_PSM.C_Rot_Mount_BringToRelative_Cmd = P_Mount_PSM_C_Rot_Mount_BringToRelative_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_BringTo_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_absolutePosition': [idl.id(16428286), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_BringTo_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_absolutePosition: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Mount_PSM.C_Rot_Mount_BringTo_Cmd = P_Mount_PSM_C_Rot_Mount_BringTo_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_BringToPreset_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_preset': [idl.id(103990046), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_BringToPreset_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_preset: P_LDM_Common.T_RotationalPosition = field(default_factory = P_LDM_Common.T_RotationalPosition)

P_Mount_PSM.C_Rot_Mount_BringToPreset_Cmd = P_Mount_PSM_C_Rot_Mount_BringToPreset_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_BringToCyclic_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_azimuthVelocity': [idl.id(143408719), ],
        'A_elevationVelocity': [idl.id(48285584), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_BringToCyclic_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_azimuthVelocity: idl.int16 = 0
    A_elevationVelocity: idl.int16 = 0

P_Mount_PSM.C_Rot_Mount_BringToCyclic_Cmd = P_Mount_PSM_C_Rot_Mount_BringToCyclic_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_EnslaveTo_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_requestedEnslaveMode': [idl.id(206145311), ],
        'A_enslaverMountID': [idl.id(177753629), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_EnslaveTo_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_requestedEnslaveMode: P_Mount_PSM.T_EnslavementMode = P_Mount_PSM.T_EnslavementMode.L_EnslavementMode_INDEPENDENT
    A_enslaverMountID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Mount_PSM.C_Rot_Mount_EnslaveTo_Cmd = P_Mount_PSM_C_Rot_Mount_EnslaveTo_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_StartScanning_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_boundaryPoints': [idl.id(30142147), idl.bound(5)],
    }
)
class P_Mount_PSM_C_Rot_Mount_StartScanning_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_boundaryPoints: Sequence[P_LDM_Common.T_RotationalPosition] = field(default_factory = list)

P_Mount_PSM.C_Rot_Mount_StartScanning_Cmd = P_Mount_PSM_C_Rot_Mount_StartScanning_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_StopScanning_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_StopScanning_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Mount_PSM.C_Rot_Mount_StopScanning_Cmd = P_Mount_PSM_C_Rot_Mount_StopScanning_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_SetWorkMode_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_workMode': [idl.id(177658374), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_SetWorkMode_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_workMode: P_Mount_PSM.T_MountWorkMode = P_Mount_PSM.T_MountWorkMode.L_MountWorkMode_INIT

P_Mount_PSM.C_Rot_Mount_SetWorkMode_Cmd = P_Mount_PSM_C_Rot_Mount_SetWorkMode_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_SetMaintenanceMode_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_maintMode': [idl.id(53543823), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_SetMaintenanceMode_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_maintMode: P_Mount_PSM.T_MaintenanceMode = P_Mount_PSM.T_MaintenanceMode.L_MaintenanceMode_CALIBRATION

P_Mount_PSM.C_Rot_Mount_SetMaintenanceMode_Cmd = P_Mount_PSM_C_Rot_Mount_SetMaintenanceMode_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_SetCalibrationMode_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_calibrationMode': [idl.id(133955208), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_SetCalibrationMode_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_calibrationMode: P_Mount_PSM.T_CalibrationMode = P_Mount_PSM.T_CalibrationMode.L_CalibrationMode_NONE

P_Mount_PSM.C_Rot_Mount_SetCalibrationMode_Cmd = P_Mount_PSM_C_Rot_Mount_SetCalibrationMode_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_StartStabilization_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_StartStabilization_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Mount_PSM.C_Rot_Mount_StartStabilization_Cmd = P_Mount_PSM_C_Rot_Mount_StartStabilization_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_StopStabilization_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_StopStabilization_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Mount_PSM.C_Rot_Mount_StopStabilization_Cmd = P_Mount_PSM_C_Rot_Mount_StopStabilization_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_SetLmcState_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_lmcState': [idl.id(93868992), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_SetLmcState_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_lmcState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Mount_PSM.C_Rot_Mount_SetLmcState_Cmd = P_Mount_PSM_C_Rot_Mount_SetLmcState_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_Set_StabilizationMode_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_stabilizationMode': [idl.id(235248836), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_Set_StabilizationMode_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_stabilizationMode: P_Mount_PSM.T_StabilizationMode = P_Mount_PSM.T_StabilizationMode.L_StabilizationMode_MANUAL

P_Mount_PSM.C_Rot_Mount_Set_StabilizationMode_Cmd = P_Mount_PSM_C_Rot_Mount_Set_StabilizationMode_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Mount_Sight_Enslave_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_mode': [idl.id(236875199), ],
    }
)
class P_Mount_PSM_C_Mount_Sight_Enslave_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_mode: P_LDM_Common.T_SightEnslavement_Mode = P_LDM_Common.T_SightEnslavement_Mode.L_SightEnslavement_Mode_IDLE

P_Mount_PSM.C_Mount_Sight_Enslave_Cmd = P_Mount_PSM_C_Mount_Sight_Enslave_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount_BringToPredefindPosition_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_position': [idl.id(26705633), ],
    }
)
class P_Mount_PSM_C_Rot_Mount_BringToPredefindPosition_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_position: P_Mount_PSM.T_PredefinedPosition = P_Mount_PSM.T_PredefinedPosition.L_PredefinedPosition_LOAD

P_Mount_PSM.C_Rot_Mount_BringToPredefindPosition_Cmd = P_Mount_PSM_C_Rot_Mount_BringToPredefindPosition_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Mount_SetLimits_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_sectorType': [idl.id(49506505), ],
        'A_sectorLimits': [idl.id(143924180), idl.bound(2)],
        'A_sectorAzRef': [idl.id(237128275), ],
    }
)
class P_Mount_PSM_C_Mount_SetLimits_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_sectorType: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_sectorLimits: Sequence[P_LDM_Common.T_RotationalPosition] = field(default_factory = list)
    A_sectorAzRef: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Mount_PSM.C_Mount_SetLimits_Cmd = P_Mount_PSM_C_Mount_SetLimits_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Mount_PSM::C_Mount_BringTo_Event_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Mount_PSM_C_Mount_BringTo_Event_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Mount_PSM.C_Mount_BringTo_Event_Cmd = P_Mount_PSM_C_Mount_BringTo_Event_Cmd
