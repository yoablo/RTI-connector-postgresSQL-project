# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Automotive_PSM.idl
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

P_Automotive_PSM = idl.get_module("P_Automotive_PSM")


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::T_DeviceInformation"),
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
class P_Automotive_PSM_T_DeviceInformation:
    A_idNumber: idl.uint8 = 0
    A_descriptor: P_LDM_Common.T_VeryShortString = field(
        default_factory=P_LDM_Common.T_VeryShortString
    )


P_Automotive_PSM.T_DeviceInformation = P_Automotive_PSM_T_DeviceInformation


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Automotive_PSM::T_BatteryStatus")],
    member_annotations={
        "A_batteryIdNumber": [
            idl.id(31436872),
        ],
        "A_batteryState": [
            idl.id(246937528),
        ],
        "A_batteryPercent": [
            idl.id(47970354),
        ],
        "A_batteryVoltage": [
            idl.id(217129192),
        ],
    },
)
class P_Automotive_PSM_T_BatteryStatus:
    A_batteryIdNumber: idl.uint8 = 0
    A_batteryState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_batteryPercent: float = 0.0
    A_batteryVoltage: float = 0.0


P_Automotive_PSM.T_BatteryStatus = P_Automotive_PSM_T_BatteryStatus


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Automotive_PSM::T_FuelTankStatus")],
    member_annotations={
        "A_fuelTankIdNumber": [
            idl.id(230380499),
        ],
        "A_fuelTankAmount": [
            idl.id(133194151),
        ],
    },
)
class P_Automotive_PSM_T_FuelTankStatus:
    A_fuelTankIdNumber: idl.uint8 = 0
    A_fuelTankAmount: float = 0.0


P_Automotive_PSM.T_FuelTankStatus = P_Automotive_PSM_T_FuelTankStatus


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::C_Automotive_Systems_Specification"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_numberOfTransmisionGears": [
            idl.id(73688494),
        ],
        "A_batteryInformation": [idl.id(91946218), idl.bound(31)],
        "A_fuelTankInformation": [idl.id(200134471), idl.bound(31)],
    },
)
class P_Automotive_PSM_C_Automotive_Systems_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_numberOfTransmisionGears: idl.uint8 = 0
    A_batteryInformation: Sequence[P_Automotive_PSM.T_DeviceInformation] = field(
        default_factory=list
    )
    A_fuelTankInformation: Sequence[P_Automotive_PSM.T_DeviceInformation] = field(
        default_factory=list
    )


P_Automotive_PSM.C_Automotive_Systems_Specification = (
    P_Automotive_PSM_C_Automotive_Systems_Specification
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::C_Automotive_Engine_State"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_fualTankAmount": [idl.id(215947096), idl.bound(31)],
        "A_batteryState": [idl.id(246937528), idl.bound(31)],
    },
)
class P_Automotive_PSM_C_Automotive_Engine_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_fualTankAmount: Sequence[P_Automotive_PSM.T_FuelTankStatus] = field(
        default_factory=list
    )
    A_batteryState: Sequence[P_Automotive_PSM.T_BatteryStatus] = field(
        default_factory=list
    )


P_Automotive_PSM.C_Automotive_Engine_State = P_Automotive_PSM_C_Automotive_Engine_State


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::C_Automotive_Transmission_State"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_gearPosition": [
            idl.id(130920940),
        ],
    },
)
class P_Automotive_PSM_C_Automotive_Transmission_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_gearPosition: idl.uint8 = 0


P_Automotive_PSM.C_Automotive_Transmission_State = (
    P_Automotive_PSM_C_Automotive_Transmission_State
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::C_Automotive_Speedometer"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_measuredSpeed": [
            idl.id(19973484),
        ],
    },
)
class P_Automotive_PSM_C_Automotive_Speedometer:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_measuredSpeed: float = 0.0


P_Automotive_PSM.C_Automotive_Speedometer = P_Automotive_PSM_C_Automotive_Speedometer


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::C_Automotive_Energy_Provider_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_voltage": [
            idl.id(143020390),
        ],
        "A_current": [
            idl.id(133314179),
        ],
    },
)
class P_Automotive_PSM_C_Automotive_Energy_Provider_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_voltage: float = 0.0
    A_current: float = 0.0


P_Automotive_PSM.C_Automotive_Energy_Provider_Status = (
    P_Automotive_PSM_C_Automotive_Energy_Provider_Status
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Automotive_PSM::C_Start_Self_Test_Cmd"),
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
    },
)
class P_Automotive_PSM_C_Start_Self_Test_Cmd:
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


P_Automotive_PSM.C_Start_Self_Test_Cmd = P_Automotive_PSM_C_Start_Self_Test_Cmd
