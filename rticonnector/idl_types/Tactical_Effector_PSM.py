
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Tactical_Effector_PSM.idl
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

P_Tactical_Effector_PSM = idl.get_module("P_Tactical_Effector_PSM")

@idl.enum
class P_Tactical_Effector_PSM_T_FireState(IntEnum):
    L_FireState_BLOCKED = 0
    L_FireState_ENABLED = 1
    L_FireState_READY = 2
    L_FireState_FAULT = 3

P_Tactical_Effector_PSM.T_FireState = P_Tactical_Effector_PSM_T_FireState

@idl.enum
class P_Tactical_Effector_PSM_T_ControlSource(IntEnum):
    L_ControlSource_DEFAULT = 0
    L_ControlSource_SYSTEM = 1
    L_ControlSource_EXTERNAL = 2
    L_ControlSource_COMMANDER = 3
    L_ControlSource_GUNNER = 4

P_Tactical_Effector_PSM.T_ControlSource = P_Tactical_Effector_PSM_T_ControlSource

@idl.enum
class P_Tactical_Effector_PSM_T_FizOverrideState(IntEnum):
    L_FizOverrideState_DISABLED = 0
    L_FizOverrideState_ACTIVE = 1
    L_FizOverrideState_WAITING = 2

P_Tactical_Effector_PSM.T_FizOverrideState = P_Tactical_Effector_PSM_T_FizOverrideState

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_weaponsSupport': [idl.id(193894160), idl.bound(16)],
        'A_enablingSupport': [idl.id(260599573), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_weaponsSupport: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_enablingSupport: bool = False

P_Tactical_Effector_PSM.C_Tactical_Effector_Specification = P_Tactical_Effector_PSM_C_Tactical_Effector_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_currentSelectedWeapon': [idl.id(56374483), ],
        'A_fireState': [idl.id(11552111), ],
        'A_isReadyForFire': [idl.id(102966574), ],
        'A_isInFireInhibitZone': [idl.id(260738525), ],
        'A_isFiring': [idl.id(175345569), ],
        'A_controlOwner': [idl.id(159739203), ],
        'A_sytemCurrentRange': [idl.id(242107216), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_currentSelectedWeapon: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_fireState: P_Tactical_Effector_PSM.T_FireState = P_Tactical_Effector_PSM.T_FireState.L_FireState_BLOCKED
    A_isReadyForFire: bool = False
    A_isInFireInhibitZone: bool = False
    A_isFiring: bool = False
    A_controlOwner: P_Tactical_Effector_PSM.T_ControlSource = P_Tactical_Effector_PSM.T_ControlSource.L_ControlSource_DEFAULT
    A_sytemCurrentRange: Optional[float] = None

P_Tactical_Effector_PSM.C_Tactical_Effector = P_Tactical_Effector_PSM_C_Tactical_Effector

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector_Control_Readiness")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_ready': [idl.id(74546749), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector_Control_Readiness:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_ready: bool = False

P_Tactical_Effector_PSM.C_Tactical_Effector_Control_Readiness = P_Tactical_Effector_PSM_C_Tactical_Effector_Control_Readiness

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Fiz_Override")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_overrideEngaged': [idl.id(82224944), ],
    }
)
class P_Tactical_Effector_PSM_C_Fiz_Override:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_overrideEngaged: P_Tactical_Effector_PSM.T_FizOverrideState = P_Tactical_Effector_PSM.T_FizOverrideState.L_FizOverrideState_DISABLED

P_Tactical_Effector_PSM.C_Fiz_Override = P_Tactical_Effector_PSM_C_Fiz_Override

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector_Enable_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector_Enable_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Tactical_Effector_Enable_Cmd = P_Tactical_Effector_PSM_C_Tactical_Effector_Enable_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector_Disable_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector_Disable_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Tactical_Effector_Disable_Cmd = P_Tactical_Effector_PSM_C_Tactical_Effector_Disable_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector_Select_Weapon_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_selectedWeapon': [idl.id(189404346), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector_Select_Weapon_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_selectedWeapon: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Tactical_Effector_PSM.C_Tactical_Effector_Select_Weapon_Cmd = P_Tactical_Effector_PSM_C_Tactical_Effector_Select_Weapon_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Tactical_Effector_Set_Control_Owner_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_controlOwner': [idl.id(159739203), ],
    }
)
class P_Tactical_Effector_PSM_C_Tactical_Effector_Set_Control_Owner_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_controlOwner: P_Tactical_Effector_PSM.T_ControlSource = P_Tactical_Effector_PSM.T_ControlSource.L_ControlSource_DEFAULT

P_Tactical_Effector_PSM.C_Tactical_Effector_Set_Control_Owner_Cmd = P_Tactical_Effector_PSM_C_Tactical_Effector_Set_Control_Owner_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Fiz_Override_Request_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Fiz_Override_Request_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Fiz_Override_Request_Cmd = P_Tactical_Effector_PSM_C_Fiz_Override_Request_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Fiz_Override_Approve_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Fiz_Override_Approve_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Fiz_Override_Approve_Cmd = P_Tactical_Effector_PSM_C_Fiz_Override_Approve_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Fiz_Override_Reject_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Fiz_Override_Reject_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Fiz_Override_Reject_Cmd = P_Tactical_Effector_PSM_C_Fiz_Override_Reject_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Control_Readiness_Enable_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Control_Readiness_Enable_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Control_Readiness_Enable_Cmd = P_Tactical_Effector_PSM_C_Control_Readiness_Enable_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Effector_PSM::C_Control_Readiness_Disable_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Tactical_Effector_PSM_C_Control_Readiness_Disable_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Effector_PSM.C_Control_Readiness_Disable_Cmd = P_Tactical_Effector_PSM_C_Control_Readiness_Disable_Cmd
