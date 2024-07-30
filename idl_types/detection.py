from enum import IntEnum
from dataclasses import field
from typing import Sequence

import rti.idl as idl
import rti.types as types
from idl_types.miscellaneousEnum import MiscellaneousEnum


@idl.struct
class SourceId:
    A_platformId: idl.int32 = 0
    A_systemId: idl.int16 = 0
    A_moduleId: idl.int16 = 0


@idl.struct
class TimeOfDataGeneration:
    A_seconds: idl.int64 = 0
    A_nanoseconds: idl.int32 = 0


@idl.struct
class DetectionUniqueID:
    A_msb: idl.uint64 = 0
    A_lsb: idl.uint64 = 0


@idl.enum
class DetectionForceType(IntEnum):
    L_IFFCategory_UNKNOWN = 0,
    L_IFFCategory_FRIEND = 1,
    L_IFFCategory_FOE = 2,
    L_IFFCategory_UNINVOLVED = 3


@idl.enum
class DetectionThreatStatus(IntEnum):
    L_EngagementStatus_UNKNOWN = 0,
    L_EngagementStatus_NONE = 1,
    L_EngagementStatus_HANDLED = 2,
    L_EngagementStatus_DROPPED = 3,
    L_EngagementStatus_THRETENING = 4


@idl.enum
class Interception(IntEnum):
    L_Interception_UNKNOWN = 0,
    L_Interception_ON = 1,
    L_Interceptions_MISSING_OUT = 2


@idl.enum
class DetectionStatus(IntEnum):
    L_DetectionState_NONE = 0,
    L_DetectionState_VALID_RECOGNIZED = 1,
    L_DetectionState_VALID_NOT_RECOGNIZED = 2,
    L_DetectionState_DELETED = 3,
    L_DetectionState_CANCELED = 4,
    L_DetectionState_MERGED = 5,
    L_DetectionState_SPLIT = 6


@idl.enum
class Type(IntEnum):
    L_DetectionType_DETECTION = 0,
    L_DetectionType_THREAT = 1,
    L_DetectionType_TARGET = 2


@idl.struct
class LifeSpan:
    A_seconds: idl.uint32 = 0
    A_nanoseconds: idl.uint32 = 0


@idl.enum
class TrajectoryType(IntEnum):
    L_Trajectory_UNKNOWN = 0,
    L_Trajectory_SURFACE = 1,
    L_Trajectory_HORIZON = 2,
    L_Trajectory_BALISTIC = 3,
    L_Trajectory_STEEP = 4,
    L_Trajectory_UNDERNEATH = 5


@idl.enum
class SensingMethod(IntEnum):
    L_Sensing_Method_UNKNOWN = 0,
    L_Sensing_Method_RF = 1,
    L_Sensing_Method_OPTIC = 2,
    L_Sensing_Method_ACOUSTIC = 3,
    L_Sensing_Method_C4I = 4,
    L_Sensing_Method_OPERATOR = 5


@idl.struct
class RelativeLocationsBase:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class SensorInertialLocation:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


@idl.struct
class RelativeLocation:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class RelativeLocationAccuracy:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class InertialLocation:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class InertialLocationAccuracy:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class AbsoluteLocation:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


@idl.struct
class AbsoluteLocationAccuracy:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


@idl.struct
class AngularVelocity:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_magnitude: float = 0.0


@idl.struct
class AngularVelocityAccuracy:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_magnitude: float = 0.0


@idl.struct
class SpeedOrientation:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class FovCenter:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class FieldOfView:
    A_hfov: float = 0.0
    A_vfov: float = 0.0
    A_fovCenter: FovCenter = FovCenter()


@idl.struct
class PhysicalParameters:
    A_relativeLocationsBase: RelativeLocationsBase = RelativeLocationsBase()
    A_sensorInertialLocationAvailable: bool = False
    A_sensorInertialLocation: SensorInertialLocation = SensorInertialLocation()
    A_relativeLocationAvailable: bool = False
    A_rangeAvailable: bool = False
    A_relativeLocation: RelativeLocation = RelativeLocation()
    A_relativeLocationAccuracy: RelativeLocationAccuracy = RelativeLocationAccuracy()
    A_inertialLocationAvailable: bool = False
    A_inertialLocation: InertialLocation = InertialLocation()
    A_inertialLocationAccuracy: InertialLocationAccuracy = InertialLocationAccuracy()
    A_absoluteLocationAvailable: bool = False
    A_absoluteLocation: AbsoluteLocation = AbsoluteLocation()
    A_absoluteLocationAccuracy: RelativeLocationAccuracy = RelativeLocationAccuracy()
    A_angularVelocityAvailable: bool = False
    A_angularVelocity: AngularVelocity = AngularVelocity()
    A_angularVelocityAccuracy: AngularVelocityAccuracy = AngularVelocityAccuracy()
    A_linearSpeedAvailable: bool = False
    A_linearSpeed: float = 0.0
    A_speedOrientation: SpeedOrientation = SpeedOrientation()
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
    A_fieldOfView: FieldOfView = FieldOfView()


@idl.struct
class DetectionSampleSize:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class AbsoluteSize:
    A_height: float = 0.0
    A_length: float = 0.0
    A_width: float = 0.0


@idl.struct
class ExposureDuration:
    A_seconds: idl.uint32 = 0
    A_nanoseconds: idl.uint32 = 0

@idl.enum
class RangeMethod(IntEnum):
    L_Value_Source_UNKNOWN = 0,
    L_Value_Source_CALCULATED = 1,
    L_Value_Source_MEASURED = 2,
    L_Value_Source_REPORTED = 3

@idl.struct
class SourceLocationAccuracy:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


@idl.struct
class SourceLocation:
    A_altitude: float = 0.0
    A_latitude: float = 0.0
    A_longitude: float = 0.0


@idl.struct(
    member_annotations={
        'A_recognizingDetectorTypes': [idl.bound(MiscellaneousEnum.VERY_SHORT_STRING * 10)],
        'A_objectClassification': [idl.bound(MiscellaneousEnum.SHORT_STRING)]
    }
)
class DescriptiveParameters:
    A_recognizingDetectorTypes: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_recognizingDetectorTypes_ItemsCount: idl.uint32 = 0
    A_classificationAvailable: bool = False
    A_objectClassification: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_classificationConfidence: float = 0.0
    A_detectionSampleSize: DetectionSampleSize = DetectionSampleSize()
    A_absoluteSize: AbsoluteSize = AbsoluteSize()
    A_exposureDuration: ExposureDuration = ExposureDuration()
    A_rangeMethod: RangeMethod = 0
    A_sourceLocationAccuracy: SourceLocationAccuracy = SourceLocationAccuracy()
    A_sourceLocation: SourceLocation = SourceLocation()


@idl.struct
class SpatialInfo:
    A_physicalInfo: PhysicalParameters = PhysicalParameters()
    A_descriptiveInfo: DescriptiveParameters = DescriptiveParameters()


@idl.struct
class SuspensionCause(IntEnum):
    L_SuspensionCause_NOT_SUSPENDED = 0,
    L_SuspensionCause_UNKNOWN = 1,
    L_SuspensionCause_FALSE_DETECTION = 2,
    L_SuspensionCause_LATE_DETECTION = 3,
    L_SuspensionCause_IRRELEVANT = 4,
    L_SuspensionCause_BUSY = 5,
    L_SuspensionCause_VANISHED = 6,
    L_SuspensionCause_OPERATOR_DECISION = 7

@idl.struct(
    member_annotations={
        'A_detectorType': [idl.bound(MiscellaneousEnum.SHORT_STRING)],
        'A_algorithm': [idl.bound(MiscellaneousEnum.SHORT_STRING)],
    }
)
class DetectingMethod:
    A_detectorType: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_algorithm: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))


@idl.struct(
    member_annotations={
        'A_sourceID': [idl.key],
        'A_detectionUniqueID': [idl.key],
        'A_detectionClassification': [idl.bound(MiscellaneousEnum.SHORT_STRING)],
        'A_method': [idl.bound(MiscellaneousEnum.METHODS_COUNT)],
        'A_designatedInfo': [idl.bound(MiscellaneousEnum.VERY_SHORT_STRING)],
        'A_detectionMethods': [idl.bound(MiscellaneousEnum.DETECTION_METHODS)]
    }
)
class Detection:
    test: int = 0
    A_sourceID: SourceId = SourceId()
    A_timeOfDataGeneration: TimeOfDataGeneration = TimeOfDataGeneration()
    A_detectionUniqueID: DetectionUniqueID = DetectionUniqueID()
    A_confidence: float = 0.0
    A_detectionClassification: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_detectionClassScore: float = 0.0
    A_detectionForceType: DetectionForceType = 0
    A_detectionThreatStatus: DetectionThreatStatus = 0
    A_interception: Interception = 0
    A_detectionStatus: DetectionStatus = 0
    A_type: Type = 0
    A_lifeSpan: LifeSpan = LifeSpan()
    A_priority: idl.int16 = 0
    A_trajectoryType: TrajectoryType = 0
    A_method: Sequence[SensingMethod] = field(default_factory=list)
    A_method_ItemsCount: idl.uint32 = 0
    A_spatialParametersAvailable: bool = False
    A_spatialInfo: SpatialInfo = SpatialInfo()
    A_suspensionCause: SuspensionCause = 0
    A_designatedInfo: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_designatedInfo_IsSet: bool = False
    A_numberOfDetectionMethods: idl.uint8 = 0
    A_numberOfDetectionMethods_IsSet: bool = False
    A_detectionMethods: Sequence[DetectingMethod] = field(default_factory=list)
    A_detectionMethods_IsSet: bool = False
    A_detectionMethods_ItemsCount: idl.uint32 = 0
    A_snapshotAvailable: bool = False
