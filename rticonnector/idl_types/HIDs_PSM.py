# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from HIDs_PSM.idl
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

P_HIDs_PSM = idl.get_module("P_HIDs_PSM")

P_HIDs_PSM_T_Validity = bool

P_HIDs_PSM.T_Validity = P_HIDs_PSM_T_Validity

P_HIDs_PSM_T_Priority = idl.uint8

P_HIDs_PSM.T_Priority = P_HIDs_PSM_T_Priority


@idl.alias(
    annotations=[
        idl.bound(32),
    ]
)
class P_HIDs_PSM_T_SwitchesDescription:
    value: Sequence[P_LDM_Common.T_ShortString] = field(default_factory=list)


P_HIDs_PSM.T_SwitchesDescription = P_HIDs_PSM_T_SwitchesDescription


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::T_JoystickRawData")],
    member_annotations={
        "A_sequentialNumber": [
            idl.id(161977479),
        ],
        "A_xVal": [
            idl.id(64568935),
        ],
        "A_yVal": [
            idl.id(218721993),
        ],
    },
)
class P_HIDs_PSM_T_JoystickRawData:
    A_sequentialNumber: idl.uint8 = 0
    A_xVal: float = 0.0
    A_yVal: float = 0.0


P_HIDs_PSM.T_JoystickRawData = P_HIDs_PSM_T_JoystickRawData


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::T_JoystickShapedData")],
    member_annotations={
        "A_sequentialNumber": [
            idl.id(161977479),
        ],
        "A_xVal": [
            idl.id(64568935),
        ],
        "A_yVal": [
            idl.id(218721993),
        ],
    },
)
class P_HIDs_PSM_T_JoystickShapedData:
    A_sequentialNumber: idl.uint8 = 0
    A_xVal: float = 0.0
    A_yVal: float = 0.0


P_HIDs_PSM.T_JoystickShapedData = P_HIDs_PSM_T_JoystickShapedData


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::T_JoystickParams")],
    member_annotations={
        "A_sequentialNumber": [
            idl.id(161977479),
        ],
        "A_isShapingSupported": [
            idl.id(27651834),
        ],
    },
)
class P_HIDs_PSM_T_JoystickParams:
    A_sequentialNumber: idl.uint8 = 0
    A_isShapingSupported: bool = False


P_HIDs_PSM.T_JoystickParams = P_HIDs_PSM_T_JoystickParams


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_HIDs_PSM::T_JoysticksSpecification"),
    ],
    member_annotations={
        "A_numberOfJoysticks": [
            idl.id(99592372),
        ],
        "A_joystickParams": [idl.id(199031102), idl.bound(16)],
    },
)
class P_HIDs_PSM_T_JoysticksSpecification:
    A_numberOfJoysticks: idl.uint8 = 0
    A_joystickParams: Sequence[P_HIDs_PSM.T_JoystickParams] = field(
        default_factory=list
    )


P_HIDs_PSM.T_JoysticksSpecification = P_HIDs_PSM_T_JoysticksSpecification


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::C_HID_Specification")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_priority": [
            idl.id(261701171),
        ],
        "A_joysticksSpecification": [
            idl.id(159321212),
        ],
        "A_numberOfInputSwitches": [
            idl.id(262096556),
        ],
        "A_numberOfOutputSwitches": [
            idl.id(224272178),
        ],
        "A_inputSwitchesDescriptors": [
            idl.id(227179339),
        ],
        "A_outputSwitchesDescriptors": [
            idl.id(182788638),
        ],
    },
)
class P_HIDs_PSM_C_HID_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_priority: idl.uint8 = 0
    A_joysticksSpecification: P_HIDs_PSM.T_JoysticksSpecification = field(
        default_factory=P_HIDs_PSM.T_JoysticksSpecification
    )
    A_numberOfInputSwitches: idl.uint8 = 0
    A_numberOfOutputSwitches: idl.uint8 = 0
    A_inputSwitchesDescriptors: P_HIDs_PSM.T_SwitchesDescription = field(
        default_factory=P_HIDs_PSM.T_SwitchesDescription
    )
    A_outputSwitchesDescriptors: P_HIDs_PSM.T_SwitchesDescription = field(
        default_factory=P_HIDs_PSM.T_SwitchesDescription
    )


P_HIDs_PSM.C_HID_Specification = P_HIDs_PSM_C_HID_Specification


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::C_Joysticks_Raw_Status")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_listOfJoystickRawStatus": [idl.id(13373586), idl.bound(30)],
    },
)
class P_HIDs_PSM_C_Joysticks_Raw_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_listOfJoystickRawStatus: Sequence[P_HIDs_PSM.T_JoystickRawData] = field(
        default_factory=list
    )


P_HIDs_PSM.C_Joysticks_Raw_Status = P_HIDs_PSM_C_Joysticks_Raw_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_HIDs_PSM::C_Joysticks_Shaped_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_listOfJoystickShapedStatus": [idl.id(155587927), idl.bound(30)],
    },
)
class P_HIDs_PSM_C_Joysticks_Shaped_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_listOfJoystickShapedStatus: Sequence[P_HIDs_PSM.T_JoystickShapedData] = field(
        default_factory=list
    )


P_HIDs_PSM.C_Joysticks_Shaped_Status = P_HIDs_PSM_C_Joysticks_Shaped_Status


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::C_HID_Switches_Status")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_inputSwitches": [
            idl.id(153847315),
        ],
        "A_inputSwitchesValidity": [
            idl.id(200199832),
        ],
    },
)
class P_HIDs_PSM_C_HID_Switches_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_inputSwitches: idl.int32 = 0
    A_inputSwitchesValidity: idl.int32 = 0


P_HIDs_PSM.C_HID_Switches_Status = P_HIDs_PSM_C_HID_Switches_Status


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_HIDs_PSM::C_Switches_Cmd")],
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
        "A_switches": [
            idl.id(56251523),
        ],
        "A_switchesMask": [
            idl.id(55233567),
        ],
    },
)
class P_HIDs_PSM_C_Switches_Cmd:
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
    A_switches: idl.int32 = 0
    A_switchesMask: idl.int32 = 0


P_HIDs_PSM.C_Switches_Cmd = P_HIDs_PSM_C_Switches_Cmd
