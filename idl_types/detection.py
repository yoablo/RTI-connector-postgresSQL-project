from dataclasses import field

import rti.idl as idl
import rti.types as types
from typing import Sequence
from miscellaneousEnum import *


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


@idl.struct
class LifeSpan:
    A_seconds: idl.uint32 = 0
    A_nanoseconds: idl.uint32 = 0


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
        'A_recognizingDetectorTypes': [MiscellaneousEnum.VERY_SHORT_STRING * 10],
        'A_objectClassification': [MiscellaneousEnum.SHORT_STRING]
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
    A_rangeMethod: idl.int32 = 0
    A_sourceLocationAccuracy: SourceLocationAccuracy = SourceLocationAccuracy()
    A_sourceLocation: SourceLocation = SourceLocation()


@idl.struct
class SpatialInfo:
    A_physicalInfo: PhysicalParameters = PhysicalParameters()
    A_descriptiveInfo: DescriptiveParameters = DescriptiveParameters()


@idl.struct(
    member_annotations={
        'A_detectorType': [MiscellaneousEnum.SHORT_STRING],
        'A_algorithm': [MiscellaneousEnum.SHORT_STRING],
    }
)
class DetectingMethod:
    A_detectorType: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_algorithm: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))


@idl.struct(
    member_annotations={
        'A_detectionClassification': [MiscellaneousEnum.VERY_SHORT_STRING],
        'A_method': [MiscellaneousEnum.METHODS_COUNT],
        'A_designatedInfo': [MiscellaneousEnum.VERY_SHORT_STRING],
        'A_detectionMethods': [MiscellaneousEnum.DETECTION_METHODS]
    }
)
class Detection:
    A_sourceID: SourceId = SourceId()
    A_timeOfDataGeneration: TimeOfDataGeneration = TimeOfDataGeneration()
    A_detectionUniqueID: DetectionUniqueID = DetectionUniqueID()
    A_confidence: float = 0.0
    A_detectionClassification: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_detectionClassScore: float = 0.0
    A_detectionForceType: idl.int32 = 0
    A_detectionThreatStatus: idl.int32 = 0
    A_interception: idl.int32 = 0
    A_detectionStatus: idl.int32 = 0
    A_type: idl.int32 = 0
    A_lifeSpan: LifeSpan = LifeSpan()
    A_priority: idl.int16 = 0
    A_trajectoryType: idl.int32 = 0
    A_method: Sequence[idl.int32] = field(default_factory=idl.array_factory(idl.int32))
    A_method_ItemsCount: idl.uint32 = 0
    A_spatialParametersAvailable: bool = False
    A_spatialInfo: SpatialInfo = SpatialInfo()
    A_suspensionCause: idl.int32 = 0
    A_designatedInfo: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))
    A_designatedInfo_IsSet: bool = False
    A_numberOfDetectionMethods: idl.uint8 = 0
    A_numberOfDetectionMethods_IsSet: bool = False
    A_detectionMethods: Sequence[DetectingMethod] = field(default_factory=list)
    A_detectionMethods_IsSet: bool = False
    A_detectionMethods_ItemsCount: idl.uint32 = 0
    A_snapshotAvailable: bool = False
