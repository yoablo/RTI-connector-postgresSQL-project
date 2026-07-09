# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Optronic_Systems_PSM.idl
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

P_Optronic_Systems_PSM = idl.get_module("P_Optronic_Systems_PSM")


@idl.enum
class P_Optronic_Systems_PSM_T_Operation_Mode(IntEnum):
    L_Operation_Mode_INIT = 0
    L_Operation_Mode_OBSERVE = 1
    L_Operation_Mode_SHIELD = 2
    L_Operation_Mode_R_MODE = 3
    L_Operation_Mode_CONTROL = 4
    L_Operation_Mode_IBIT = 5
    L_Operation_Mode_BORESIGHT = 6
    L_Operation_Mode_MAINT = 7
    L_Operation_Mode_NON_OPER = 8
    L_Operation_Mode_VB_TRACK = 9
    L_Operation_Mode_SCAN = 10
    L_Operation_Mode_S_MODE = 11
    L_Operation_Mode_TRACK = 12


P_Optronic_Systems_PSM.T_Operation_Mode = P_Optronic_Systems_PSM_T_Operation_Mode


@idl.enum
class P_Optronic_Systems_PSM_T_Train_Status(IntEnum):
    L_Train_Status_OPERATIONAL = 0
    L_Train_Status_STOP_TRAIN = 1
    L_Train_Status_TRAIN = 2


P_Optronic_Systems_PSM.T_Train_Status = P_Optronic_Systems_PSM_T_Train_Status


@idl.enum
class P_Optronic_Systems_PSM_T_Control_Mode(IntEnum):
    L_Control_Mode_BMS_CONTROL = 0
    L_Control_Mode_INDEPENDENT = 1


P_Optronic_Systems_PSM.T_Control_Mode = P_Optronic_Systems_PSM_T_Control_Mode


@idl.enum
class P_Optronic_Systems_PSM_T_Action(IntEnum):
    L_Action_DETECT = 0
    L_Action_SCAN = 1


P_Optronic_Systems_PSM.T_Action = P_Optronic_Systems_PSM_T_Action


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_System_Specification"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_System_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )


P_Optronic_Systems_PSM.C_Optronic_System_Specification = (
    P_Optronic_Systems_PSM_C_Optronic_System_Specification
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_System_Video_Specification"),
    ],
    member_annotations={
        "A_supportedVideoStreams": [idl.id(200954828), idl.bound(20)],
        "A_videoStreamAssignmentSupport": [
            idl.id(237239723),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_System_Video_Specification(
    P_Optronic_Systems_PSM.C_Optronic_System_Specification
):
    A_supportedVideoStreams: Sequence[P_LDM_Common.T_Identifier] = field(
        default_factory=list
    )
    A_videoStreamAssignmentSupport: bool = False


P_Optronic_Systems_PSM.C_Optronic_System_Video_Specification = (
    P_Optronic_Systems_PSM_C_Optronic_System_Video_Specification
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Command_Response"),
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
class P_Optronic_Systems_PSM_C_Optronic_Command_Response:
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


P_Optronic_Systems_PSM.C_Optronic_Command_Response = (
    P_Optronic_Systems_PSM_C_Optronic_Command_Response
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_System_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_System_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )


P_Optronic_Systems_PSM.C_Optronic_System_Status = (
    P_Optronic_Systems_PSM_C_Optronic_System_Status
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Extended_Status"),
    ],
    member_annotations={
        "A_operationMode": [
            idl.id(76810895),
        ],
        "A_workMode": [
            idl.id(177658374),
        ],
        "A_trainStatus": [
            idl.id(110582757),
        ],
        "A_controlMode": [
            idl.id(50066142),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Extended_Status(
    P_Optronic_Systems_PSM.C_Optronic_System_Status
):
    A_operationMode: P_Optronic_Systems_PSM.T_Operation_Mode = (
        P_Optronic_Systems_PSM.T_Operation_Mode.L_Operation_Mode_INIT
    )
    A_workMode: P_Optronic_Systems_PSM.T_Operation_Mode = (
        P_Optronic_Systems_PSM.T_Operation_Mode.L_Operation_Mode_INIT
    )
    A_trainStatus: P_Optronic_Systems_PSM.T_Train_Status = (
        P_Optronic_Systems_PSM.T_Train_Status.L_Train_Status_OPERATIONAL
    )
    A_controlMode: P_Optronic_Systems_PSM.T_Control_Mode = (
        P_Optronic_Systems_PSM.T_Control_Mode.L_Control_Mode_BMS_CONTROL
    )


P_Optronic_Systems_PSM.C_Optronic_Extended_Status = (
    P_Optronic_Systems_PSM_C_Optronic_Extended_Status
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Concealed_Status"),
    ],
    member_annotations={
        "A_param1": [
            idl.id(152639104),
        ],
        "A_param2": [
            idl.id(251279978),
        ],
        "A_param3": [
            idl.id(206306990),
        ],
        "A_param4": [
            idl.id(145519628),
        ],
        "A_param5": [
            idl.id(43395246),
        ],
        "A_param6": [
            idl.id(40658848),
        ],
        "A_param7": [
            idl.id(63544000),
        ],
        "A_param8": [
            idl.id(176032680),
        ],
        "A_param9": [
            idl.id(73878328),
        ],
        "A_param10": [
            idl.id(267026459),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Concealed_Status(
    P_Optronic_Systems_PSM.C_Optronic_System_Status
):
    A_param1: idl.uint8 = 0
    A_param2: idl.uint8 = 0
    A_param3: idl.uint8 = 0
    A_param4: idl.uint8 = 0
    A_param5: idl.uint8 = 0
    A_param6: idl.uint8 = 0
    A_param7: idl.uint8 = 0
    A_param8: idl.uint8 = 0
    A_param9: idl.uint8 = 0
    A_param10: idl.uint8 = 0


P_Optronic_Systems_PSM.C_Optronic_Concealed_Status = (
    P_Optronic_Systems_PSM_C_Optronic_Concealed_Status
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Work_Params"),
    ],
    member_annotations={
        "A_param1": [
            idl.id(152639104),
        ],
        "A_param2": [
            idl.id(251279978),
        ],
        "A_param3": [
            idl.id(206306990),
        ],
        "A_param4": [
            idl.id(145519628),
        ],
        "A_param5": [
            idl.id(43395246),
        ],
        "A_param6": [
            idl.id(40658848),
        ],
        "A_param7": [
            idl.id(63544000),
        ],
        "A_param8": [
            idl.id(176032680),
        ],
        "A_param9": [
            idl.id(73878328),
        ],
        "A_param10": [
            idl.id(267026459),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Work_Params(
    P_Optronic_Systems_PSM.C_Optronic_System_Status
):
    A_param1: idl.uint8 = 0
    A_param2: idl.uint8 = 0
    A_param3: idl.uint8 = 0
    A_param4: idl.uint8 = 0
    A_param5: idl.uint8 = 0
    A_param6: idl.uint8 = 0
    A_param7: idl.uint8 = 0
    A_param8: idl.uint8 = 0
    A_param9: idl.uint8 = 0
    A_param10: idl.uint8 = 0


P_Optronic_Systems_PSM.C_Optronic_Work_Params = (
    P_Optronic_Systems_PSM_C_Optronic_Work_Params
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Request_Range_Cmd"),
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
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Request_Range_Cmd:
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


P_Optronic_Systems_PSM.C_Optronic_Request_Range_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Request_Range_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Start_Stream_Cmd"),
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
        "A_streamID": [
            idl.id(162484737),
        ],
        "A_detectorType": [
            idl.id(81702893),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Start_Stream_Cmd:
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
    A_streamID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_detectorType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )


P_Optronic_Systems_PSM.C_Optronic_Start_Stream_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Start_Stream_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Stop_Processing_Stream_Cmd"),
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
        "A_streamID": [
            idl.id(162484737),
        ],
        "A_detectorType": [
            idl.id(81702893),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Stop_Processing_Stream_Cmd:
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
    A_streamID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_detectorType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )


P_Optronic_Systems_PSM.C_Optronic_Stop_Processing_Stream_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Stop_Processing_Stream_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Set_Operation_Mode_Cmd"),
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
        "A_mode": [
            idl.id(236875199),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Set_Operation_Mode_Cmd:
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
    A_mode: P_Optronic_Systems_PSM.T_Operation_Mode = (
        P_Optronic_Systems_PSM.T_Operation_Mode.L_Operation_Mode_INIT
    )


P_Optronic_Systems_PSM.C_Optronic_Set_Operation_Mode_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Set_Operation_Mode_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Password_Notify_Cmd"),
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
        "A_password": [
            idl.id(266394819),
        ],
        "A_passwordType": [
            idl.id(43477988),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Password_Notify_Cmd:
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
    A_password: idl.int16 = 0
    A_passwordType: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )


P_Optronic_Systems_PSM.C_Optronic_Password_Notify_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Password_Notify_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Set_Action_Cmd"),
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
        "A_action": [
            idl.id(224299759),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Set_Action_Cmd:
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
    A_action: P_Optronic_Systems_PSM.T_Action = (
        P_Optronic_Systems_PSM.T_Action.L_Action_DETECT
    )


P_Optronic_Systems_PSM.C_Optronic_Set_Action_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Set_Action_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Set_Work_Params_Cmd"),
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
        "A_param1": [
            idl.id(152639104),
        ],
        "A_param2": [
            idl.id(251279978),
        ],
        "A_param3": [
            idl.id(206306990),
        ],
        "A_param4": [
            idl.id(145519628),
        ],
        "A_param5": [
            idl.id(43395246),
        ],
        "A_param6": [
            idl.id(40658848),
        ],
        "A_param7": [
            idl.id(63544000),
        ],
        "A_param8": [
            idl.id(176032680),
        ],
        "A_param9": [
            idl.id(73878328),
        ],
        "A_param10": [
            idl.id(267026459),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Set_Work_Params_Cmd:
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
    A_param1: idl.uint8 = 0
    A_param2: idl.uint8 = 0
    A_param3: idl.uint8 = 0
    A_param4: idl.uint8 = 0
    A_param5: idl.uint8 = 0
    A_param6: idl.uint8 = 0
    A_param7: idl.uint8 = 0
    A_param8: idl.uint8 = 0
    A_param9: idl.uint8 = 0
    A_param10: idl.uint8 = 0


P_Optronic_Systems_PSM.C_Optronic_Set_Work_Params_Cmd = (
    P_Optronic_Systems_PSM_C_Optronic_Set_Work_Params_Cmd
)


@idl.enum
class P_Optronic_Systems_PSM_T_Boresight_Step(IntEnum):
    L_Boresight_Step_START = 0
    L_Boresight_Step_LASE = 1
    L_Boresight_Step_BORESIGHT_IN = 2
    L_Boresight_Step_TARGET_ON = 3
    L_Boresight_Step_ROTATE_IMAGE = 4
    L_Boresight_Step_FIX_CROSS_POSITION = 5
    L_Boresight_Step_FIX_CROSS_POSITION_FLIR = 6
    L_Boresight_Step_FINISH = 7


P_Optronic_Systems_PSM.T_Boresight_Step = P_Optronic_Systems_PSM_T_Boresight_Step


@idl.enum
class P_Optronic_Systems_PSM_T_Boresight_Directive(IntEnum):
    L_Boresight_Directive_PICTURE1 = 0
    L_Boresight_Directive_PICTURE2 = 1


P_Optronic_Systems_PSM.T_Boresight_Directive = (
    P_Optronic_Systems_PSM_T_Boresight_Directive
)


@idl.enum
class P_Optronic_Systems_PSM_T_FLIR_Camera_Control(IntEnum):
    L_FLIR_Camera_Control_POWER = 0
    L_FLIR_Camera_Control_CONTINUOUS_ZOOM = 1
    L_FLIR_Camera_Control_ZOOM_GO_TO_PAL = 2
    L_FLIR_Camera_Control_GAIN_LEVEL_MODE = 3
    L_FLIR_Camera_Control_MANUAL_GAIN = 4
    L_FLIR_Camera_Control_MANUAL_LEVEL = 5
    L_FLIR_Camera_Control_FOCUS_CONTROL = 6
    L_FLIR_Camera_Control_IMAGE_POLARITY = 7
    L_FLIR_Camera_Control_DIGITAL_ZOOM = 8
    L_FLIR_Camera_Control_NUC = 9
    L_FLIR_Camera_Control_EMPHASIS = 10
    L_FLIR_Camera_Control_ZOOM_GO_TO_HDSDI = 11
    L_FLIR_Camera_Control_TURBULENCE_CONTROL = 12
    L_FLIR_Camera_Control_SET_DEFAULT = 13


P_Optronic_Systems_PSM.T_FLIR_Camera_Control = (
    P_Optronic_Systems_PSM_T_FLIR_Camera_Control
)


@idl.enum
class P_Optronic_Systems_PSM_T_Sight_Type(IntEnum):
    L_Sight_Type_KATLANIT = 0
    L_Sight_Type_COMMANDER_SIGHT = 1
    L_Sight_Type_GUNNER_SIGHT = 2


P_Optronic_Systems_PSM.T_Sight_Type = P_Optronic_Systems_PSM_T_Sight_Type


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Optronic_Boresight_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_paramNum1": [
            idl.id(42727018),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Optronic_Boresight_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_paramNum1: idl.int16 = 0


P_Optronic_Systems_PSM.C_Optronic_Boresight_Status = (
    P_Optronic_Systems_PSM_C_Optronic_Boresight_Status
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Boresight_Action_Status"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_action": [
            idl.id(224299759),
        ],
        "A_status": [
            idl.id(207505413),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Boresight_Action_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_action: P_LDM_Common.T_System_Action = (
        P_LDM_Common.T_System_Action.L_System_Action_START
    )
    A_status: P_LDM_Common.T_Command_Response = (
        P_LDM_Common.T_Command_Response.L_Command_Response_INVALID
    )


P_Optronic_Systems_PSM.C_Boresight_Action_Status = (
    P_Optronic_Systems_PSM_C_Boresight_Action_Status
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Boresight_Next_Cmd"),
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
        "A_nextStep": [
            idl.id(156256486),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Boresight_Next_Cmd:
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
    A_nextStep: P_Optronic_Systems_PSM.T_Boresight_Step = (
        P_Optronic_Systems_PSM.T_Boresight_Step.L_Boresight_Step_START
    )


P_Optronic_Systems_PSM.C_Boresight_Next_Cmd = (
    P_Optronic_Systems_PSM_C_Boresight_Next_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_TV_Boresight_Cmd"),
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
        "A_command": [
            idl.id(121859441),
        ],
    },
)
class P_Optronic_Systems_PSM_C_TV_Boresight_Cmd:
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
    A_command: P_Optronic_Systems_PSM.T_Boresight_Directive = (
        P_Optronic_Systems_PSM.T_Boresight_Directive.L_Boresight_Directive_PICTURE1
    )


P_Optronic_Systems_PSM.C_TV_Boresight_Cmd = P_Optronic_Systems_PSM_C_TV_Boresight_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Sight_Enslave_Cmd"),
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
        "A_mode": [
            idl.id(236875199),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Sight_Enslave_Cmd:
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
    A_mode: P_LDM_Common.T_SightEnslavement_Mode = (
        P_LDM_Common.T_SightEnslavement_Mode.L_SightEnslavement_Mode_IDLE
    )


P_Optronic_Systems_PSM.C_Sight_Enslave_Cmd = P_Optronic_Systems_PSM_C_Sight_Enslave_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Sight_FlirCameraControl_Cmd"),
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
        "A_command": [
            idl.id(121859441),
        ],
        "A_data": [
            idl.id(99029611),
        ],
        "A_sightType": [
            idl.id(25624126),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Sight_FlirCameraControl_Cmd:
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
    A_command: P_LDM_Common.T_SightEnslavement_Mode = (
        P_LDM_Common.T_SightEnslavement_Mode.L_SightEnslavement_Mode_IDLE
    )
    A_data: idl.uint16 = 0
    A_sightType: P_Optronic_Systems_PSM.T_Sight_Type = (
        P_Optronic_Systems_PSM.T_Sight_Type.L_Sight_Type_KATLANIT
    )


P_Optronic_Systems_PSM.C_Sight_FlirCameraControl_Cmd = (
    P_Optronic_Systems_PSM_C_Sight_FlirCameraControl_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Optronic_Systems_PSM::C_Boresight_Action_Cmd"),
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
        "A_action": [
            idl.id(224299759),
        ],
    },
)
class P_Optronic_Systems_PSM_C_Boresight_Action_Cmd:
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
    A_action: P_LDM_Common.T_System_Action = (
        P_LDM_Common.T_System_Action.L_System_Action_START
    )


P_Optronic_Systems_PSM.C_Boresight_Action_Cmd = (
    P_Optronic_Systems_PSM_C_Boresight_Action_Cmd
)
