
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from VideoTracking_PSM.idl
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

P_VideoTracking_PSM = idl.get_module("P_VideoTracking_PSM")

@idl.enum
class P_VideoTracking_PSM_T_Video_Tracker_State(IntEnum):
    L_Video_Tracker_State_OFF = 0
    L_Video_Tracker_State_ON_TARGET = 1
    L_Video_Tracker_State_TMR = 2

P_VideoTracking_PSM.T_Video_Tracker_State = P_VideoTracking_PSM_T_Video_Tracker_State

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_VideoTracking_PSM::C_Video_Tracker_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_maxTrackableObjects': [idl.id(104898683), ],
        'A_trackableVideoStreamsIds': [idl.id(176240182), idl.bound(32)],
    }
)
class P_VideoTracking_PSM_C_Video_Tracker_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_maxTrackableObjects: idl.int32 = 0
    A_trackableVideoStreamsIds: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)

P_VideoTracking_PSM.C_Video_Tracker_Specification = P_VideoTracking_PSM_C_Video_Tracker_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_VideoTracking_PSM::C_Video_Tracker")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_videoTrackerState': [idl.id(233903997), ],
        'A_trackedVideoStreamId': [idl.id(21434138), ],
        'A_mountId': [idl.id(35863804), ],
    }
)
class P_VideoTracking_PSM_C_Video_Tracker:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_videoTrackerState: P_VideoTracking_PSM.T_Video_Tracker_State = P_VideoTracking_PSM.T_Video_Tracker_State.L_Video_Tracker_State_OFF
    A_trackedVideoStreamId: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_mountId: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_VideoTracking_PSM.C_Video_Tracker = P_VideoTracking_PSM_C_Video_Tracker

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_VideoTracking_PSM::C_Video_Tracker_StartLeadOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_trackVideoStreamId': [idl.id(186125975), ],
    }
)
class P_VideoTracking_PSM_C_Video_Tracker_StartLeadOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_trackVideoStreamId: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_VideoTracking_PSM.C_Video_Tracker_StartLeadOn_Cmd = P_VideoTracking_PSM_C_Video_Tracker_StartLeadOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_VideoTracking_PSM::C_Video_Tracker_StopLeadOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_VideoTracking_PSM_C_Video_Tracker_StopLeadOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_VideoTracking_PSM.C_Video_Tracker_StopLeadOn_Cmd = P_VideoTracking_PSM_C_Video_Tracker_StopLeadOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_VideoTracking_PSM::C_Video_Tracker_SetMountId_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_id': [idl.id(247462910), ],
    }
)
class P_VideoTracking_PSM_C_Video_Tracker_SetMountId_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_id: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_VideoTracking_PSM.C_Video_Tracker_SetMountId_Cmd = P_VideoTracking_PSM_C_Video_Tracker_SetMountId_Cmd
