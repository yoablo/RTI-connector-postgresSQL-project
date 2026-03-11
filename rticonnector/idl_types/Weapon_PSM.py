
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Weapon_PSM.idl
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

P_Weapon_PSM = idl.get_module("P_Weapon_PSM")

P_Weapon_PSM_T_WeaponAmmunition = P_LDM_Common.T_ShortString

P_Weapon_PSM.T_WeaponAmmunition = P_Weapon_PSM_T_WeaponAmmunition

@idl.alias(
    annotations = [idl.bound(20),]
)
class P_Weapon_PSM_T_ListOfWeaponAmmunitions:
    value: Sequence[P_LDM_Common.T_ShortString] = field(default_factory = list)

P_Weapon_PSM.T_ListOfWeaponAmmunitions = P_Weapon_PSM_T_ListOfWeaponAmmunitions

@idl.enum
class P_Weapon_PSM_T_FireSemiCorrAction(IntEnum):
    L_FireSemiCorrAction_ADD = 0
    L_FireSemiCorrAction_REMOVE = 1
    L_FireSemiCorrAction_TARGET = 2
    L_FireSemiCorrAction_CANCEL_TARGET = 3
    L_FireSemiCorrAction_RIGHT = 4
    L_FireSemiCorrAction_LEFT = 5

P_Weapon_PSM.T_FireSemiCorrAction = P_Weapon_PSM_T_FireSemiCorrAction

@idl.enum
class P_Weapon_PSM_T_FireMode(IntEnum):
    L_FireMode_DIRECT = 0
    L_FireMode_STABILIZATION = 1

P_Weapon_PSM.T_FireMode = P_Weapon_PSM_T_FireMode

@idl.enum
class P_Weapon_PSM_T_FiringType(IntEnum):
    L_FiringType_SINGLE = 0
    L_FiringType_BURST = 1
    L_FiringType_FULL = 2

P_Weapon_PSM.T_FiringType = P_Weapon_PSM_T_FiringType

@idl.enum
class P_Weapon_PSM_T_CannonAppliancePosition(IntEnum):
    L_CannonAppliancePosition_NONE = 0
    L_CannonAppliancePosition_OBSERVATION = 1
    L_CannonAppliancePosition_SIGHT = 2
    L_CannonAppliancePosition_FIRE = 3

P_Weapon_PSM.T_CannonAppliancePosition = P_Weapon_PSM_T_CannonAppliancePosition

@idl.enum
class P_Weapon_PSM_T_RangeType(IntEnum):
    L_RangeType_MANUAL = 0
    L_RangeType_MEASURED = 1
    L_RangeType_BATTLE = 2
    L_RangeType_MINIMAL = 3
    L_RangeType_TRAVEL = 4

P_Weapon_PSM.T_RangeType = P_Weapon_PSM_T_RangeType

@idl.enum
class P_Weapon_PSM_T_CockingState(IntEnum):
    L_CockingState_OFF = 0
    L_CockingState_ON = 1
    L_CockingState_IN_PROGRESS = 2
    L_CockingState_FAULT = 3

P_Weapon_PSM.T_CockingState = P_Weapon_PSM_T_CockingState

@idl.enum
class P_Weapon_PSM_T_FCS_Mode(IntEnum):
    L_FCS_Mode_ON = 0
    L_FCS_Mode_UNIT_OFF_OPERATOR = 1
    L_FCS_Mode_UNIT_OFF_COMPUTING = 2
    L_FCS_Mode_MANUAL = 3

P_Weapon_PSM.T_FCS_Mode = P_Weapon_PSM_T_FCS_Mode

@idl.enum
class P_Weapon_PSM_T_FCS_Parameter(IntEnum):
    L_FCS_Parameter_WIND_SPEED = 0
    L_FCS_Parameter_HEIGHT = 1
    L_FCS_Parameter_AIR_TEMPERATURE = 2
    L_FCS_Parameter_GUN_POWDER_TEMPERATURE = 3
    L_FCS_Parameter_STATIC_COMPENSATION_ELEVATION = 4
    L_FCS_Parameter_STATIC_COMPENSATION_DEFLECTION = 5
    L_FCS_Parameter_RELATIVE_AZIMUTH = 6
    L_FCS_Parameter_ABSOLUTE_AZIMUTH = 7
    L_FCS_Parameter_DYNAMIC_COMPENSATION_ELEVATION = 8
    L_FCS_Parameter_DYNAMIC_COMPENSATION_DEFLECTION = 9
    L_FCS_Parameter_ENSLAVEMENT_ERROR_ELEVATION = 10
    L_FCS_Parameter_ENSLAVEMENT_ERROR_DEFLECTION = 11
    L_FCS_Parameter_MANUAL_RANGE = 12

P_Weapon_PSM.T_FCS_Parameter = P_Weapon_PSM_T_FCS_Parameter

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::T_LoaderAmmunitionState")],
    member_annotations = {
        'A_ammunitionName': [idl.id(267068887), ],
        'A_loaderSequenceNumber': [idl.id(236004433), ],
        'A_ammunitionCount': [idl.id(177769603), ],
    }
)
class P_Weapon_PSM_T_LoaderAmmunitionState:
    A_ammunitionName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_loaderSequenceNumber: idl.uint8 = 0
    A_ammunitionCount: idl.int32 = 0

P_Weapon_PSM.T_LoaderAmmunitionState = P_Weapon_PSM_T_LoaderAmmunitionState

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::T_Ammunition")],
    member_annotations = {
        'A_ammunitionName': [idl.id(267068887), ],
        'A_ammunitionCount': [idl.id(177769603), ],
    }
)
class P_Weapon_PSM_T_Ammunition:
    A_ammunitionName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_ammunitionCount: idl.int32 = 0

P_Weapon_PSM.T_Ammunition = P_Weapon_PSM_T_Ammunition

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::T_GunJumpValue")],
    member_annotations = {
        'A_traverseGunJump': [idl.id(66452456), ],
        'A_elevationGunJump': [idl.id(49503367), ],
    }
)
class P_Weapon_PSM_T_GunJumpValue:
    A_traverseGunJump: float = 0.0
    A_elevationGunJump: float = 0.0

P_Weapon_PSM.T_GunJumpValue = P_Weapon_PSM_T_GunJumpValue

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::T_BalisticCompensationValue")],
    member_annotations = {
        'A_traverse': [idl.id(39062148), ],
        'A_elevation': [idl.id(185059946), ],
        'A_traverseDynamic': [idl.id(85258101), ],
        'A_elevationDynamic': [idl.id(202955337), ],
    }
)
class P_Weapon_PSM_T_BalisticCompensationValue:
    A_traverse: float = 0.0
    A_elevation: float = 0.0
    A_traverseDynamic: float = 0.0
    A_elevationDynamic: float = 0.0

P_Weapon_PSM.T_BalisticCompensationValue = P_Weapon_PSM_T_BalisticCompensationValue

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::T_RangeMeasurement")],
    member_annotations = {
        'A_rangeValue': [idl.id(159489137), ],
        'A_rangeAccuracy': [idl.id(210806210), ],
        'A_sequenceNumber': [idl.id(232152101), ],
    }
)
class P_Weapon_PSM_T_RangeMeasurement:
    A_rangeValue: float = 0.0
    A_rangeAccuracy: float = 0.0
    A_sequenceNumber: idl.int16 = 0

P_Weapon_PSM.T_RangeMeasurement = P_Weapon_PSM_T_RangeMeasurement

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Weapon_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_caliber': [idl.id(268186056), ],
        'A_weaponName': [idl.id(86399886), ],
        'A_supportedAmmunitionList': [idl.id(71747423), ],
        'A_fireCorrectionSupport': [idl.id(213845062), ],
        'A_hotFireCorrectionSupport': [idl.id(113971641), ],
        'A_firingTypeSupport': [idl.id(148556402), idl.bound(3)],
        'A_burstLengthChangeSupport': [idl.id(60760835), ],
        'A_minBurstLength': [idl.id(50882846), ],
        'A_maxBurstLength': [idl.id(237299935), ],
        'A_loaderSupport': [idl.id(200744367), ],
        'A_fireInhibitZoneSupport': [idl.id(172484004), ],
        'A_balisticCompensationSupport': [idl.id(187502423), ],
    }
)
class P_Weapon_PSM_C_Weapon_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_caliber: float = 0.0
    A_weaponName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_supportedAmmunitionList: P_Weapon_PSM.T_ListOfWeaponAmmunitions = field(default_factory = P_Weapon_PSM.T_ListOfWeaponAmmunitions)
    A_fireCorrectionSupport: bool = False
    A_hotFireCorrectionSupport: bool = False
    A_firingTypeSupport: Sequence[P_Weapon_PSM.T_FiringType] = field(default_factory = list)
    A_burstLengthChangeSupport: bool = False
    A_minBurstLength: idl.int16 = 0
    A_maxBurstLength: idl.int16 = 0
    A_loaderSupport: bool = False
    A_fireInhibitZoneSupport: bool = False
    A_balisticCompensationSupport: bool = False

P_Weapon_PSM.C_Weapon_Specification = P_Weapon_PSM_C_Weapon_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Weapon_Loader_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_numberOfLoaders': [idl.id(49667620), ],
    }
)
class P_Weapon_PSM_C_Weapon_Loader_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_numberOfLoaders: idl.uint8 = 0

P_Weapon_PSM.C_Weapon_Loader_Specification = P_Weapon_PSM_C_Weapon_Loader_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Weapon")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_currentAmmunition': [idl.id(45786869), ],
        'A_currentFiringType': [idl.id(13379310), ],
        'A_burstLength': [idl.id(83906516), ],
        'A_isInFireInhibitZone': [idl.id(260738525), ],
        'A_cockingState': [idl.id(58372020), ],
        'A_lowAmmoState': [idl.id(13960035), ],
    }
)
class P_Weapon_PSM_C_Weapon:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_currentAmmunition: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_currentFiringType: P_Weapon_PSM.T_FiringType = P_Weapon_PSM.T_FiringType.L_FiringType_SINGLE
    A_burstLength: idl.uint8 = 0
    A_isInFireInhibitZone: bool = False
    A_cockingState: P_Weapon_PSM.T_CockingState = P_Weapon_PSM.T_CockingState.L_CockingState_OFF
    A_lowAmmoState: bool = False

P_Weapon_PSM.C_Weapon = P_Weapon_PSM_C_Weapon

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_FireSemiCorrection")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_elevationValue': [idl.id(219992818), ],
        'A_traverseValue': [idl.id(134318796), ],
        'A_lastIndication': [idl.id(72679071), ],
    }
)
class P_Weapon_PSM_C_FireSemiCorrection:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_elevationValue: idl.int16 = 0
    A_traverseValue: idl.int16 = 0
    A_lastIndication: P_Weapon_PSM.T_FireSemiCorrAction = P_Weapon_PSM.T_FireSemiCorrAction.L_FireSemiCorrAction_ADD

P_Weapon_PSM.C_FireSemiCorrection = P_Weapon_PSM_C_FireSemiCorrection

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_FireHotCorrection")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_azimuthHotCorrection': [idl.id(129341050), ],
        'A_elevationHotCorrection': [idl.id(146539350), ],
    }
)
class P_Weapon_PSM_C_FireHotCorrection:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_azimuthHotCorrection: float = 0.0
    A_elevationHotCorrection: float = 0.0

P_Weapon_PSM.C_FireHotCorrection = P_Weapon_PSM_C_FireHotCorrection

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Fire_Event")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fireMode': [idl.id(102907917), ],
        'A_fireType': [idl.id(89284970), ],
        'A_fireInitiatorDescriptor': [idl.id(176845168), ],
        'A_currentAmmunition': [idl.id(45786869), ],
        'A_fireLocationAvailable': [idl.id(240129194), ],
        'A_fireLocation': [idl.id(38796174), ],
    }
)
class P_Weapon_PSM_C_Fire_Event:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fireMode: P_Weapon_PSM.T_FireMode = P_Weapon_PSM.T_FireMode.L_FireMode_DIRECT
    A_fireType: bool = False
    A_fireInitiatorDescriptor: P_LDM_Common.T_VeryShortString = field(default_factory = P_LDM_Common.T_VeryShortString)
    A_currentAmmunition: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_fireLocationAvailable: bool = False
    A_fireLocation: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Weapon_PSM.C_Fire_Event = P_Weapon_PSM_C_Fire_Event

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Weapon_Loaders")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_currentAmmunition': [idl.id(45786869), idl.bound(20)],
        'A_currentLoader': [idl.id(86413533), ],
    }
)
class P_Weapon_PSM_C_Weapon_Loaders:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_currentAmmunition: Sequence[P_Weapon_PSM.T_LoaderAmmunitionState] = field(default_factory = list)
    A_currentLoader: idl.uint8 = 0

P_Weapon_PSM.C_Weapon_Loaders = P_Weapon_PSM_C_Weapon_Loaders

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Balistic_Parameters")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_gunPowderTemperature': [idl.id(229963660), ],
        'A_gunPowderTemperatureSource': [idl.id(217480135), ],
        'A_gunJump': [idl.id(56281219), ],
        'A_balisticCompensation': [idl.id(240577419), ],
    }
)
class P_Weapon_PSM_C_Balistic_Parameters:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_gunPowderTemperature: float = 0.0
    A_gunPowderTemperatureSource: P_LDM_Common.T_Value_Source = P_LDM_Common.T_Value_Source.L_Value_Source_UNKNOWN
    A_gunJump: P_Weapon_PSM.T_GunJumpValue = field(default_factory = P_Weapon_PSM.T_GunJumpValue)
    A_balisticCompensation: P_Weapon_PSM.T_BalisticCompensationValue = field(default_factory = P_Weapon_PSM.T_BalisticCompensationValue)

P_Weapon_PSM.C_Balistic_Parameters = P_Weapon_PSM_C_Balistic_Parameters

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Ramp_Position")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_postion': [idl.id(83459906), ],
        'A_isContinues': [idl.id(245253684), ],
    }
)
class P_Weapon_PSM_C_Ramp_Position:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_postion: P_Weapon_PSM.T_CannonAppliancePosition = P_Weapon_PSM.T_CannonAppliancePosition.L_CannonAppliancePosition_NONE
    A_isContinues: bool = False

P_Weapon_PSM.C_Ramp_Position = P_Weapon_PSM_C_Ramp_Position

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_AmmunitionList")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_list': [idl.id(43447639), idl.bound(20)],
    }
)
class P_Weapon_PSM_C_AmmunitionList:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_list: Sequence[P_Weapon_PSM.T_Ammunition] = field(default_factory = list)

P_Weapon_PSM.C_AmmunitionList = P_Weapon_PSM_C_AmmunitionList

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Fire_Series")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fireEventInSeries': [idl.id(113931363), ],
        'A_seriesStartTime': [idl.id(13950453), ],
        'A_seriesEndTime': [idl.id(216311584), ],
        'A_seriesAmmunition': [idl.id(262411396), ],
        'A_seriesRangeType': [idl.id(43876912), ],
        'A_seriesRange': [idl.id(119823897), ],
        'A_seriesAirTemperature': [idl.id(136679608), ],
        'A_seriesGunPowderTemperature': [idl.id(102962035), ],
        'A_seriesHeight': [idl.id(208633532), ],
        'A_seriesGunJumpValue': [idl.id(32597079), ],
        'A_seriesLearningValue': [idl.id(121558912), ],
        'A_accumulatedLearningValue': [idl.id(96934584), ],
        'A_endSeriesReason': [idl.id(21744586), ],
        'A_nonLearningReason': [idl.id(75932247), ],
    }
)
class P_Weapon_PSM_C_Fire_Series:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fireEventInSeries: idl.int16 = 0
    A_seriesStartTime: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_seriesEndTime: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_seriesAmmunition: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_seriesRangeType: P_Weapon_PSM.T_RangeType = P_Weapon_PSM.T_RangeType.L_RangeType_MANUAL
    A_seriesRange: P_Weapon_PSM.T_RangeMeasurement = field(default_factory = P_Weapon_PSM.T_RangeMeasurement)
    A_seriesAirTemperature: float = 0.0
    A_seriesGunPowderTemperature: float = 0.0
    A_seriesHeight: float = 0.0
    A_seriesGunJumpValue: P_Weapon_PSM.T_GunJumpValue = field(default_factory = P_Weapon_PSM.T_GunJumpValue)
    A_seriesLearningValue: float = 0.0
    A_accumulatedLearningValue: float = 0.0
    A_endSeriesReason: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_nonLearningReason: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Weapon_PSM.C_Fire_Series = P_Weapon_PSM_C_Fire_Series

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_FireEvent_Shell")],
    member_annotations = {
        'A_movementState': [idl.id(248034516), ],
        'A_platformSpeed': [idl.id(78673287), ],
        'A_sightEnslavement': [idl.id(220551691), ],
        'A_trackState': [idl.id(115701259), ],
        'A_trackID': [idl.id(188094313), ],
        'A_isGunnerTouch': [idl.id(98862323), ],
        'A_isCommanderTouch': [idl.id(180300358), ],
        'A_elevationSemiCorrection': [idl.id(127370406), ],
        'A_traverseSemiCorrection': [idl.id(44615645), ],
        'A_sideWindVelocity': [idl.id(197342223), ],
        'A_elevationDynamicCompensation': [idl.id(56567334), ],
        'A_deflectionDynamicCompensation': [idl.id(103337218), ],
        'A_absoluteAzimuth': [idl.id(173265625), ],
        'A_attitude': [idl.id(231526761), ],
        'A_shellNumberInSeries': [idl.id(33648210), ],
        'A_gunResolver': [idl.id(63748537), ],
        'A_deflectionEnslavementError': [idl.id(56926495), ],
        'A_elevationEnslavementError': [idl.id(16352289), ],
    }
)
class P_Weapon_PSM_C_FireEvent_Shell(P_Weapon_PSM.C_Fire_Event):
    A_movementState: bool = False
    A_platformSpeed: float = 0.0
    A_sightEnslavement: P_LDM_Common.T_SightEnslavement_Mode = P_LDM_Common.T_SightEnslavement_Mode.L_SightEnslavement_Mode_IDLE
    A_trackState: bool = False
    A_trackID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_isGunnerTouch: bool = False
    A_isCommanderTouch: bool = False
    A_elevationSemiCorrection: idl.int16 = 0
    A_traverseSemiCorrection: idl.int16 = 0
    A_sideWindVelocity: P_LDM_Common.T_Vector_3D = field(default_factory = P_LDM_Common.T_Vector_3D)
    A_elevationDynamicCompensation: float = 0.0
    A_deflectionDynamicCompensation: float = 0.0
    A_absoluteAzimuth: float = 0.0
    A_attitude: P_LDM_Common.T_Attitude = field(default_factory = P_LDM_Common.T_Attitude)
    A_shellNumberInSeries: idl.int16 = 0
    A_gunResolver: float = 0.0
    A_deflectionEnslavementError: float = 0.0
    A_elevationEnslavementError: float = 0.0

P_Weapon_PSM.C_FireEvent_Shell = P_Weapon_PSM_C_FireEvent_Shell

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_FireSemiCorrection_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_requestedCorrection': [idl.id(219208497), ],
    }
)
class P_Weapon_PSM_C_FireSemiCorrection_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_requestedCorrection: P_Weapon_PSM.T_FireSemiCorrAction = P_Weapon_PSM.T_FireSemiCorrAction.L_FireSemiCorrAction_ADD

P_Weapon_PSM.C_FireSemiCorrection_Cmd = P_Weapon_PSM_C_FireSemiCorrection_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_FireHotCorrection_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_azimuthHotCorrection': [idl.id(129341050), ],
        'A_elevationHotCorrection': [idl.id(146539350), ],
    }
)
class P_Weapon_PSM_C_FireHotCorrection_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_azimuthHotCorrection: float = 0.0
    A_elevationHotCorrection: float = 0.0

P_Weapon_PSM.C_FireHotCorrection_Cmd = P_Weapon_PSM_C_FireHotCorrection_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_SetAmmunition_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_requestedAmmunition': [idl.id(229210782), ],
        'A_requestedLoader': [idl.id(213927640), ],
        'A_loaderSequenceNumber': [idl.id(236004433), ],
        'A_requestedBurstLength': [idl.id(255252827), ],
    }
)
class P_Weapon_PSM_C_SetAmmunition_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_requestedAmmunition: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_requestedLoader: idl.uint8 = 0
    A_loaderSequenceNumber: idl.uint8 = 0
    A_requestedBurstLength: idl.uint8 = 0

P_Weapon_PSM.C_SetAmmunition_Cmd = P_Weapon_PSM_C_SetAmmunition_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_SetAmmunitionList_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_supportedAmmunitionsList': [idl.id(189499306), ],
    }
)
class P_Weapon_PSM_C_SetAmmunitionList_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_supportedAmmunitionsList: P_Weapon_PSM.T_ListOfWeaponAmmunitions = field(default_factory = P_Weapon_PSM.T_ListOfWeaponAmmunitions)

P_Weapon_PSM.C_SetAmmunitionList_Cmd = P_Weapon_PSM_C_SetAmmunitionList_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Firing_Type_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_firingType': [idl.id(117405101), ],
    }
)
class P_Weapon_PSM_C_Set_Firing_Type_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_firingType: P_Weapon_PSM.T_FiringType = P_Weapon_PSM.T_FiringType.L_FiringType_SINGLE

P_Weapon_PSM.C_Set_Firing_Type_Cmd = P_Weapon_PSM_C_Set_Firing_Type_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Burst_Length_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_burstLength': [idl.id(83906516), ],
        'A_ammunitionType': [idl.id(90539466), ],
    }
)
class P_Weapon_PSM_C_Set_Burst_Length_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_burstLength: idl.uint8 = 0
    A_ammunitionType: Optional[P_LDM_Common.T_ShortString] = None

P_Weapon_PSM.C_Set_Burst_Length_Cmd = P_Weapon_PSM_C_Set_Burst_Length_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Projectiles_Rate_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_firingRate': [idl.id(172123202), ],
    }
)
class P_Weapon_PSM_C_Set_Projectiles_Rate_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_firingRate: idl.int32 = 0

P_Weapon_PSM.C_Set_Projectiles_Rate_Cmd = P_Weapon_PSM_C_Set_Projectiles_Rate_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Ammunition_Loader_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_loaderAmmunition': [idl.id(183137645), ],
    }
)
class P_Weapon_PSM_C_Set_Ammunition_Loader_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_loaderAmmunition: P_Weapon_PSM.T_LoaderAmmunitionState = field(default_factory = P_Weapon_PSM.T_LoaderAmmunitionState)

P_Weapon_PSM.C_Set_Ammunition_Loader_Cmd = P_Weapon_PSM_C_Set_Ammunition_Loader_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Balistic_Parameters_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_powderTemperature': [idl.id(7743644), ],
        'A_vicinityTemperature': [idl.id(209766739), ],
        'A_humidity': [idl.id(40463860), ],
        'A_airPressure': [idl.id(157462497), ],
        'A_windSpeed': [idl.id(219447323), ],
        'A_windDirection': [idl.id(25861558), ],
    }
)
class P_Weapon_PSM_C_Set_Balistic_Parameters_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_powderTemperature: float = 0.0
    A_vicinityTemperature: float = 0.0
    A_humidity: float = 0.0
    A_airPressure: float = 0.0
    A_windSpeed: float = 0.0
    A_windDirection: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)

P_Weapon_PSM.C_Set_Balistic_Parameters_Cmd = P_Weapon_PSM_C_Set_Balistic_Parameters_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_GunJump_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_jump': [idl.id(199641731), ],
    }
)
class P_Weapon_PSM_C_Set_GunJump_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_jump: P_Weapon_PSM.T_GunJumpValue = field(default_factory = P_Weapon_PSM.T_GunJumpValue)

P_Weapon_PSM.C_Set_GunJump_Cmd = P_Weapon_PSM_C_Set_GunJump_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Ballistic_Compensation_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_compensation': [idl.id(169601750), ],
    }
)
class P_Weapon_PSM_C_Set_Ballistic_Compensation_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_compensation: P_Weapon_PSM.T_BalisticCompensationValue = field(default_factory = P_Weapon_PSM.T_BalisticCompensationValue)

P_Weapon_PSM.C_Set_Ballistic_Compensation_Cmd = P_Weapon_PSM_C_Set_Ballistic_Compensation_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Weapon_Base_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_responseNotRequired': [idl.id(193715237), ],
    }
)
class P_Weapon_PSM_C_Weapon_Base_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_responseNotRequired: bool = False

P_Weapon_PSM.C_Weapon_Base_Cmd = P_Weapon_PSM_C_Weapon_Base_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Enter_Ramp_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_rampEntering': [idl.id(236224408), ],
        'A_continuesPosition': [idl.id(8014668), ],
    }
)
class P_Weapon_PSM_C_Enter_Ramp_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_rampEntering: bool = False
    A_continuesPosition: bool = False

P_Weapon_PSM.C_Enter_Ramp_Cmd = P_Weapon_PSM_C_Enter_Ramp_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_Ammuntion_List_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_weaponAmmunition': [idl.id(17151301), idl.bound(20)],
    }
)
class P_Weapon_PSM_C_Set_Ammuntion_List_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_weaponAmmunition: Sequence[P_Weapon_PSM.T_Ammunition] = field(default_factory = list)

P_Weapon_PSM.C_Set_Ammuntion_List_Cmd = P_Weapon_PSM_C_Set_Ammuntion_List_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Weapon_PSM::C_Set_FCS_Computing_Mode_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fcsMode': [idl.id(67890095), ],
        'A_parameterType': [idl.id(60175090), ],
        'A_parameterValue': [idl.id(52495252), ],
    }
)
class P_Weapon_PSM_C_Set_FCS_Computing_Mode_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fcsMode: P_Weapon_PSM.T_FCS_Mode = P_Weapon_PSM.T_FCS_Mode.L_FCS_Mode_ON
    A_parameterType: P_Weapon_PSM.T_FCS_Parameter = P_Weapon_PSM.T_FCS_Parameter.L_FCS_Parameter_WIND_SPEED
    A_parameterValue: idl.float32 = 0.0

P_Weapon_PSM.C_Set_FCS_Computing_Mode_Cmd = P_Weapon_PSM_C_Set_FCS_Computing_Mode_Cmd
