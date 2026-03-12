
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Navigation_PSM.idl
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

P_Navigation_PSM = idl.get_module("P_Navigation_PSM")

@idl.enum
class P_Navigation_PSM_T_HeadingRefDatum(IntEnum):
    L_HeadingRefDatum_MAGNETIC = 0
    L_HeadingRefDatum_TRUE = 1
    L_HeadingRefDatum_GRID = 2

P_Navigation_PSM.T_HeadingRefDatum = P_Navigation_PSM_T_HeadingRefDatum

@idl.enum
class P_Navigation_PSM_T_GpsKeyStatus(IntEnum):
    L_GpsKeyStatus_KEY_REQUIRED = 0
    L_GpsKeyStatus_INVALID_KEY = 1
    L_GpsKeyStatus_KEY_ACCEPTED = 2
    L_GpsKeyStatus_NO_ACTION = 3

P_Navigation_PSM.T_GpsKeyStatus = P_Navigation_PSM_T_GpsKeyStatus

@idl.enum
class P_Navigation_PSM_T_ModeState(IntEnum):
    L_ModeState_INITIALIZING = 0
    L_ModeState_GYRO_COMPASS_NOT_READY = 1
    L_ModeState_GYRO_COMPASS_DEGRADED = 2
    L_ModeState_GYRO_COMPASS_FULL = 3
    L_ModeState_NAV_MODE = 4
    L_ModeState_INS_OFF = 5

P_Navigation_PSM.T_ModeState = P_Navigation_PSM_T_ModeState

@idl.enum
class P_Navigation_PSM_T_Uncertainty(IntEnum):
    L_Uncertainty_GDOP = 0
    L_Uncertainty_FOM = 1
    L_Uncertainty_CEP = 2
    L_Uncertainty_ERROR = 3
    L_Uncertainty_NONE = 4

P_Navigation_PSM.T_Uncertainty = P_Navigation_PSM_T_Uncertainty

@idl.enum
class P_Navigation_PSM_T_NavResource(IntEnum):
    L_NavResource_COMPASS_ONLY = 0
    L_NavResource_GPS_ONLY = 1
    L_NavResource_KEY_GPS_ONLY = 2
    L_NavResource_INS_ONLY = 3
    L_NavResource_GPS_AIDED_INS = 4
    L_NavResource_KEY_GPS_AIDED_INS = 5

P_Navigation_PSM.T_NavResource = P_Navigation_PSM_T_NavResource

@idl.enum
class P_Navigation_PSM_T_AlignMode(IntEnum):
    L_AlignMode_NORMAL_ALIGN = 0
    L_AlignMode_SH_ALIGN = 1
    L_AlignMode_ON_MOVE_ALIGN = 2

P_Navigation_PSM.T_AlignMode = P_Navigation_PSM_T_AlignMode

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Navigation_Resource")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_resourceType': [idl.id(190888830), ],
        'A_northReference': [idl.id(33375872), ],
        'A_dataOutputRate': [idl.id(48002361), ],
        'A_zuptMode': [idl.id(140713441), ],
        'A_utc': [idl.id(39408754), ],
        'A_magneticVariation': [idl.id(123328125), ],
        'A_gridConvergence': [idl.id(5769172), ],
        'A_resourceInputSourceID': [idl.id(31052640), idl.bound(3)],
        'A_motionLimitSourceID': [idl.id(14569655), ],
        'A_specificationSourceID': [idl.id(221192984), ],
        'A_selectedDatumSourceID': [idl.id(139296669), ],
        'A_angularMotionSourceID': [idl.id(232299024), idl.bound(3)],
        'A_attitudeSourceID': [idl.id(164831132), ],
        'A_headingSourceID': [idl.id(43547783), ],
        'A_linearMotionSourceID': [idl.id(53792137), idl.bound(3)],
        'A_frameVelocitySourceID': [idl.id(91957894), ],
        'A_positionSourceID': [idl.id(197463906), ],
    }
)
class P_Navigation_PSM_C_Navigation_Resource:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_resourceType: P_Navigation_PSM.T_NavResource = P_Navigation_PSM.T_NavResource.L_NavResource_COMPASS_ONLY
    A_northReference: P_Navigation_PSM.T_HeadingRefDatum = P_Navigation_PSM.T_HeadingRefDatum.L_HeadingRefDatum_MAGNETIC
    A_dataOutputRate: float = 0.0
    A_zuptMode: bool = False
    A_utc: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_magneticVariation: float = 0.0
    A_gridConvergence: float = 0.0
    A_resourceInputSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_motionLimitSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_specificationSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_selectedDatumSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_angularMotionSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_attitudeSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_headingSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_linearMotionSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_frameVelocitySourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_positionSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Navigation_PSM.C_Navigation_Resource = P_Navigation_PSM_C_Navigation_Resource

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_GPS_Receiver")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_gpsKeyStatus': [idl.id(75924950), ],
        'A_gpsReady': [idl.id(110705517), ],
        'A_gpsInitFail': [idl.id(127913799), ],
        'A_spoofersDetected': [idl.id(203118883), ],
        'A_positionError': [idl.id(174661909), ],
        'A_gpsCriticalFailure': [idl.id(7769737), ],
        'A_numberOfSatellites': [idl.id(47576042), ],
        'A_figureOfMerit': [idl.id(47361394), ],
    }
)
class P_Navigation_PSM_C_GPS_Receiver:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_gpsKeyStatus: P_Navigation_PSM.T_GpsKeyStatus = P_Navigation_PSM.T_GpsKeyStatus.L_GpsKeyStatus_KEY_REQUIRED
    A_gpsReady: bool = False
    A_gpsInitFail: bool = False
    A_spoofersDetected: bool = False
    A_positionError: float = 0.0
    A_gpsCriticalFailure: bool = False
    A_numberOfSatellites: idl.int16 = 0
    A_figureOfMerit: idl.float32 = 0.0

P_Navigation_PSM.C_GPS_Receiver = P_Navigation_PSM_C_GPS_Receiver

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Inertial_Nav_System")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_alignTimeToGo': [idl.id(205760253), ],
        'A_positionRequest': [idl.id(142561419), ],
        'A_positionFixReceived': [idl.id(187661184), ],
        'A_positionFixAccepted': [idl.id(23830193), ],
        'A_zuptRequest': [idl.id(186245124), ],
        'A_insCriticalFailure': [idl.id(250149265), ],
        'A_odometerNotCompatible': [idl.id(42296514), ],
        'A_positionError': [idl.id(174661909), ],
        'A_insTimeToReadiness': [idl.id(196783252), ],
        'A_insModeStatus': [idl.id(204655139), ],
    }
)
class P_Navigation_PSM_C_Inertial_Nav_System:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_alignTimeToGo: P_LDM_Common.T_Duration = field(default_factory = P_LDM_Common.T_Duration)
    A_positionRequest: bool = False
    A_positionFixReceived: bool = False
    A_positionFixAccepted: bool = False
    A_zuptRequest: bool = False
    A_insCriticalFailure: bool = False
    A_odometerNotCompatible: bool = False
    A_positionError: float = 0.0
    A_insTimeToReadiness: P_LDM_Common.T_Duration = field(default_factory = P_LDM_Common.T_Duration)
    A_insModeStatus: P_Navigation_PSM.T_ModeState = P_Navigation_PSM.T_ModeState.L_ModeState_INITIALIZING

P_Navigation_PSM.C_Inertial_Nav_System = P_Navigation_PSM_C_Inertial_Nav_System

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Magnetometer")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Navigation_PSM_C_Magnetometer:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Navigation_PSM.C_Magnetometer = P_Navigation_PSM_C_Magnetometer

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Odometer")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_distanceTravelled': [idl.id(254202973), ],
    }
)
class P_Navigation_PSM_C_Odometer:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_distanceTravelled: float = 0.0

P_Navigation_PSM.C_Odometer = P_Navigation_PSM_C_Odometer

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Position")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_currentPosition': [idl.id(139922608), ],
    }
)
class P_Navigation_PSM_C_Position:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_currentPosition: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Navigation_PSM.C_Position = P_Navigation_PSM_C_Position

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Heading")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_sensorHeading': [idl.id(223596635), ],
        'A_platformHeading': [idl.id(135912205), ],
    }
)
class P_Navigation_PSM_C_Heading:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_sensorHeading: float = 0.0
    A_platformHeading: float = 0.0

P_Navigation_PSM.C_Heading = P_Navigation_PSM_C_Heading

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Attitude")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_sensorAttitude': [idl.id(179166098), ],
    }
)
class P_Navigation_PSM_C_Attitude:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_sensorAttitude: P_LDM_Common.T_Attitude = field(default_factory = P_LDM_Common.T_Attitude)

P_Navigation_PSM.C_Attitude = P_Navigation_PSM_C_Attitude

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Res_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_maxDataCalcRate': [idl.id(159280183), ],
        'A_worldMagModelSupport': [idl.id(32340622), ],
        'A_supportOutputSourceID': [idl.id(195793017), ],
        'A_supportSetupSourceID': [idl.id(262867245), ],
    }
)
class P_Navigation_PSM_C_Nav_Res_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_maxDataCalcRate: float = 0.0
    A_worldMagModelSupport: bool = False
    A_supportOutputSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_supportSetupSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Navigation_PSM.C_Nav_Res_Specification = P_Navigation_PSM_C_Nav_Res_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Res_Attitude_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_pitchSupport': [idl.id(230383644), ],
        'A_rollSupport': [idl.id(139232426), ],
        'A_yawSupport': [idl.id(160464970), ],
    }
)
class P_Navigation_PSM_C_Nav_Res_Attitude_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_pitchSupport: bool = False
    A_rollSupport: bool = False
    A_yawSupport: bool = False

P_Navigation_PSM.C_Nav_Res_Attitude_Specification = P_Navigation_PSM_C_Nav_Res_Attitude_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_PositionUncertainty")],
    member_annotations = {
        'A_positionUncertainty': [idl.id(1605410), ],
        'A_positionUncertaintyValue': [idl.id(254759515), ],
        'A_heightUncertainty': [idl.id(81183808), ],
        'A_heightUncertaintyValue': [idl.id(174727286), ],
    }
)
class P_Navigation_PSM_C_PositionUncertainty(P_Navigation_PSM.C_Position):
    A_positionUncertainty: P_Navigation_PSM.T_Uncertainty = P_Navigation_PSM.T_Uncertainty.L_Uncertainty_GDOP
    A_positionUncertaintyValue: float = 0.0
    A_heightUncertainty: P_Navigation_PSM.T_Uncertainty = P_Navigation_PSM.T_Uncertainty.L_Uncertainty_GDOP
    A_heightUncertaintyValue: float = 0.0

P_Navigation_PSM.C_PositionUncertainty = P_Navigation_PSM_C_PositionUncertainty

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Limit_Setting")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_pitchRateLimit': [idl.id(174233877), ],
        'A_rollRateLimit': [idl.id(191304320), ],
        'A_yawRateLimit': [idl.id(146895806), ],
        'A_pitchRateExceedance': [idl.id(35818924), ],
        'A_rollRateExceedance': [idl.id(202574286), ],
        'A_yawRateExceedance': [idl.id(229511805), ],
        'A_pitchAccelLimit': [idl.id(252995204), ],
        'A_rollAccelLimit': [idl.id(41107519), ],
        'A_yawAccelLimit': [idl.id(194580807), ],
        'A_pitchAccelExceedance': [idl.id(73677718), ],
        'A_rollAccelExceedance': [idl.id(41445025), ],
        'A_yawAccelExceedance': [idl.id(67692584), ],
        'A_xAxisVelocityLimit': [idl.id(233330941), ],
        'A_yAxisVelocityLimit': [idl.id(143926475), ],
        'A_zAxisVelocityLimit': [idl.id(111466450), ],
        'A_xAxisVelocityExceed': [idl.id(75779922), ],
        'A_yAxisVelocityExceed': [idl.id(99176088), ],
        'A_zAxisVelocityExceed': [idl.id(60695735), ],
        'A_xAxisAccelLimit': [idl.id(12141822), ],
        'A_yAxisAccelLimit': [idl.id(43947991), ],
        'A_zAxisAccelLimit': [idl.id(229290353), ],
        'A_xAxisAccelExceedance': [idl.id(193596986), ],
        'A_yAxisAccelExceedance': [idl.id(2143107), ],
        'A_zAxisAccelExceedance': [idl.id(26513007), ],
        'A_pitchAngleLimit': [idl.id(79217714), ],
        'A_pitchAngleExceedance': [idl.id(168221596), ],
        'A_rollAngleLimit': [idl.id(3053779), ],
        'A_rollAngleExceedance': [idl.id(117737275), ],
    }
)
class P_Navigation_PSM_C_Motion_Limit_Setting:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_pitchRateLimit: float = 0.0
    A_rollRateLimit: float = 0.0
    A_yawRateLimit: float = 0.0
    A_pitchRateExceedance: bool = False
    A_rollRateExceedance: bool = False
    A_yawRateExceedance: bool = False
    A_pitchAccelLimit: float = 0.0
    A_rollAccelLimit: float = 0.0
    A_yawAccelLimit: float = 0.0
    A_pitchAccelExceedance: bool = False
    A_rollAccelExceedance: bool = False
    A_yawAccelExceedance: bool = False
    A_xAxisVelocityLimit: float = 0.0
    A_yAxisVelocityLimit: float = 0.0
    A_zAxisVelocityLimit: float = 0.0
    A_xAxisVelocityExceed: bool = False
    A_yAxisVelocityExceed: bool = False
    A_zAxisVelocityExceed: bool = False
    A_xAxisAccelLimit: float = 0.0
    A_yAxisAccelLimit: float = 0.0
    A_zAxisAccelLimit: float = 0.0
    A_xAxisAccelExceedance: bool = False
    A_yAxisAccelExceedance: bool = False
    A_zAxisAccelExceedance: bool = False
    A_pitchAngleLimit: float = 0.0
    A_pitchAngleExceedance: bool = False
    A_rollAngleLimit: float = 0.0
    A_rollAngleExceedance: bool = False

P_Navigation_PSM.C_Motion_Limit_Setting = P_Navigation_PSM_C_Motion_Limit_Setting

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Navigation_Frame_Velocity")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_northVelocity': [idl.id(139062098), ],
        'A_eastVelocity': [idl.id(50170541), ],
        'A_downVelocity': [idl.id(167957270), ],
    }
)
class P_Navigation_PSM_C_Navigation_Frame_Velocity:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_northVelocity: float = 0.0
    A_eastVelocity: float = 0.0
    A_downVelocity: float = 0.0

P_Navigation_PSM.C_Navigation_Frame_Velocity = P_Navigation_PSM_C_Navigation_Frame_Velocity

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Linear_Motion")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_platformFrameVelocity': [idl.id(203088002), ],
        'A_platformFrameAccel': [idl.id(252667915), ],
        'A_axis': [idl.id(38414735), ],
    }
)
class P_Navigation_PSM_C_Linear_Motion:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_platformFrameVelocity: float = 0.0
    A_platformFrameAccel: float = 0.0
    A_axis: P_LDM_Common.T_Axis3D = P_LDM_Common.T_Axis3D.L_Axis3D_INVALID

P_Navigation_PSM.C_Linear_Motion = P_Navigation_PSM_C_Linear_Motion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Install_Align_Setting")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_installationOffset': [idl.id(248008378), ],
        'A_installationAttitude': [idl.id(225390158), ],
    }
)
class P_Navigation_PSM_C_Install_Align_Setting:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_installationOffset: P_LDM_Common.T_LinearOffset = field(default_factory = P_LDM_Common.T_LinearOffset)
    A_installationAttitude: P_LDM_Common.T_Attitude = field(default_factory = P_LDM_Common.T_Attitude)

P_Navigation_PSM.C_Install_Align_Setting = P_Navigation_PSM_C_Install_Align_Setting

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Res_Output_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_headingSupport': [idl.id(2776891), ],
        'A_positionSupport': [idl.id(20171753), ],
        'A_platformVelocitySupport': [idl.id(106146439), ],
        'A_navigationVelocitySupport': [idl.id(153799713), ],
        'A_posUncertaintySupport': [idl.id(181375069), ],
        'A_heightSupport': [idl.id(149293336), ],
        'A_heightUncertaintySupport': [idl.id(91277288), ],
        'A_dateSupport': [idl.id(267491668), ],
        'A_timeSupport': [idl.id(33164017), ],
        'A_platformAccelSupport': [idl.id(36243438), ],
        'A_distCalcSinceSystemReady': [idl.id(61325987), ],
    }
)
class P_Navigation_PSM_C_Nav_Res_Output_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_headingSupport: bool = False
    A_positionSupport: bool = False
    A_platformVelocitySupport: bool = False
    A_navigationVelocitySupport: bool = False
    A_posUncertaintySupport: bool = False
    A_heightSupport: bool = False
    A_heightUncertaintySupport: bool = False
    A_dateSupport: bool = False
    A_timeSupport: bool = False
    A_platformAccelSupport: bool = False
    A_distCalcSinceSystemReady: bool = False

P_Navigation_PSM.C_Nav_Res_Output_Specification = P_Navigation_PSM_C_Nav_Res_Output_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Res_Setup_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_setPositionSupport': [idl.id(210401564), ],
        'A_setNorthReferenceSupport': [idl.id(121888719), ],
        'A_setCoordSystemSupport': [idl.id(42483439), ],
        'A_installAlignmentSupport': [idl.id(31529420), ],
        'A_limitsSupport': [idl.id(9099665), ],
        'A_setDataOutputRatesSupport': [idl.id(224237084), ],
        'A_keyedGpsSupport': [idl.id(58700755), ],
    }
)
class P_Navigation_PSM_C_Nav_Res_Setup_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_setPositionSupport: bool = False
    A_setNorthReferenceSupport: bool = False
    A_setCoordSystemSupport: bool = False
    A_installAlignmentSupport: bool = False
    A_limitsSupport: bool = False
    A_setDataOutputRatesSupport: bool = False
    A_keyedGpsSupport: bool = False

P_Navigation_PSM.C_Nav_Res_Setup_Specification = P_Navigation_PSM_C_Nav_Res_Setup_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Angular_Motion")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_angularAccelAboutAxis': [idl.id(20220794), ],
        'A_angularVelocityAboutAxis': [idl.id(91215792), ],
        'A_axis': [idl.id(38414735), ],
    }
)
class P_Navigation_PSM_C_Angular_Motion:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_angularAccelAboutAxis: float = 0.0
    A_angularVelocityAboutAxis: float = 0.0
    A_axis: P_LDM_Common.T_Axis3D = P_LDM_Common.T_Axis3D.L_Axis3D_INVALID

P_Navigation_PSM.C_Angular_Motion = P_Navigation_PSM_C_Angular_Motion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Speedometer")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_measuredSpeed': [idl.id(19973484), ],
    }
)
class P_Navigation_PSM_C_Speedometer:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_measuredSpeed: float = 0.0

P_Navigation_PSM.C_Speedometer = P_Navigation_PSM_C_Speedometer

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Coord_System_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_coordinateSystemTypeName': [idl.id(170290458), ],
    }
)
class P_Navigation_PSM_C_Coord_System_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_coordinateSystemTypeName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Navigation_PSM.C_Coord_System_Specification = P_Navigation_PSM_C_Coord_System_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Coord_Datum_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_coordinateDatumTypeName': [idl.id(26403290), ],
        'A_selectedNavResSourceID': [idl.id(262521872), idl.bound(20)],
        'A_navResSpecificationSourceID': [idl.id(108459785), idl.bound(20)],
        'A_coordSysSpecificationSourceID': [idl.id(253558903), idl.bound(2)],
    }
)
class P_Navigation_PSM_C_Coord_Datum_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_coordinateDatumTypeName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_selectedNavResSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_navResSpecificationSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_coordSysSpecificationSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)

P_Navigation_PSM.C_Coord_Datum_Specification = P_Navigation_PSM_C_Coord_Datum_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Platform_Mobility_State")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_platformIsMoving': [idl.id(114595823), ],
    }
)
class P_Navigation_PSM_C_Platform_Mobility_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_platformIsMoving: bool = False

P_Navigation_PSM.C_Platform_Mobility_State = P_Navigation_PSM_C_Platform_Mobility_State

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Report")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_currentPosition': [idl.id(139922608), ],
        'A_platformHeading': [idl.id(135912205), ],
        'A_sensorAttitude': [idl.id(179166098), ],
        'A_northVelocity': [idl.id(139062098), ],
        'A_eastVelocity': [idl.id(50170541), ],
        'A_downVelocity': [idl.id(167957270), ],
        'A_accelerationX': [idl.id(29093206), ],
        'A_accelerationY': [idl.id(15524911), ],
        'A_accelerationZ': [idl.id(33529724), ],
        'A_angularVelocityXComponent': [idl.id(226565320), ],
        'A_angularVelocityYComponent': [idl.id(118196319), ],
        'A_angularVelocityZComponent': [idl.id(8685478), ],
    }
)
class P_Navigation_PSM_C_Motion_Report:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_currentPosition: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_platformHeading: float = 0.0
    A_sensorAttitude: P_LDM_Common.T_Attitude = field(default_factory = P_LDM_Common.T_Attitude)
    A_northVelocity: float = 0.0
    A_eastVelocity: float = 0.0
    A_downVelocity: float = 0.0
    A_accelerationX: float = 0.0
    A_accelerationY: float = 0.0
    A_accelerationZ: float = 0.0
    A_angularVelocityXComponent: float = 0.0
    A_angularVelocityYComponent: float = 0.0
    A_angularVelocityZComponent: float = 0.0

P_Navigation_PSM.C_Motion_Report = P_Navigation_PSM_C_Motion_Report

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Aligment_Survey_Status")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_mode': [idl.id(236875199), ],
    }
)
class P_Navigation_PSM_C_Aligment_Survey_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_mode: P_Navigation_PSM.T_AlignMode = P_Navigation_PSM.T_AlignMode.L_AlignMode_NORMAL_ALIGN

P_Navigation_PSM.C_Aligment_Survey_Status = P_Navigation_PSM_C_Aligment_Survey_Status

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_GridConvergeReq_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_GridConvergeReq_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Navigation_PSM.C_Nav_Resource_GridConvergeReq_Cmd = P_Navigation_PSM_C_Nav_Resource_GridConvergeReq_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_MagnVariationReq_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_MagnVariationReq_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Navigation_PSM.C_Nav_Resource_MagnVariationReq_Cmd = P_Navigation_PSM_C_Nav_Resource_MagnVariationReq_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_SetMagnVariation_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_magneticVariation': [idl.id(123328125), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_SetMagnVariation_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_magneticVariation: float = 0.0

P_Navigation_PSM.C_Nav_Resource_SetMagnVariation_Cmd = P_Navigation_PSM_C_Nav_Resource_SetMagnVariation_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_SetUTC_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_timeOfDay': [idl.id(36504274), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_SetUTC_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_timeOfDay: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Navigation_PSM.C_Nav_Resource_SetUTC_Cmd = P_Navigation_PSM_C_Nav_Resource_SetUTC_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_SetZuptMode_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_modeOn': [idl.id(3361706), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_SetZuptMode_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_modeOn: bool = False

P_Navigation_PSM.C_Nav_Resource_SetZuptMode_Cmd = P_Navigation_PSM_C_Nav_Resource_SetZuptMode_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_SetDataOutRate_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_statusOutput': [idl.id(238513276), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_SetDataOutRate_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_statusOutput: float = 0.0

P_Navigation_PSM.C_Nav_Resource_SetDataOutRate_Cmd = P_Navigation_PSM_C_Nav_Resource_SetDataOutRate_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_SetCoordSystem_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_coordDatumTypeName': [idl.id(208920108), ],
        'A_coordSystemTypeName': [idl.id(116612161), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_SetCoordSystem_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_coordDatumTypeName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_coordSystemTypeName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Navigation_PSM.C_Nav_Resource_SetCoordSystem_Cmd = P_Navigation_PSM_C_Nav_Resource_SetCoordSystem_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_Resource_SetNorthRef_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_datum': [idl.id(21432654), ],
    }
)
class P_Navigation_PSM_C_Nav_Resource_SetNorthRef_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_datum: P_Navigation_PSM.T_HeadingRefDatum = P_Navigation_PSM.T_HeadingRefDatum.L_HeadingRefDatum_MAGNETIC

P_Navigation_PSM.C_Nav_Resource_SetNorthRef_Cmd = P_Navigation_PSM_C_Nav_Resource_SetNorthRef_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_System_StoreHeadingAlign_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_heading': [idl.id(100681476), ],
    }
)
class P_Navigation_PSM_C_Nav_System_StoreHeadingAlign_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_heading: float = 0.0

P_Navigation_PSM.C_Nav_System_StoreHeadingAlign_Cmd = P_Navigation_PSM_C_Nav_System_StoreHeadingAlign_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Magnetometer_Calibrate_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_bearingFromMagNorth': [idl.id(185634357), ],
    }
)
class P_Navigation_PSM_C_Magnetometer_Calibrate_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_bearingFromMagNorth: float = 0.0

P_Navigation_PSM.C_Magnetometer_Calibrate_Cmd = P_Navigation_PSM_C_Magnetometer_Calibrate_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Odometer_ResetDistance_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Navigation_PSM_C_Odometer_ResetDistance_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Navigation_PSM.C_Odometer_ResetDistance_Cmd = P_Navigation_PSM_C_Odometer_ResetDistance_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Position_SetUncertaintyTypes_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_heightUncertainty': [idl.id(81183808), ],
        'A_positionUncertainty': [idl.id(1605410), ],
    }
)
class P_Navigation_PSM_C_Position_SetUncertaintyTypes_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_heightUncertainty: P_Navigation_PSM.T_Uncertainty = P_Navigation_PSM.T_Uncertainty.L_Uncertainty_GDOP
    A_positionUncertainty: P_Navigation_PSM.T_Uncertainty = P_Navigation_PSM.T_Uncertainty.L_Uncertainty_GDOP

P_Navigation_PSM.C_Position_SetUncertaintyTypes_Cmd = P_Navigation_PSM_C_Position_SetUncertaintyTypes_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Position_SetCurrentPosition_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_position': [idl.id(26705633), ],
    }
)
class P_Navigation_PSM_C_Position_SetCurrentPosition_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_position: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Navigation_PSM.C_Position_SetCurrentPosition_Cmd = P_Navigation_PSM_C_Position_SetCurrentPosition_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Heading_SetCurrentHeading_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_heading': [idl.id(100681476), ],
    }
)
class P_Navigation_PSM_C_Heading_SetCurrentHeading_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_heading: float = 0.0

P_Navigation_PSM.C_Heading_SetCurrentHeading_Cmd = P_Navigation_PSM_C_Heading_SetCurrentHeading_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Limit_SetPitchRollLimit_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_pitchLimit': [idl.id(2373853), ],
        'A_rollLimit': [idl.id(76810531), ],
    }
)
class P_Navigation_PSM_C_Motion_Limit_SetPitchRollLimit_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_pitchLimit: float = 0.0
    A_rollLimit: float = 0.0

P_Navigation_PSM.C_Motion_Limit_SetPitchRollLimit_Cmd = P_Navigation_PSM_C_Motion_Limit_SetPitchRollLimit_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Limit_SetLinearAccLimit_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_xLimit': [idl.id(227398557), ],
        'A_yLimit': [idl.id(119482050), ],
        'A_zLimit': [idl.id(230518087), ],
    }
)
class P_Navigation_PSM_C_Motion_Limit_SetLinearAccLimit_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_xLimit: float = 0.0
    A_yLimit: float = 0.0
    A_zLimit: float = 0.0

P_Navigation_PSM.C_Motion_Limit_SetLinearAccLimit_Cmd = P_Navigation_PSM_C_Motion_Limit_SetLinearAccLimit_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Limit_SetVelocityLimit_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_xLimit': [idl.id(227398557), ],
        'A_yLimit': [idl.id(119482050), ],
        'A_zLimit': [idl.id(230518087), ],
    }
)
class P_Navigation_PSM_C_Motion_Limit_SetVelocityLimit_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_xLimit: float = 0.0
    A_yLimit: float = 0.0
    A_zLimit: float = 0.0

P_Navigation_PSM.C_Motion_Limit_SetVelocityLimit_Cmd = P_Navigation_PSM_C_Motion_Limit_SetVelocityLimit_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Limit_SetAngulAccLimit_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_pitchLimit': [idl.id(2373853), ],
        'A_rollLimit': [idl.id(76810531), ],
        'A_yawLimit': [idl.id(89226572), ],
    }
)
class P_Navigation_PSM_C_Motion_Limit_SetAngulAccLimit_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_pitchLimit: float = 0.0
    A_rollLimit: float = 0.0
    A_yawLimit: float = 0.0

P_Navigation_PSM.C_Motion_Limit_SetAngulAccLimit_Cmd = P_Navigation_PSM_C_Motion_Limit_SetAngulAccLimit_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Motion_Limit_SetAngRateLimit_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_pitchLimit': [idl.id(2373853), ],
        'A_rollLimit': [idl.id(76810531), ],
        'A_yawLimit': [idl.id(89226572), ],
    }
)
class P_Navigation_PSM_C_Motion_Limit_SetAngRateLimit_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_pitchLimit: float = 0.0
    A_rollLimit: float = 0.0
    A_yawLimit: float = 0.0

P_Navigation_PSM.C_Motion_Limit_SetAngRateLimit_Cmd = P_Navigation_PSM_C_Motion_Limit_SetAngRateLimit_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Install_Align_SetInstallOffset_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_installationOffset': [idl.id(248008378), ],
    }
)
class P_Navigation_PSM_C_Install_Align_SetInstallOffset_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_installationOffset: P_LDM_Common.T_LinearOffset = field(default_factory = P_LDM_Common.T_LinearOffset)

P_Navigation_PSM.C_Install_Align_SetInstallOffset_Cmd = P_Navigation_PSM_C_Install_Align_SetInstallOffset_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Install_Align_SetInstAttitude_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_installationAttitude': [idl.id(225390158), ],
    }
)
class P_Navigation_PSM_C_Install_Align_SetInstAttitude_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_installationAttitude: P_LDM_Common.T_Attitude = field(default_factory = P_LDM_Common.T_Attitude)

P_Navigation_PSM.C_Install_Align_SetInstAttitude_Cmd = P_Navigation_PSM_C_Install_Align_SetInstAttitude_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_System_Realign_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Navigation_PSM_C_Nav_System_Realign_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Navigation_PSM.C_Nav_System_Realign_Cmd = P_Navigation_PSM_C_Nav_System_Realign_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Navigation_PSM::C_Nav_GPS_Connect_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_connect': [idl.id(245357314), ],
    }
)
class P_Navigation_PSM_C_Nav_GPS_Connect_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_connect: bool = False

P_Navigation_PSM.C_Nav_GPS_Connect_Cmd = P_Navigation_PSM_C_Nav_GPS_Connect_Cmd
