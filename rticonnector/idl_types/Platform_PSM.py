# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Platform_PSM.idl
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

P_Platform_PSM = idl.get_module("P_Platform_PSM")


@idl.enum
class P_Platform_PSM_T_PlatformMode(IntEnum):
    L_PlatformMode_OPERATION = 0
    L_PlatformMode_SIMULATION = 1
    L_PlatformMode_BURNING = 2
    L_PlatformMode_CALIBRATION = 3
    L_PlatformMode_MAINTENANCE = 4
    L_PlatformMode_TECH_MAINTENANCE = 5


P_Platform_PSM.T_PlatformMode = P_Platform_PSM_T_PlatformMode


@idl.enum
class P_Platform_PSM_T_HatchState(IntEnum):
    L_HatchState_OPEN = 0
    L_HatchState_SEMI = 1
    L_HatchState_CLOSED = 2
    L_HatchState_FAULT = 3


P_Platform_PSM.T_HatchState = P_Platform_PSM_T_HatchState


@idl.enum
class P_Platform_PSM_T_MissionState(IntEnum):
    L_MissionState_MOVING_TOWARD_CONTACT = 0
    L_MissionState_SIGHTS_POSITION = 1
    L_MissionState_FIRING_POSITION = 2
    L_MissionState_ENCOUNTER = 3
    L_MissionState_PERIPHERAL_SECURITY = 4


P_Platform_PSM.T_MissionState = P_Platform_PSM_T_MissionState


@idl.enum
class P_Platform_PSM_T_CombatStateController(IntEnum):
    L_CombatStateController_COMMANDER = 0
    L_CombatStateController_ALGORITHM = 1


P_Platform_PSM.T_CombatStateController = P_Platform_PSM_T_CombatStateController


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Platform_PSM::T_HatchStatus")],
    member_annotations={
        "A_hatchIdNumber": [
            idl.id(119323304),
        ],
        "A_hatchState": [
            idl.id(198448767),
        ],
    },
)
class P_Platform_PSM_T_HatchStatus:
    A_hatchIdNumber: idl.uint8 = 0
    A_hatchState: P_Platform_PSM.T_HatchState = (
        P_Platform_PSM.T_HatchState.L_HatchState_OPEN
    )


P_Platform_PSM.T_HatchStatus = P_Platform_PSM_T_HatchStatus


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Platform_PSM::T_LightStatus")],
    member_annotations={
        "A_lightsIdNumber": [
            idl.id(134658096),
        ],
        "A_lightsState": [
            idl.id(20658126),
        ],
    },
)
class P_Platform_PSM_T_LightStatus:
    A_lightsIdNumber: idl.uint8 = 0
    A_lightsState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON


P_Platform_PSM.T_LightStatus = P_Platform_PSM_T_LightStatus


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::T_DeviceInformation"),
    ],
    member_annotations={
        "A_idNumber": [
            idl.id(106058244),
        ],
        "A_descriptor": [
            idl.id(52732520),
        ],
    },
)
class P_Platform_PSM_T_DeviceInformation:
    A_idNumber: idl.uint8 = 0
    A_descriptor: P_LDM_Common.T_VeryShortString = field(
        default_factory=P_LDM_Common.T_VeryShortString
    )


P_Platform_PSM.T_DeviceInformation = P_Platform_PSM_T_DeviceInformation


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Systems_Specification"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_hatchesInformation": [idl.id(154651479), idl.bound(31)],
        "A_lightsInformation": [idl.id(163989469), idl.bound(31)],
        "A_platformType": [
            idl.id(23982935),
        ],
        "A_platformSubType": [
            idl.id(9101197),
        ],
        "A_fcsSupport": [
            idl.id(252838819),
        ],
        "A_fcsType": [
            idl.id(70507212),
        ],
        "A_apsSupport": [
            idl.id(134940479),
        ],
    },
)
class P_Platform_PSM_C_Platform_Systems_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_hatchesInformation: Sequence[P_Platform_PSM.T_DeviceInformation] = field(
        default_factory=list
    )
    A_lightsInformation: Sequence[P_Platform_PSM.T_DeviceInformation] = field(
        default_factory=list
    )
    A_platformType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_platformSubType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_fcsSupport: bool = False
    A_fcsType: Optional[P_LDM_Common.T_ShortString] = None
    A_apsSupport: bool = False


P_Platform_PSM.C_Platform_Systems_Specification = (
    P_Platform_PSM_C_Platform_Systems_Specification
)


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Platform_PSM::C_Platform_State")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_platform": [
            idl.id(29421584),
        ],
        "A_platformSubType": [
            idl.id(9101197),
        ],
        "A_operationalMode": [
            idl.id(47535655),
        ],
    },
)
class P_Platform_PSM_C_Platform_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_platform: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_platformSubType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_operationalMode: P_Platform_PSM.T_PlatformMode = (
        P_Platform_PSM.T_PlatformMode.L_PlatformMode_OPERATION
    )


P_Platform_PSM.C_Platform_State = P_Platform_PSM_C_Platform_State


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Spatial_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_platformAttitude": [
            idl.id(258980669),
        ],
        "A_platformBearing": [
            idl.id(173478804),
        ],
        "A_platformIsMoving": [
            idl.id(114595823),
        ],
        "A_platformHeading": [
            idl.id(135912205),
        ],
    },
)
class P_Platform_PSM_C_Platform_Spatial_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_platformAttitude: P_LDM_Common.T_Attitude = field(
        default_factory=P_LDM_Common.T_Attitude
    )
    A_platformBearing: float = 0.0
    A_platformIsMoving: bool = False
    A_platformHeading: float = 0.0


P_Platform_PSM.C_Platform_Spatial_Status = P_Platform_PSM_C_Platform_Spatial_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Environment_Parameters"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_vicinityTemperature": [
            idl.id(209766739),
        ],
        "A_humidity": [
            idl.id(40463860),
        ],
        "A_airPressure": [
            idl.id(157462497),
        ],
        "A_windSpeed": [
            idl.id(219447323),
        ],
        "A_windDirection": [
            idl.id(25861558),
        ],
        "A_airPollution": [
            idl.id(170607418),
        ],
        "A_visibility": [
            idl.id(60271523),
        ],
        "A_lightingIntensity": [
            idl.id(177878861),
        ],
    },
)
class P_Platform_PSM_C_Platform_Environment_Parameters:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_vicinityTemperature: float = 0.0
    A_humidity: float = 0.0
    A_airPressure: float = 0.0
    A_windSpeed: float = 0.0
    A_windDirection: float = 0.0
    A_airPollution: float = 0.0
    A_visibility: float = 0.0
    A_lightingIntensity: float = 0.0


P_Platform_PSM.C_Platform_Environment_Parameters = (
    P_Platform_PSM_C_Platform_Environment_Parameters
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Internal_Parameters"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_temperature": [
            idl.id(242883168),
        ],
        "A_humidity": [
            idl.id(40463860),
        ],
        "A_airPressure": [
            idl.id(157462497),
        ],
    },
)
class P_Platform_PSM_C_Platform_Internal_Parameters:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_temperature: float = 0.0
    A_humidity: float = 0.0
    A_airPressure: float = 0.0


P_Platform_PSM.C_Platform_Internal_Parameters = (
    P_Platform_PSM_C_Platform_Internal_Parameters
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Peripherial"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_hatchesState": [idl.id(249359146), idl.bound(31)],
        "A_lightsState": [idl.id(20658126), idl.bound(31)],
    },
)
class P_Platform_PSM_C_Platform_Peripherial:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_hatchesState: Sequence[P_Platform_PSM.T_HatchStatus] = field(default_factory=list)
    A_lightsState: Sequence[P_Platform_PSM.T_LightStatus] = field(default_factory=list)


P_Platform_PSM.C_Platform_Peripherial = P_Platform_PSM_C_Platform_Peripherial


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Combat_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_combatStatus": [
            idl.id(71283897),
        ],
        "A_currentController": [
            idl.id(196408582),
        ],
    },
)
class P_Platform_PSM_C_Platform_Combat_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_combatStatus: P_Platform_PSM.T_MissionState = (
        P_Platform_PSM.T_MissionState.L_MissionState_MOVING_TOWARD_CONTACT
    )
    A_currentController: P_Platform_PSM.T_CombatStateController = (
        P_Platform_PSM.T_CombatStateController.L_CombatStateController_COMMANDER
    )


P_Platform_PSM.C_Platform_Combat_Status = P_Platform_PSM_C_Platform_Combat_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Platform_Commands_Response"),
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
        "A_metadata": [
            idl.id(88603227),
        ],
        "A_responseState": [
            idl.id(203692061),
        ],
        "A_additionalCode": [
            idl.id(51197241),
        ],
    },
)
class P_Platform_PSM_C_Platform_Commands_Response:
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
    A_metadata: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_responseState: P_LDM_Common.T_Command_Response = (
        P_LDM_Common.T_Command_Response.L_Command_Response_INVALID
    )
    A_additionalCode: idl.int32 = 0


P_Platform_PSM.C_Platform_Commands_Response = (
    P_Platform_PSM_C_Platform_Commands_Response
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Set_Operational_Mode_Cmd"),
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
        "A_operationalMode": [
            idl.id(47535655),
        ],
    },
)
class P_Platform_PSM_C_Set_Operational_Mode_Cmd:
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
    A_operationalMode: P_Platform_PSM.T_PlatformMode = (
        P_Platform_PSM.T_PlatformMode.L_PlatformMode_OPERATION
    )


P_Platform_PSM.C_Set_Operational_Mode_Cmd = P_Platform_PSM_C_Set_Operational_Mode_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Platform_PSM::C_Force_Manual_Control_Cmd"),
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
        "A_manualControl": [
            idl.id(12790092),
        ],
    },
)
class P_Platform_PSM_C_Force_Manual_Control_Cmd:
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
    A_manualControl: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON


P_Platform_PSM.C_Force_Manual_Control_Cmd = P_Platform_PSM_C_Force_Manual_Control_Cmd
