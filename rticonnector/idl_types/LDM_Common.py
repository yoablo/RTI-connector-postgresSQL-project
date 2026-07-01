# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from LDM_Common.idl
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

P_LDM_Common = idl.get_module("P_LDM_Common")

P_LDM_Common_T_Char = idl.char

P_LDM_Common.T_Char = P_LDM_Common_T_Char

P_LDM_Common_T_Byte = idl.uint8

P_LDM_Common.T_Byte = P_LDM_Common_T_Byte

P_LDM_Common_T_Int16 = idl.int16

P_LDM_Common.T_Int16 = P_LDM_Common_T_Int16

P_LDM_Common_T_UInt16 = idl.uint16

P_LDM_Common.T_UInt16 = P_LDM_Common_T_UInt16

P_LDM_Common_T_Int32 = idl.int32

P_LDM_Common.T_Int32 = P_LDM_Common_T_Int32

P_LDM_Common_T_UInt32 = idl.uint32

P_LDM_Common.T_UInt32 = P_LDM_Common_T_UInt32

P_LDM_Common_T_Int64 = int

P_LDM_Common.T_Int64 = P_LDM_Common_T_Int64

P_LDM_Common_T_UInt64 = idl.uint64

P_LDM_Common.T_UInt64 = P_LDM_Common_T_UInt64

P_LDM_Common_T_Single = idl.float32

P_LDM_Common.T_Single = P_LDM_Common_T_Single

P_LDM_Common_T_Double = float

P_LDM_Common.T_Double = P_LDM_Common_T_Double

P_LDM_Common_T_Boolean = bool

P_LDM_Common.T_Boolean = P_LDM_Common_T_Boolean


@idl.alias(
    annotations=[
        idl.bound(10),
    ]
)
class P_LDM_Common_T_VeryShortString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_VeryShortString = P_LDM_Common_T_VeryShortString


@idl.alias(
    annotations=[
        idl.bound(20),
    ]
)
class P_LDM_Common_T_ShortString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_ShortString = P_LDM_Common_T_ShortString


@idl.alias(
    annotations=[
        idl.bound(32),
    ]
)
class P_LDM_Common_T_RegularString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_RegularString = P_LDM_Common_T_RegularString


@idl.alias(
    annotations=[
        idl.bound(100),
    ]
)
class P_LDM_Common_T_MediumString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_MediumString = P_LDM_Common_T_MediumString


@idl.alias(
    annotations=[
        idl.bound(500),
    ]
)
class P_LDM_Common_T_LongString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_LongString = P_LDM_Common_T_LongString

P_LDM_Common_T_Descriptor = P_LDM_Common.T_ShortString

P_LDM_Common.T_Descriptor = P_LDM_Common_T_Descriptor

P_LDM_Common_T_Percentage = float

P_LDM_Common.T_Percentage = P_LDM_Common_T_Percentage

P_LDM_Common_T_Probability = float

P_LDM_Common.T_Probability = P_LDM_Common_T_Probability

P_LDM_Common_T_DistanceInMeters = float

P_LDM_Common.T_DistanceInMeters = P_LDM_Common_T_DistanceInMeters

P_LDM_Common_T_AngleInRadians = float

P_LDM_Common.T_AngleInRadians = P_LDM_Common_T_AngleInRadians

P_LDM_Common_T_ForceInNewtons = float

P_LDM_Common.T_ForceInNewtons = P_LDM_Common_T_ForceInNewtons

P_LDM_Common_T_FrequencyInHertz = float

P_LDM_Common.T_FrequencyInHertz = P_LDM_Common_T_FrequencyInHertz

P_LDM_Common_T_SpeedInMetPerSec = float

P_LDM_Common.T_SpeedInMetPerSec = P_LDM_Common_T_SpeedInMetPerSec

P_LDM_Common_T_AngularVelocityInRadPerSec = float

P_LDM_Common.T_AngularVelocityInRadPerSec = P_LDM_Common_T_AngularVelocityInRadPerSec

P_LDM_Common_T_LinearAcceleratInMetPerSec2 = float

P_LDM_Common.T_LinearAcceleratInMetPerSec2 = P_LDM_Common_T_LinearAcceleratInMetPerSec2

P_LDM_Common_T_AngularAcceleratInRadPerSec2 = float

P_LDM_Common.T_AngularAcceleratInRadPerSec2 = (
    P_LDM_Common_T_AngularAcceleratInRadPerSec2
)

P_LDM_Common_T_Latitude = float

P_LDM_Common.T_Latitude = P_LDM_Common_T_Latitude

P_LDM_Common_T_Longitude = float

P_LDM_Common.T_Longitude = P_LDM_Common_T_Longitude

P_LDM_Common_T_Altitude = float

P_LDM_Common.T_Altitude = P_LDM_Common_T_Altitude

P_LDM_Common_T_Bearing = float

P_LDM_Common.T_Bearing = P_LDM_Common_T_Bearing

P_LDM_Common_T_Heading = float

P_LDM_Common.T_Heading = P_LDM_Common_T_Heading

P_LDM_Common_T_LiquidVolume = float

P_LDM_Common.T_LiquidVolume = P_LDM_Common_T_LiquidVolume

P_LDM_Common_T_Temperature = float

P_LDM_Common.T_Temperature = P_LDM_Common_T_Temperature

P_LDM_Common_T_Height = float

P_LDM_Common.T_Height = P_LDM_Common_T_Height

P_LDM_Common_T_Area = float

P_LDM_Common.T_Area = P_LDM_Common_T_Area

P_LDM_Common_T_Volume = float

P_LDM_Common.T_Volume = P_LDM_Common_T_Volume

P_LDM_Common_T_Ratio = float

P_LDM_Common.T_Ratio = P_LDM_Common_T_Ratio

P_LDM_Common_T_Current = float

P_LDM_Common.T_Current = P_LDM_Common_T_Current

P_LDM_Common_T_Voltage = float

P_LDM_Common.T_Voltage = P_LDM_Common_T_Voltage

P_LDM_Common_T_Impedance = float

P_LDM_Common.T_Impedance = P_LDM_Common_T_Impedance


@idl.enum
class P_LDM_Common_T_Axis3D(IntEnum):
    L_Axis3D_INVALID = 0
    L_Axis3D_X_AXIS = 1
    L_Axis3D_Y_AXIS = 2
    L_Axis3D_Z_AXIS = 3


P_LDM_Common.T_Axis3D = P_LDM_Common_T_Axis3D


@idl.enum
class P_LDM_Common_T_OnOff(IntEnum):
    L_OnOff_ON = 0
    L_OnOff_OFF = 1


P_LDM_Common.T_OnOff = P_LDM_Common_T_OnOff


@idl.enum
class P_LDM_Common_T_EnabledState(IntEnum):
    L_EnabledState_ENABLED = 0
    L_EnabledState_DISABLED = 1


P_LDM_Common.T_EnabledState = P_LDM_Common_T_EnabledState


@idl.enum
class P_LDM_Common_T_Value_Source(IntEnum):
    L_Value_Source_UNKNOWN = 0
    L_Value_Source_CALCULATED = 1
    L_Value_Source_MEASURED = 2
    L_Value_Source_REPORTED = 3


P_LDM_Common.T_Value_Source = P_LDM_Common_T_Value_Source


@idl.enum
class P_LDM_Common_T_Command_Response(IntEnum):
    L_Command_Response_INVALID = 0
    L_Command_Response_SUCCESS = 1
    L_Command_Response_PENDING = 2
    L_Command_Response_ERROR = 3
    L_Command_Response_INCOMPLETE = 4


P_LDM_Common.T_Command_Response = P_LDM_Common_T_Command_Response


@idl.enum
class P_LDM_Common_T_SightEnslavement_Mode(IntEnum):
    L_SightEnslavement_Mode_IDLE = 0
    L_SightEnslavement_Mode_GS_TO_GUN = 1
    L_SightEnslavement_Mode_GUN_TO_GS = 2
    L_SightEnslavement_Mode_CS_TO_GUN = 3
    L_SightEnslavement_Mode_GUN_TO_CS = 4


P_LDM_Common.T_SightEnslavement_Mode = P_LDM_Common_T_SightEnslavement_Mode


@idl.enum
class P_LDM_Common_T_Operator(IntEnum):
    L_Operator_COMMANDER = 0
    L_Operator_GUNNER = 1
    L_Operator_DRIVER = 2
    L_Operator_OTHER = 3


P_LDM_Common.T_Operator = P_LDM_Common_T_Operator


@idl.enum
class P_LDM_Common_T_System_Action(IntEnum):
    L_System_Action_START = 0
    L_System_Action_ABORT = 1
    L_System_Action_RETRY = 2
    L_System_Action_CONTINUE = 3


P_LDM_Common.T_System_Action = P_LDM_Common_T_System_Action


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Coordinate2D")],
    member_annotations={
        "A_latitude": [
            idl.id(252288645),
        ],
        "A_longitude": [
            idl.id(249776067),
        ],
    },
)
class P_LDM_Common_T_Coordinate2D:
    A_latitude: float = 0.0
    A_longitude: float = 0.0


P_LDM_Common.T_Coordinate2D = P_LDM_Common_T_Coordinate2D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_CoordinatePolar2D")],
    member_annotations={
        "A_azimuth": [
            idl.id(132319399),
        ],
        "A_range": [
            idl.id(149142522),
        ],
    },
)
class P_LDM_Common_T_CoordinatePolar2D:
    A_azimuth: float = 0.0
    A_range: float = 0.0


P_LDM_Common.T_CoordinatePolar2D = P_LDM_Common_T_CoordinatePolar2D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Coordinate3D")],
    member_annotations={
        "A_altitude": [
            idl.id(143806669),
        ],
        "A_latitude": [
            idl.id(252288645),
        ],
        "A_longitude": [
            idl.id(249776067),
        ],
    },
)
class P_LDM_Common_T_Coordinate3D:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


P_LDM_Common.T_Coordinate3D = P_LDM_Common_T_Coordinate3D


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_LDM_Common::T_Covariance_Coordinate3D"),
    ],
    member_annotations={
        "A_altitude_latitude": [
            idl.id(200386494),
        ],
        "A_latitude_longitude": [
            idl.id(187768712),
        ],
        "A_longitude_altitude": [
            idl.id(64158173),
        ],
    },
)
class P_LDM_Common_T_Covariance_Coordinate3D:
    A_altitude_latitude: float = 0.0
    A_latitude_longitude: float = 0.0
    A_longitude_altitude: float = 0.0


P_LDM_Common.T_Covariance_Coordinate3D = P_LDM_Common_T_Covariance_Coordinate3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_CoordinatePolar3D")],
    member_annotations={
        "A_elevation": [
            idl.id(185059946),
        ],
        "A_azimuth": [
            idl.id(132319399),
        ],
        "A_range": [
            idl.id(149142522),
        ],
    },
)
class P_LDM_Common_T_CoordinatePolar3D:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


P_LDM_Common.T_CoordinatePolar3D = P_LDM_Common_T_CoordinatePolar3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_CovariancePolar3D")],
    member_annotations={
        "A_elevation_azimuth": [
            idl.id(201093986),
        ],
        "A_azimuth_range": [
            idl.id(66183831),
        ],
        "A_range_elevation": [
            idl.id(132898885),
        ],
    },
)
class P_LDM_Common_T_CovariancePolar3D:
    A_elevation_azimuth: float = 0.0
    A_azimuth_range: float = 0.0
    A_range_elevation: float = 0.0


P_LDM_Common.T_CovariancePolar3D = P_LDM_Common_T_CovariancePolar3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Identifier")],
    member_annotations={
        "A_platformId": [
            idl.id(193125732),
        ],
        "A_systemId": [
            idl.id(226945837),
        ],
        "A_moduleId": [
            idl.id(98483598),
        ],
    },
)
class P_LDM_Common_T_Identifier:
    A_platformId: idl.int32 = 0
    A_systemId: idl.int16 = 0
    A_moduleId: idl.int16 = 0


P_LDM_Common.T_Identifier = P_LDM_Common_T_Identifier


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_DateTime")],
    member_annotations={
        "A_seconds": [
            idl.id(47523875),
        ],
        "A_nanoseconds": [
            idl.id(168751860),
        ],
    },
)
class P_LDM_Common_T_DateTime:
    A_seconds: int = 0
    A_nanoseconds: idl.int32 = 0


P_LDM_Common.T_DateTime = P_LDM_Common_T_DateTime


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Duration")],
    member_annotations={
        "A_seconds": [
            idl.id(47523875),
        ],
        "A_nanoseconds": [
            idl.id(168751860),
        ],
    },
)
class P_LDM_Common_T_Duration:
    A_seconds: idl.uint32 = 0
    A_nanoseconds: idl.uint32 = 0


P_LDM_Common.T_Duration = P_LDM_Common_T_Duration


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Version")],
    member_annotations={
        "A_major": [
            idl.id(181829708),
        ],
        "A_minor": [
            idl.id(123566980),
        ],
        "A_revision": [
            idl.id(120131913),
        ],
        "A_build": [
            idl.id(132241162),
        ],
    },
)
class P_LDM_Common_T_Version:
    A_major: idl.uint16 = 0
    A_minor: idl.uint16 = 0
    A_revision: idl.uint16 = 0
    A_build: idl.uint16 = 0


P_LDM_Common.T_Version = P_LDM_Common_T_Version


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Attitude")],
    member_annotations={
        "A_pitch": [
            idl.id(234084394),
        ],
        "A_roll": [
            idl.id(37030839),
        ],
        "A_yaw": [
            idl.id(174145604),
        ],
    },
)
class P_LDM_Common_T_Attitude:
    A_pitch: float = 0.0
    A_roll: float = 0.0
    A_yaw: float = 0.0


P_LDM_Common.T_Attitude = P_LDM_Common_T_Attitude


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_LinearOffset")],
    member_annotations={
        "A_xOffset": [
            idl.id(155543010),
        ],
        "A_yOffset": [
            idl.id(100746606),
        ],
        "A_zOffset": [
            idl.id(158238848),
        ],
    },
)
class P_LDM_Common_T_LinearOffset:
    A_xOffset: float = 0.0
    A_yOffset: float = 0.0
    A_zOffset: float = 0.0


P_LDM_Common.T_LinearOffset = P_LDM_Common_T_LinearOffset


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_RotationalOffset")],
    member_annotations={
        "A_pitchOffset": [
            idl.id(170002966),
        ],
        "A_rollOffset": [
            idl.id(86270452),
        ],
        "A_yawOffset": [
            idl.id(2406003),
        ],
    },
)
class P_LDM_Common_T_RotationalOffset:
    A_pitchOffset: float = 0.0
    A_rollOffset: float = 0.0
    A_yawOffset: float = 0.0


P_LDM_Common.T_RotationalOffset = P_LDM_Common_T_RotationalOffset


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_RotationalPosition")],
    member_annotations={
        "A_azimuth": [
            idl.id(132319399),
        ],
        "A_azimuthAccuracy": [
            idl.id(90381994),
        ],
        "A_elevation": [
            idl.id(185059946),
        ],
        "A_elevationAccuracy": [
            idl.id(5936303),
        ],
    },
)
class P_LDM_Common_T_RotationalPosition:
    A_azimuth: float = 0.0
    A_azimuthAccuracy: float = 0.0
    A_elevation: float = 0.0
    A_elevationAccuracy: float = 0.0


P_LDM_Common.T_RotationalPosition = P_LDM_Common_T_RotationalPosition


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Vector_3D")],
    member_annotations={
        "A_elevation": [
            idl.id(185059946),
        ],
        "A_azimuth": [
            idl.id(132319399),
        ],
        "A_magnitude": [
            idl.id(178695539),
        ],
    },
)
class P_LDM_Common_T_Vector_3D:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_magnitude: float = 0.0


P_LDM_Common.T_Vector_3D = P_LDM_Common_T_Vector_3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_VideoPosition")],
    member_annotations={
        "A_verticalPosition": [
            idl.id(211066011),
        ],
        "A_horizontalPosition": [
            idl.id(83622824),
        ],
    },
)
class P_LDM_Common_T_VideoPosition:
    A_verticalPosition: float = 0.0
    A_horizontalPosition: float = 0.0


P_LDM_Common.T_VideoPosition = P_LDM_Common_T_VideoPosition


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_LDM_Common::T_PixelsVideoPosition"),
    ],
    member_annotations={
        "A_verticalPosition": [
            idl.id(211066011),
        ],
        "A_horizontalPosition": [
            idl.id(83622824),
        ],
    },
)
class P_LDM_Common_T_PixelsVideoPosition:
    A_verticalPosition: idl.int16 = 0
    A_horizontalPosition: idl.int16 = 0


P_LDM_Common.T_PixelsVideoPosition = P_LDM_Common_T_PixelsVideoPosition


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Resolution")],
    member_annotations={
        "A_vertical": [
            idl.id(73630748),
        ],
        "A_horizontal": [
            idl.id(205819821),
        ],
    },
)
class P_LDM_Common_T_Resolution:
    A_vertical: idl.uint16 = 0
    A_horizontal: idl.uint16 = 0


P_LDM_Common.T_Resolution = P_LDM_Common_T_Resolution


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Uuid")],
    member_annotations={
        "A_msb": [
            idl.id(21731089),
        ],
        "A_lsb": [
            idl.id(16396169),
        ],
    },
)
class P_LDM_Common_T_Uuid:
    A_msb: idl.uint64 = 0
    A_lsb: idl.uint64 = 0


P_LDM_Common.T_Uuid = P_LDM_Common_T_Uuid


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Dimension")],
    member_annotations={
        "A_height": [
            idl.id(126938091),
        ],
        "A_length": [
            idl.id(268122242),
        ],
        "A_width": [
            idl.id(216631209),
        ],
    },
)
class P_LDM_Common_T_Dimension:
    A_height: float = 0.0
    A_length: float = 0.0
    A_width: float = 0.0


P_LDM_Common.T_Dimension = P_LDM_Common_T_Dimension


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Pointing3D")],
    member_annotations={
        "A_azimuth": [
            idl.id(132319399),
        ],
        "A_elevation": [
            idl.id(185059946),
        ],
    },
)
class P_LDM_Common_T_Pointing3D:
    A_azimuth: float = 0.0
    A_elevation: float = 0.0


P_LDM_Common.T_Pointing3D = P_LDM_Common_T_Pointing3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Command_Header")],
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
class P_LDM_Common_T_Command_Header:
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


P_LDM_Common.T_Command_Header = P_LDM_Common_T_Command_Header


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Response_Header")],
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
class P_LDM_Common_T_Response_Header:
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


P_LDM_Common.T_Response_Header = P_LDM_Common_T_Response_Header
