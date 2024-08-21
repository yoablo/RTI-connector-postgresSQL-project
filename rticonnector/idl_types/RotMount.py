# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from RotMount.idl
# using RTI Code Generator (rtiddsgen) version 4.3.0.
# The rtiddsgen tool is part of the RTI Connext DDS distribution.
# For more information, type 'rtiddsgen -help' at a command shell
# or consult the Code Generator User's Manual.

from dataclasses import field
import rti.idl as idl
from enum import IntEnum

from rticonnector.idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet

P_LDM_Common = P_LDM_Common_Objet
P_Mount_PSM = idl.get_module("P_Mount_PSM")


@idl.enum
class P_Mount_PSM_T_ProcessState(IntEnum):
    L_ProcessState_OFF = 0
    L_ProcessState_IN_PROGRESS = 1
    L_ProcessState_COMPLETED = 2
    L_ProcessState_FAILED = 3


P_Mount_PSM.T_ProcessState = P_Mount_PSM_T_ProcessState


@idl.enum
class P_Mount_PSM_T_EnslavementMode(IntEnum):
    L_EnslavementMode_INDEPENDENT = 0
    L_EnslavementMode_ENSLAVED = 1
    L_EnslavementMode_MECHANICAL = 2


P_Mount_PSM.T_EnslavementMode = P_Mount_PSM_T_EnslavementMode


@idl.enum
class P_Mount_PSM_T_MountWorkMode(IntEnum):
    L_MountWorkMode_INIT = 0
    L_MountWorkMode_OPER = 1
    L_MountWorkMode_MAINT = 2


P_Mount_PSM.T_MountWorkMode = P_Mount_PSM_T_MountWorkMode


@idl.enum
class P_LDM_Common_T_OnOff(IntEnum):
    L_OnOff_ON = 0
    L_OnOff_OFF = 1


P_LDM_Common.T_OnOff = P_LDM_Common_T_OnOff

@idl.enum
class P_Mount_PSM_T_StabilizationMode(IntEnum):
    L_StabilizationMode_MANUAL = 0
    L_StabilizationMode_POWER = 1
    L_StabilizationMode_STABILIZATION = 2


P_Mount_PSM.T_StabilizationMode = P_Mount_PSM_T_StabilizationMode

P_LDM_Common = idl.get_module("P_LDM_Common")


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Mount_PSM::C_Rot_Mount")],
    member_annotations={
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
    }
)
class P_Mount_PSM_C_Rot_Mount:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_mountPosition: P_LDM_Common.T_RotationalPosition = field(default_factory=P_LDM_Common.T_RotationalPosition)
    A_absolutePosition: P_LDM_Common.T_Coordinate3D = field(default_factory=P_LDM_Common.T_Coordinate3D)
    A_attitudeToNorthPosition: float = 0.0
    A_scanState: P_Mount_PSM.T_ProcessState = P_Mount_PSM.T_ProcessState.L_ProcessState_OFF
    A_bringToState: P_Mount_PSM.T_ProcessState = P_Mount_PSM.T_ProcessState.L_ProcessState_OFF
    A_bringToPreset: P_LDM_Common.T_RotationalPosition = field(default_factory=P_LDM_Common.T_RotationalPosition)
    A_enslavementMode: P_Mount_PSM.T_EnslavementMode = P_Mount_PSM.T_EnslavementMode.L_EnslavementMode_INDEPENDENT
    A_enslavedTo: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_workMode: P_Mount_PSM.T_MountWorkMode = P_Mount_PSM.T_MountWorkMode.L_MountWorkMode_INIT
    A_lmcState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_stabilizationState: P_Mount_PSM.T_StabilizationMode = P_Mount_PSM.T_StabilizationMode.L_StabilizationMode_MANUAL
    A_inMovementInhibitZone: bool = False
    A_traverseMode: bool = False


P_Mount_PSM.C_Rot_Mount = P_Mount_PSM_C_Rot_Mount
