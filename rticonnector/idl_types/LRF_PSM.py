
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from LRF_PSM.idl
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

from LDM_Common import *

P_LRF_PSM = idl.get_module("P_LRF_PSM")

@idl.enum
class P_LRF_PSM_T_LRF_State(IntEnum):
    L_LRF_State_SINGLE = 0
    L_LRF_State_MULTI = 1
    L_LRF_State_HIGH_SPEED = 2

P_LRF_PSM.T_LRF_State = P_LRF_PSM_T_LRF_State

@idl.enum
class P_LRF_PSM_T_LRF_LasingStatus(IntEnum):
    L_LRF_LasingStatus_NONE = 0
    L_LRF_LasingStatus_SINGLE = 1
    L_LRF_LasingStatus_MULTI = 2
    L_LRF_LasingStatus_ERROR = 3

P_LRF_PSM.T_LRF_LasingStatus = P_LRF_PSM_T_LRF_LasingStatus

@idl.enum
class P_LRF_PSM_T_LRF_RangeType(IntEnum):
    L_LRF_RangeType_MANUAL = 0
    L_LRF_RangeType_MEASURED = 1
    L_LRF_RangeType_BATTLE = 2
    L_LRF_RangeType_MINIMAL = 3
    L_LRF_RangeType_TRAVEL = 4

P_LRF_PSM.T_LRF_RangeType = P_LRF_PSM_T_LRF_RangeType

@idl.enum
class P_LRF_PSM_T_LRF_RangeAccuracy(IntEnum):
    L_LRF_RangeAccuracy_ACCURATE = 0
    L_LRF_RangeAccuracy_MEASURED = 1

P_LRF_PSM.T_LRF_RangeAccuracy = P_LRF_PSM_T_LRF_RangeAccuracy

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::T_MeasuredRange")],
    member_annotations = {
        'A_rangeValue': [idl.id(159489137), ],
        'A_sequenceNumber': [idl.id(232152101), ],
    }
)
class P_LRF_PSM_T_MeasuredRange:
    A_rangeValue: float = 0.0
    A_sequenceNumber: idl.int16 = 0

P_LRF_PSM.T_MeasuredRange = P_LRF_PSM_T_MeasuredRange

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_minRange': [idl.id(100609151), ],
        'A_maxRange': [idl.id(97585923), ],
        'A_lrfModesSupport': [idl.id(129189752), idl.bound(5)],
        'A_lrfSourceID': [idl.id(108686414), ],
    }
)
class P_LRF_PSM_C_LRF_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_minRange: float = 0.0
    A_maxRange: float = 0.0
    A_lrfModesSupport: Sequence[P_LRF_PSM.T_LRF_State] = field(default_factory = list)
    A_lrfSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_LRF_PSM.C_LRF_Specification = P_LRF_PSM_C_LRF_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_lrfState': [idl.id(172310794), ],
    }
)
class P_LRF_PSM_C_LRF:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_lrfState: P_LRF_PSM.T_LRF_State = P_LRF_PSM.T_LRF_State.L_LRF_State_SINGLE

P_LRF_PSM.C_LRF = P_LRF_PSM_C_LRF

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_Measurement")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_rangeMeasurements': [idl.id(7195534), idl.bound(6)],
        'A_rangeType': [idl.id(216707555), ],
        'A_lasingStatus': [idl.id(261603226), ],
        'A_rangeAccuracy': [idl.id(210806210), ],
        'A_measureRangeSeqNum': [idl.id(169185660), ],
    }
)
class P_LRF_PSM_C_LRF_Measurement:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_rangeMeasurements: Sequence[P_LRF_PSM.T_MeasuredRange] = field(default_factory = list)
    A_rangeType: P_LRF_PSM.T_LRF_RangeType = P_LRF_PSM.T_LRF_RangeType.L_LRF_RangeType_MANUAL
    A_lasingStatus: P_LRF_PSM.T_LRF_LasingStatus = P_LRF_PSM.T_LRF_LasingStatus.L_LRF_LasingStatus_NONE
    A_rangeAccuracy: P_LRF_PSM.T_LRF_RangeAccuracy = P_LRF_PSM.T_LRF_RangeAccuracy.L_LRF_RangeAccuracy_ACCURATE
    A_measureRangeSeqNum: idl.int16 = 0

P_LRF_PSM.C_LRF_Measurement = P_LRF_PSM_C_LRF_Measurement

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_Measurement_Extended")],
    member_annotations = {
        'A_lasingLocation': [idl.id(91000504), ],
        'A_lasingInitiator': [idl.id(136519591), ],
    }
)
class P_LRF_PSM_C_LRF_Measurement_Extended(P_LRF_PSM.C_LRF_Measurement):
    A_lasingLocation: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_lasingInitiator: P_LDM_Common.T_Operator = P_LDM_Common.T_Operator.L_Operator_COMMANDER

P_LRF_PSM.C_LRF_Measurement_Extended = P_LRF_PSM_C_LRF_Measurement_Extended

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_StartFiringLaser_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_lrfType': [idl.id(111760909), ],
    }
)
class P_LRF_PSM_C_LRF_StartFiringLaser_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_lrfType: idl.uint8 = 0

P_LRF_PSM.C_LRF_StartFiringLaser_Cmd = P_LRF_PSM_C_LRF_StartFiringLaser_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_StopFiringLaser_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_LRF_PSM_C_LRF_StopFiringLaser_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_LRF_PSM.C_LRF_StopFiringLaser_Cmd = P_LRF_PSM_C_LRF_StopFiringLaser_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_SetRangeType_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_rangeType': [idl.id(216707555), ],
        'A_measuredRangeSeqNum': [idl.id(134485417), ],
        'A_rangeValue': [idl.id(159489137), ],
    }
)
class P_LRF_PSM_C_LRF_SetRangeType_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_rangeType: P_LRF_PSM.T_LRF_RangeType = P_LRF_PSM.T_LRF_RangeType.L_LRF_RangeType_MANUAL
    A_measuredRangeSeqNum: idl.int16 = 0
    A_rangeValue: float = 0.0

P_LRF_PSM.C_LRF_SetRangeType_Cmd = P_LRF_PSM_C_LRF_SetRangeType_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_LRF_PSM::C_LRF_SetMinimalRange_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_minimalRangeValue': [idl.id(216275746), ],
    }
)
class P_LRF_PSM_C_LRF_SetMinimalRange_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_minimalRangeValue: float = 0.0

P_LRF_PSM.C_LRF_SetMinimalRange_Cmd = P_LRF_PSM_C_LRF_SetMinimalRange_Cmd
