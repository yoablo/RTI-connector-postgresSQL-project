from dataclasses import field
from enum import IntEnum
from typing import Sequence, Optional
from rti import idl

from auto_idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet

P_LDM_Common = P_LDM_Common_Objet
P_Tactical_Sensor_PSM = idl.get_module("P_Tactical_Sensor_PSM")


@idl.enum
class P_Tactical_Sensor_PSM_T_IFFCategory(IntEnum):
    L_IFFCategory_UNKNOWN = 0
    L_IFFCategory_FRIEND = 1
    L_IFFCategory_FOE = 2
    L_IFFCategory_UNINVOLVED = 3


P_Tactical_Sensor_PSM.T_IFFCategory = P_Tactical_Sensor_PSM_T_IFFCategory


@idl.enum
class P_Tactical_Sensor_PSM_T_EngagementStatus(IntEnum):
    L_EngagementStatus_UNKNOWN = 0
    L_EngagementStatus_NONE = 1
    L_EngagementStatus_HANDLED = 2
    L_EngagementStatus_DROPPED = 3
    L_EngagementStatus_THRETENING = 4


P_Tactical_Sensor_PSM.T_EngagementStatus = P_Tactical_Sensor_PSM_T_EngagementStatus


@idl.enum
class P_Tactical_Sensor_PSM_T_Interception(IntEnum):
    L_Interception_UNKNOWN = 0
    L_Interception_ON = 1
    L_Interception_MISSING_OUT = 2


P_Tactical_Sensor_PSM.T_Interception = P_Tactical_Sensor_PSM_T_Interception


@idl.enum
class P_Tactical_Sensor_PSM_T_DetectionState(IntEnum):
    L_DetectionState_NONE = 0
    L_DetectionState_VALID_RECOGNIZED = 1
    L_DetectionState_VALID_NOT_RECOGNIZED = 2
    L_DetectionState_DELETED = 3
    L_DetectionState_CANCELED = 4
    L_DetectionState_MERGED = 5
    L_DetectionState_SPLIT = 6
    L_DetectionState_DESTROYED = 7


P_Tactical_Sensor_PSM.T_DetectionState = P_Tactical_Sensor_PSM_T_DetectionState


@idl.enum
class P_Tactical_Sensor_PSM_T_DetectionType(IntEnum):
    L_DetectionType_DETECTION = 0
    L_DetectionType_THREAT = 1
    L_DetectionType_TARGET = 2


P_Tactical_Sensor_PSM.T_DetectionType = P_Tactical_Sensor_PSM_T_DetectionType


@idl.enum
class P_Tactical_Sensor_PSM_T_Trajectory(IntEnum):
    L_Trajectory_UNKNOWN = 0
    L_Trajectory_SURFACE = 1
    L_Trajectory_HORIZON = 2
    L_Trajectory_BALISTIC = 3
    L_Trajectory_STEEP = 4
    L_Trajectory_UNDERNEATH = 5


P_Tactical_Sensor_PSM.T_Trajectory = P_Tactical_Sensor_PSM_T_Trajectory


@idl.enum
class P_Tactical_Sensor_PSM_T_Sensing_Method(IntEnum):
    L_Sensing_Method_UNKNOWN = 0
    L_Sensing_Method_RF = 1
    L_Sensing_Method_OPTIC = 2
    L_Sensing_Method_ACOUSTIC = 3
    L_Sensing_Method_C4I = 4
    L_Sensing_Method_OPERATOR = 5


P_Tactical_Sensor_PSM.T_Sensing_Method = P_Tactical_Sensor_PSM_T_Sensing_Method


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Field_Of_View")],
    member_annotations={
        'A_hfov': [idl.id(219673437), ],
        'A_vfov': [idl.id(94953845), ],
        'A_fovCenter': [idl.id(86166626), ],
    }
)
class P_Tactical_Sensor_PSM_T_Field_Of_View:
    A_hfov: float = 0.0
    A_vfov: float = 0.0
    A_fovCenter: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)


P_Tactical_Sensor_PSM.T_Field_Of_View = P_Tactical_Sensor_PSM_T_Field_Of_View


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Physical_Parameters")],
    member_annotations={
        'A_relativeLocationsBase': [idl.id(202129906), ],
        'A_sensorInertialLocationAvailable': [idl.id(160154763), ],
        'A_sensorInertialLocation': [idl.id(25381208), ],
        'A_relativeLocationAvailable': [idl.id(247777497), ],
        'A_rangeAvailable': [idl.id(260167579), ],
        'A_relativeLocation': [idl.id(176177253), ],
        'A_relativeLocationAccuracy': [idl.id(256823903), ],
        'A_inertialLocationAvailable': [idl.id(239505011), ],
        'A_inertialLocation': [idl.id(199017188), ],
        'A_inertialLocationAccuracy': [idl.id(151609059), ],
        'A_absoluteLocationAvailable': [idl.id(237173483), ],
        'A_absoluteLocation': [idl.id(126442216), ],
        'A_absoluteLocationAccuracy': [idl.id(29155565), ],
        'A_angularVelocityAvailable': [idl.id(90633880), ],
        'A_angularVelocity': [idl.id(41912237), ],
        'A_angularVelocityAccuracy': [idl.id(259421538), ],
        'A_linearSpeedAvailable': [idl.id(17206948), ],
        'A_linearSpeed': [idl.id(79564538), ],
        'A_speedOrientation': [idl.id(105149909), ],
        'A_linearSpeedAccuracy': [idl.id(140233796), ],
        'A_radialVelocityAvailable': [idl.id(30429412), ],
        'A_radialVelocity': [idl.id(218586043), ],
        'A_radialVelocityAccuracy': [idl.id(12645927), ],
        'A_tangentialVelocityAvailable': [idl.id(206873348), ],
        'A_horizontalTangentialVelocity': [idl.id(195513788), ],
        'A_horizontalTangentialVelocityError': [idl.id(156366719), ],
        'A_verticalTangentialVelocity': [idl.id(194277054), ],
        'A_verticalTangentialVelocityError': [idl.id(201403017), ],
        'A_fieldOfViewAvailable': [idl.id(158004688), ],
        'A_fieldOfView': [idl.id(163011555), ],
    }
)
class P_Tactical_Sensor_PSM_T_Physical_Parameters:
    A_relativeLocationsBase: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_sensorInertialLocationAvailable: bool = False
    A_sensorInertialLocation: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D)
    A_relativeLocationAvailable: bool = False
    A_rangeAvailable: bool = False
    A_relativeLocation: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_relativeLocationAccuracy: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_inertialLocationAvailable: bool = False
    A_inertialLocation: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_inertialLocationAccuracy: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_absoluteLocationAvailable: bool = False
    A_absoluteLocation: P_LDM_Common.T_Coordinate3D = field(default_factory=P_LDM_Common.T_Coordinate3D)
    A_absoluteLocationAccuracy: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D)
    A_angularVelocityAvailable: bool = False
    A_angularVelocity: P_LDM_Common.T_Vector_3D = field(default_factory=P_LDM_Common.T_Vector_3D)
    A_angularVelocityAccuracy: P_LDM_Common.T_Vector_3D = field(default_factory=P_LDM_Common.T_Vector_3D)
    A_linearSpeedAvailable: bool = False
    A_linearSpeed: float = 0.0
    A_speedOrientation: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_linearSpeedAccuracy: float = 0.0
    A_radialVelocityAvailable: bool = False
    A_radialVelocity: float = 0.0
    A_radialVelocityAccuracy: float = 0.0
    A_tangentialVelocityAvailable: bool = False
    A_horizontalTangentialVelocity: float = 0.0
    A_horizontalTangentialVelocityError: float = 0.0
    A_verticalTangentialVelocity: float = 0.0
    A_verticalTangentialVelocityError: float = 0.0
    A_fieldOfViewAvailable: bool = False
    A_fieldOfView: P_Tactical_Sensor_PSM.T_Field_Of_View = field(default_factory=P_Tactical_Sensor_PSM.T_Field_Of_View)


P_Tactical_Sensor_PSM.T_Physical_Parameters = P_Tactical_Sensor_PSM_T_Physical_Parameters


@idl.alias(
    annotations=[idl.bound(20), ]
)
class CharSequence:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Descriptive_Parameters")],
    member_annotations={
        'A_recognizingDetectorTypes': [idl.id(164911381), idl.bound(10)],
        'A_classificationAvailable': [idl.id(74505323), ],
        'A_objectClassification': [idl.id(186028223), idl.bound(20)],
        'A_classificationConfidence': [idl.id(193401693), ],
        'A_detectionSampleSize': [idl.id(238759197), ],
        'A_absoluteSize': [idl.id(141075497), ],
        'A_exposureDuration': [idl.id(40368954), ],
        'A_rangeMethod': [idl.id(127229930), ],
        'A_sourceLocationAccuracy': [idl.id(9859942), ],
        'A_sourceLocation': [idl.id(121402085), ],
    }
)
class P_Tactical_Sensor_PSM_T_Descriptive_Parameters:
    A_recognizingDetectorTypes: Sequence[CharSequence] = field(default_factory=list)
    A_classificationAvailable: bool = False
    A_objectClassification: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))
    A_classificationConfidence: float = 0.0
    A_detectionSampleSize: P_LDM_Common.T_CoordinatePolar3D = field(
        default_factory=P_LDM_Common.T_CoordinatePolar3D)
    A_absoluteSize: P_LDM_Common.T_Dimension = field(default_factory=P_LDM_Common.T_Dimension)
    A_exposureDuration: P_LDM_Common.T_Duration = field(default_factory=P_LDM_Common.T_Duration)
    A_rangeMethod: P_LDM_Common.T_Value_Source = P_LDM_Common.T_Value_Source.L_Value_Source_UNKNOWN
    A_sourceLocationAccuracy: P_LDM_Common.T_Coordinate3D = field(
        default_factory=P_LDM_Common.T_Coordinate3D)
    A_sourceLocation: P_LDM_Common.T_Coordinate3D = field(default_factory=P_LDM_Common.T_Coordinate3D)


P_Tactical_Sensor_PSM.T_Descriptive_Parameters = P_Tactical_Sensor_PSM_T_Descriptive_Parameters


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Spatial_Info")],
    member_annotations={
        'A_physicalInfo': [idl.id(170544614), ],
        'A_descriptiveInfo': [idl.id(219430159), ],
    }
)
class P_Tactical_Sensor_PSM_T_Spatial_Info:
    A_physicalInfo: P_Tactical_Sensor_PSM.T_Physical_Parameters = field(
        default_factory=P_Tactical_Sensor_PSM.T_Physical_Parameters)
    A_descriptiveInfo: P_Tactical_Sensor_PSM.T_Descriptive_Parameters = field(
        default_factory=P_Tactical_Sensor_PSM.T_Descriptive_Parameters)


P_Tactical_Sensor_PSM.T_Spatial_Info = P_Tactical_Sensor_PSM_T_Spatial_Info


@idl.enum
class P_Tactical_Sensor_PSM_T_SuspensionCause(IntEnum):
    L_SuspensionCause_NOT_SUSPENDED = 0
    L_SuspensionCause_UNKNOWN = 1
    L_SuspensionCause_FALSE_DETECTION = 2
    L_SuspensionCause_LATE_DETECTION = 3
    L_SuspensionCause_IRRELEVANT = 4
    L_SuspensionCause_BUSY = 5
    L_SuspensionCause_VANISHED = 6
    L_SuspensionCause_OPERATOR_DECISION = 7


P_Tactical_Sensor_PSM.T_SuspensionCause = P_Tactical_Sensor_PSM_T_SuspensionCause


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_DetectingMethod")],
    member_annotations={
        'A_detectorType': [idl.id(81702893), idl.bound(20)],
        'A_algorithm': [idl.id(156910574), idl.bound(20)],
    }
)
class P_Tactical_Sensor_PSM_T_DetectingMethod:
    A_detectorType: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))
    A_algorithm: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_Tactical_Sensor_PSM.T_DetectingMethod = P_Tactical_Sensor_PSM_T_DetectingMethod


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection")],
    member_annotations={
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_detectionUniqueID': [idl.key, idl.id(246744424), ],
        'A_confidence': [idl.id(136595483), ],
        'A_detectionClassification': [idl.id(85099305), idl.bound(20)],
        'A_detectionClassScore': [idl.id(76917289), ],
        'A_detectionForceType': [idl.id(180790050), ],
        'A_detectionThreatStatus': [idl.id(223270006), ],
        'A_interception': [idl.id(115597617), ],
        'A_detectionStatus': [idl.id(20783098), ],
        'A_type': [idl.id(60540847), ],
        'A_lifeSpan': [idl.id(33812822), ],
        'A_priority': [idl.id(261701171), ],
        'A_trajectoryType': [idl.id(130758057), ],
        'A_method': [idl.id(21615206), idl.bound(15)],
        'A_spatialParametersAvailable': [idl.id(59484478), ],
        'A_spatialInfo': [idl.id(266667200), ],
        'A_suspensionCause': [idl.id(120918324), ],
        'A_designatedInfo': [idl.id(44045387), idl.bound(20)],
        'A_numberOfDetectionMethods': [idl.id(165807565), ],
        'A_detectionMethods': [idl.id(87615255), idl.bound(32)],
        'A_snapshotAvailable': [idl.id(149581014), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_detectionUniqueID: P_LDM_Common.T_Uuid = field(default_factory=P_LDM_Common.T_Uuid)
    A_confidence: float = 0.0
    A_detectionClassification: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))
    A_detectionClassScore: float = 0.0
    A_detectionForceType: P_Tactical_Sensor_PSM.T_IFFCategory =\
        P_Tactical_Sensor_PSM.T_IFFCategory.L_IFFCategory_UNKNOWN
    A_detectionThreatStatus: P_Tactical_Sensor_PSM.T_EngagementStatus =\
        P_Tactical_Sensor_PSM.T_EngagementStatus.L_EngagementStatus_UNKNOWN
    A_interception: P_Tactical_Sensor_PSM.T_Interception =\
        P_Tactical_Sensor_PSM.T_Interception.L_Interception_UNKNOWN
    A_detectionStatus: P_Tactical_Sensor_PSM.T_DetectionState =\
        P_Tactical_Sensor_PSM.T_DetectionState.L_DetectionState_NONE
    A_type: P_Tactical_Sensor_PSM.T_DetectionType = P_Tactical_Sensor_PSM.T_DetectionType.L_DetectionType_DETECTION
    A_lifeSpan: P_LDM_Common.T_Duration = field(default_factory=P_LDM_Common.T_Duration)
    A_priority: idl.int16 = 0
    A_trajectoryType: P_Tactical_Sensor_PSM.T_Trajectory = P_Tactical_Sensor_PSM.T_Trajectory.L_Trajectory_UNKNOWN
    A_method: Sequence[P_Tactical_Sensor_PSM.T_Sensing_Method] = field(default_factory=list)
    A_spatialParametersAvailable: bool = False
    A_spatialInfo: P_Tactical_Sensor_PSM.T_Spatial_Info = field(default_factory=P_Tactical_Sensor_PSM.T_Spatial_Info)
    A_suspensionCause: P_Tactical_Sensor_PSM.T_SuspensionCause =\
        P_Tactical_Sensor_PSM.T_SuspensionCause.L_SuspensionCause_NOT_SUSPENDED
    A_designatedInfo: Optional[Sequence[idl.char]] = None
    A_numberOfDetectionMethods: Optional[idl.uint8] = None
    A_detectionMethods: Optional[Sequence[P_Tactical_Sensor_PSM.T_DetectingMethod]] = None
    A_snapshotAvailable: bool = False


P_Tactical_Sensor_PSM.C_Detection = P_Tactical_Sensor_PSM_C_Detection
