from enum import IntEnum

from rti import idl

P_LDM_Common = idl.get_module("P_LDM_Common")


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Identifier")],
    member_annotations={
        'A_platformId': [idl.id(193125732), ],
        'A_systemId': [idl.id(226945837), ],
        'A_moduleId': [idl.id(98483598), ],
    }
)
class P_LDM_Common_T_Identifier:
    A_platformId: idl.int32 = 0
    A_systemId: idl.int16 = 0
    A_moduleId: idl.int16 = 0


P_LDM_Common.T_Identifier = P_LDM_Common_T_Identifier


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_DateTime")],
    member_annotations={
        'A_seconds': [idl.id(47523875), ],
        'A_nanoseconds': [idl.id(168751860), ],
    }
)
class P_LDM_Common_T_DateTime:
    A_seconds: int = 0
    A_nanoseconds: idl.int32 = 0


P_LDM_Common.T_DateTime = P_LDM_Common_T_DateTime


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Uuid")],
    member_annotations={
        'A_msb': [idl.id(21731089), ],
        'A_lsb': [idl.id(16396169), ],
    }
)
class P_LDM_Common_T_Uuid:
    A_msb: idl.uint64 = 0
    A_lsb: idl.uint64 = 0


P_LDM_Common.T_Uuid = P_LDM_Common_T_Uuid


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Duration")],
    member_annotations={
        'A_seconds': [idl.id(47523875), ],
        'A_nanoseconds': [idl.id(168751860), ],
    }
)
class P_LDM_Common_T_Duration:
    A_seconds: idl.uint32 = 0
    A_nanoseconds: idl.uint32 = 0


P_LDM_Common.T_Duration = P_LDM_Common_T_Duration


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_CoordinatePolar3D")],
    member_annotations={
        'A_elevation': [idl.id(185059946), ],
        'A_azimuth': [idl.id(132319399), ],
        'A_range': [idl.id(149142522), ],
    }
)
class P_LDM_Common_T_CoordinatePolar3D:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


P_LDM_Common.T_CoordinatePolar3D = P_LDM_Common_T_CoordinatePolar3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Coordinate3D")],
    member_annotations={
        'A_altitude': [idl.id(143806669), ],
        'A_latitude': [idl.id(252288645), ],
        'A_longitude': [idl.id(249776067), ],
    }
)
class P_LDM_Common_T_Coordinate3D:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


P_LDM_Common.T_Coordinate3D = P_LDM_Common_T_Coordinate3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Vector_3D")],
    member_annotations={
        'A_elevation': [idl.id(185059946), ],
        'A_azimuth': [idl.id(132319399), ],
        'A_magnitude': [idl.id(178695539), ],
    }
)
class P_LDM_Common_T_Vector_3D:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_magnitude: float = 0.0


P_LDM_Common.T_Vector_3D = P_LDM_Common_T_Vector_3D


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Dimension")],
    member_annotations={
        'A_height': [idl.id(126938091), ],
        'A_length': [idl.id(268122242), ],
        'A_width': [idl.id(216631209), ],
    }
)
class P_LDM_Common_T_Dimension:
    A_height: float = 0.0
    A_length: float = 0.0
    A_width: float = 0.0


P_LDM_Common.T_Dimension = P_LDM_Common_T_Dimension


@idl.enum
class P_LDM_Common_T_Value_Source(IntEnum):
    L_Value_Source_UNKNOWN = 0
    L_Value_Source_CALCULATED = 1
    L_Value_Source_MEASURED = 2
    L_Value_Source_REPORTED = 3


P_LDM_Common.T_Value_Source = P_LDM_Common_T_Value_Source


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_VideoPosition")],
    member_annotations={
        'A_verticalPosition': [idl.id(211066011), ],
        'A_horizontalPosition': [idl.id(83622824), ],
    }
)
class P_LDM_Common_T_VideoPosition:
    A_verticalPosition: float = 0.0
    A_horizontalPosition: float = 0.0


P_LDM_Common.T_VideoPosition = P_LDM_Common_T_VideoPosition


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_Version")],
    member_annotations={
        'A_major': [idl.id(181829708), ],
        'A_minor': [idl.id(123566980), ],
        'A_revision': [idl.id(120131913), ],
        'A_build': [idl.id(132241162), ],
    }
)
class P_LDM_Common_T_Version:
    A_major: idl.uint16 = 0
    A_minor: idl.uint16 = 0
    A_revision: idl.uint16 = 0
    A_build: idl.uint16 = 0


P_LDM_Common.T_Version = P_LDM_Common_T_Version


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_LDM_Common::T_RotationalPosition")],
    member_annotations={
        'A_azimuth': [idl.id(132319399), ],
        'A_azimuthAccuracy': [idl.id(90381994), ],
        'A_elevation': [idl.id(185059946), ],
        'A_elevationAccuracy': [idl.id(5936303), ],
    }
)
class P_LDM_Common_T_RotationalPosition:
    A_azimuth: float = 0.0
    A_azimuthAccuracy: float = 0.0
    A_elevation: float = 0.0
    A_elevationAccuracy: float = 0.0


P_LDM_Common.T_RotationalPosition = P_LDM_Common_T_RotationalPosition


@idl.enum
class P_LDM_Common_T_EnabledState(IntEnum):
    L_EnabledState_ENABLED = 0
    L_EnabledState_DISABLED = 1


P_LDM_Common.T_EnabledState = P_LDM_Common_T_EnabledState
