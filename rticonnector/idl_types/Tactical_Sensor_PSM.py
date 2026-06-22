
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Tactical_Sensor_PSM.idl
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

P_Tactical_Sensor_PSM = idl.get_module("P_Tactical_Sensor_PSM")

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
    L_DetectionState_IRRELEVANT = 8

P_Tactical_Sensor_PSM.T_DetectionState = P_Tactical_Sensor_PSM_T_DetectionState

@idl.enum
class P_Tactical_Sensor_PSM_T_DetectionType(IntEnum):
    L_DetectionType_DETECTION = 0
    L_DetectionType_THREAT = 1
    L_DetectionType_TARGET = 2

P_Tactical_Sensor_PSM.T_DetectionType = P_Tactical_Sensor_PSM_T_DetectionType

@idl.enum
class P_Tactical_Sensor_PSM_T_EngagementStatus(IntEnum):
    L_EngagementStatus_UNKNOWN = 0
    L_EngagementStatus_NONE = 1
    L_EngagementStatus_HANDLED = 2
    L_EngagementStatus_DROPPED = 3
    L_EngagementStatus_THRETENING = 4

P_Tactical_Sensor_PSM.T_EngagementStatus = P_Tactical_Sensor_PSM_T_EngagementStatus

@idl.enum
class P_Tactical_Sensor_PSM_T_IFFCategory(IntEnum):
    L_IFFCategory_UNKNOWN = 0
    L_IFFCategory_FRIEND = 1
    L_IFFCategory_FOE = 2
    L_IFFCategory_UNINVOLVED = 3

P_Tactical_Sensor_PSM.T_IFFCategory = P_Tactical_Sensor_PSM_T_IFFCategory

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

@idl.enum
class P_Tactical_Sensor_PSM_T_DetectionTrackContent(IntEnum):
    L_DetectionTrackContent_UNKNOWN = 0
    L_DetectionTrackContent_IN_TRACK = 1
    L_DetectionTrackContent_OBSCURED = 2
    L_DetectionTrackContent_END_TRACK = 3

P_Tactical_Sensor_PSM.T_DetectionTrackContent = P_Tactical_Sensor_PSM_T_DetectionTrackContent

@idl.enum
class P_Tactical_Sensor_PSM_T_Interception(IntEnum):
    L_Interception_UNKNOWN = 0
    L_Interception_ON = 1
    L_Interception_MISSING_OUT = 2

P_Tactical_Sensor_PSM.T_Interception = P_Tactical_Sensor_PSM_T_Interception

@idl.enum
class P_Tactical_Sensor_PSM_T_ThreatFamily(IntEnum):
    L_ThreatFamily_UNKNOWN = 0
    L_ThreatFamily_MARNAT = 1
    L_ThreatFamily_TOLAR = 2
    L_ThreatFamily_TANK_BULLET = 3
    L_ThreatFamily_TANNAT = 4
    L_ThreatFamily_OTHER = 5

P_Tactical_Sensor_PSM.T_ThreatFamily = P_Tactical_Sensor_PSM_T_ThreatFamily

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

@idl.enum
class P_Tactical_Sensor_PSM_T_TrackRelation(IntEnum):
    L_TrackRelation_IN = 0
    L_TrackRelation_NEAR = 1

P_Tactical_Sensor_PSM.T_TrackRelation = P_Tactical_Sensor_PSM_T_TrackRelation

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Detection_Unique_Id")],
    member_annotations = {
        'A_sourceID': [idl.id(118386796), ],
        'A_detectionUniqueId': [idl.id(245520743), ],
    }
)
class P_Tactical_Sensor_PSM_T_Detection_Unique_Id:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_detectionUniqueId: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)

P_Tactical_Sensor_PSM.T_Detection_Unique_Id = P_Tactical_Sensor_PSM_T_Detection_Unique_Id

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Revelation_Source")],
    member_annotations = {
        'A_identification': [idl.id(268347597), ],
        'A_revelationTime': [idl.id(197862764), ],
        'A_locationAvailable': [idl.id(262544635), ],
        'A_location': [idl.id(211489702), ],
        'A_locationAccuracy': [idl.id(210648354), ],
    }
)
class P_Tactical_Sensor_PSM_T_Revelation_Source:
    A_identification: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_revelationTime: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_locationAvailable: bool = False
    A_location: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_locationAccuracy: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Tactical_Sensor_PSM.T_Revelation_Source = P_Tactical_Sensor_PSM_T_Revelation_Source

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Field_Of_View")],
    member_annotations = {
        'A_hfov': [idl.id(219673437), ],
        'A_vfov': [idl.id(94953845), ],
        'A_fovCenter': [idl.id(86166626), ],
    }
)
class P_Tactical_Sensor_PSM_T_Field_Of_View:
    A_hfov: float = 0.0
    A_vfov: float = 0.0
    A_fovCenter: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)

P_Tactical_Sensor_PSM.T_Field_Of_View = P_Tactical_Sensor_PSM_T_Field_Of_View

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_DetectingMethod")],
    member_annotations = {
        'A_detectorType': [idl.id(81702893), ],
        'A_algorithm': [idl.id(156910574), ],
    }
)
class P_Tactical_Sensor_PSM_T_DetectingMethod:
    A_detectorType: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_algorithm: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Tactical_Sensor_PSM.T_DetectingMethod = P_Tactical_Sensor_PSM_T_DetectingMethod

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Detection_Topic_Characteristic")],
    member_annotations = {
        'A_detectionID': [idl.id(42345041), ],
        'A_typeName': [idl.id(117117272), ],
    }
)
class P_Tactical_Sensor_PSM_T_Detection_Topic_Characteristic:
    A_detectionID: P_Tactical_Sensor_PSM.T_Detection_Unique_Id = field(default_factory = P_Tactical_Sensor_PSM.T_Detection_Unique_Id)
    A_typeName: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Tactical_Sensor_PSM.T_Detection_Topic_Characteristic = P_Tactical_Sensor_PSM_T_Detection_Topic_Characteristic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Subunit_Status")],
    member_annotations = {
        'A_subUnit': [idl.id(45537546), ],
        'A_activate': [idl.id(78360471), ],
    }
)
class P_Tactical_Sensor_PSM_T_Subunit_Status:
    A_subUnit: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_activate: bool = False

P_Tactical_Sensor_PSM.T_Subunit_Status = P_Tactical_Sensor_PSM_T_Subunit_Status

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Descriptive_Parameters")],
    member_annotations = {
        'A_recognizingDetectorTypes': [idl.id(164911381), idl.bound(10)],
        'A_classificationAvailable': [idl.id(74505323), ],
        'A_objectClassification': [idl.id(186028223), ],
        'A_classificationConfidence': [idl.id(193401693), ],
        'A_detectionSampleSize': [idl.id(238759197), ],
        'A_absoluteSize': [idl.id(141075497), ],
        'A_exposureDuration': [idl.id(40368954), ],
        'A_rangeMethod': [idl.id(127229930), ],
        'A_sourceLocationAccuracy': [idl.id(9859942), ],
        'A_sourceLocationCovariance': [idl.id(117488242), ],
        'A_sourceLocation': [idl.id(121402085), ],
    }
)
class P_Tactical_Sensor_PSM_T_Descriptive_Parameters:
    A_recognizingDetectorTypes: Sequence[P_LDM_Common.T_MediumString] = field(default_factory = list)
    A_classificationAvailable: bool = False
    A_objectClassification: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_classificationConfidence: float = 0.0
    A_detectionSampleSize: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_absoluteSize: P_LDM_Common.T_Dimension = field(default_factory = P_LDM_Common.T_Dimension)
    A_exposureDuration: P_LDM_Common.T_Duration = field(default_factory = P_LDM_Common.T_Duration)
    A_rangeMethod: P_LDM_Common.T_Value_Source = P_LDM_Common.T_Value_Source.L_Value_Source_UNKNOWN
    A_sourceLocationAccuracy: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_sourceLocationCovariance: P_LDM_Common.T_Covariance_Coordinate3D = field(default_factory = P_LDM_Common.T_Covariance_Coordinate3D)
    A_sourceLocation: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Tactical_Sensor_PSM.T_Descriptive_Parameters = P_Tactical_Sensor_PSM_T_Descriptive_Parameters

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Polygon_Point")],
    member_annotations = {
        'A_point': [idl.id(248223038), ],
        'A_accuracy': [idl.id(73885973), ],
    }
)
class P_Tactical_Sensor_PSM_T_Polygon_Point:
    A_point: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_accuracy: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)

P_Tactical_Sensor_PSM.T_Polygon_Point = P_Tactical_Sensor_PSM_T_Polygon_Point

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Physical_Parameters")],
    member_annotations = {
        'A_relativeLocationsBase': [idl.id(202129906), ],
        'A_sensorInertialLocationAvailable': [idl.id(160154763), ],
        'A_sensorInertialLocation': [idl.id(25381208), ],
        'A_relativeLocationAvailable': [idl.id(247777497), ],
        'A_rangeAvailable': [idl.id(260167579), ],
        'A_relativeLocation': [idl.id(176177253), ],
        'A_relativeLocationAccuracy': [idl.id(256823903), ],
        'A_relativeLocationCovariance': [idl.id(90631693), ],
        'A_inertialLocationAvailable': [idl.id(239505011), ],
        'A_inertialLocation': [idl.id(199017188), ],
        'A_inertialLocationAccuracy': [idl.id(151609059), ],
        'A_inertialLocationCovariance': [idl.id(113956340), ],
        'A_absoluteLocationAvailable': [idl.id(237173483), ],
        'A_absoluteLocation': [idl.id(126442216), ],
        'A_absoluteLocationAccuracy': [idl.id(29155565), ],
        'A_absoluteLocationCovariance': [idl.id(212606104), ],
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
    A_relativeLocationsBase: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_sensorInertialLocationAvailable: bool = False
    A_sensorInertialLocation: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_relativeLocationAvailable: bool = False
    A_rangeAvailable: bool = False
    A_relativeLocation: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_relativeLocationAccuracy: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_relativeLocationCovariance: P_LDM_Common.T_CovariancePolar3D = field(default_factory = P_LDM_Common.T_CovariancePolar3D)
    A_inertialLocationAvailable: bool = False
    A_inertialLocation: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_inertialLocationAccuracy: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_inertialLocationCovariance: P_LDM_Common.T_CovariancePolar3D = field(default_factory = P_LDM_Common.T_CovariancePolar3D)
    A_absoluteLocationAvailable: bool = False
    A_absoluteLocation: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_absoluteLocationAccuracy: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_absoluteLocationCovariance: P_LDM_Common.T_Covariance_Coordinate3D = field(default_factory = P_LDM_Common.T_Covariance_Coordinate3D)
    A_angularVelocityAvailable: bool = False
    A_angularVelocity: P_LDM_Common.T_Vector_3D = field(default_factory = P_LDM_Common.T_Vector_3D)
    A_angularVelocityAccuracy: P_LDM_Common.T_Vector_3D = field(default_factory = P_LDM_Common.T_Vector_3D)
    A_linearSpeedAvailable: bool = False
    A_linearSpeed: float = 0.0
    A_speedOrientation: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
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
    A_fieldOfView: P_Tactical_Sensor_PSM.T_Field_Of_View = field(default_factory = P_Tactical_Sensor_PSM.T_Field_Of_View)

P_Tactical_Sensor_PSM.T_Physical_Parameters = P_Tactical_Sensor_PSM_T_Physical_Parameters

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Spatial_Info")],
    member_annotations = {
        'A_physicalInfo': [idl.id(170544614), ],
        'A_descriptiveInfo': [idl.id(219430159), ],
    }
)
class P_Tactical_Sensor_PSM_T_Spatial_Info:
    A_physicalInfo: P_Tactical_Sensor_PSM.T_Physical_Parameters = field(default_factory = P_Tactical_Sensor_PSM.T_Physical_Parameters)
    A_descriptiveInfo: P_Tactical_Sensor_PSM.T_Descriptive_Parameters = field(default_factory = P_Tactical_Sensor_PSM.T_Descriptive_Parameters)

P_Tactical_Sensor_PSM.T_Spatial_Info = P_Tactical_Sensor_PSM_T_Spatial_Info

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_ThreatData")],
    member_annotations = {
        'A_threatID': [idl.id(241586546), ],
        'A_threatType': [idl.id(42452415), ],
        'A_isDetectedByEOS': [idl.id(119038996), ],
        'A_isDetectedBySR': [idl.id(121962734), ],
        'A_isDetectedByPearl': [idl.id(75379114), ],
    }
)
class P_Tactical_Sensor_PSM_T_ThreatData:
    A_threatID: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_threatType: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_isDetectedByEOS: bool = False
    A_isDetectedBySR: bool = False
    A_isDetectedByPearl: bool = False

P_Tactical_Sensor_PSM.T_ThreatData = P_Tactical_Sensor_PSM_T_ThreatData

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_AronlodThreat")],
    member_annotations = {
        'A_orientation': [idl.id(153422287), ],
        'A_distance': [idl.id(178978473), ],
        'A_pencils': [idl.id(135574486), ],
        'A_threatPencils': [idl.id(162902902), idl.bound(32)],
    }
)
class P_Tactical_Sensor_PSM_T_AronlodThreat:
    A_orientation: float = 0.0
    A_distance: float = 0.0
    A_pencils: idl.uint8 = 0
    A_threatPencils: Sequence[P_Tactical_Sensor_PSM.T_ThreatData] = field(default_factory = list)

P_Tactical_Sensor_PSM.T_AronlodThreat = P_Tactical_Sensor_PSM_T_AronlodThreat

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::T_Fusion_Polygon")],
    member_annotations = {
        'A_type': [idl.id(60540847), ],
        'A_classification': [idl.id(261715353), ],
        'A_activityState': [idl.id(8552541), ],
        'A_trackRelation': [idl.id(181324728), ],
        'A_generationTime': [idl.id(172547583), ],
    }
)
class P_Tactical_Sensor_PSM_T_Fusion_Polygon:
    A_type: P_LDM_Common.T_RegularString = field(default_factory = P_LDM_Common.T_RegularString)
    A_classification: P_LDM_Common.T_RegularString = field(default_factory = P_LDM_Common.T_RegularString)
    A_activityState: P_LDM_Common.T_RegularString = field(default_factory = P_LDM_Common.T_RegularString)
    A_trackRelation: P_Tactical_Sensor_PSM.T_TrackRelation = P_Tactical_Sensor_PSM.T_TrackRelation.L_TrackRelation_IN
    A_generationTime: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Tactical_Sensor_PSM.T_Fusion_Polygon = P_Tactical_Sensor_PSM_T_Fusion_Polygon

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_detectorTypesSupport': [idl.id(12414556), idl.bound(10)],
        'A_detectingClassSupport': [idl.id(171675280), idl.bound(50)],
        'A_rangeSupport': [idl.id(8397463), ],
        'A_detectionSizeSupport': [idl.id(83890616), ],
        'A_accuracySupport': [idl.id(114850561), ],
        'A_detectionThreatLevelSupport': [idl.id(79787413), ],
        'A_setDetectorStateSupport': [idl.id(5997863), ],
        'A_videoDetectorSupport': [idl.id(203143827), ],
        'A_snapshotSupport': [idl.id(126899836), ],
        'A_rfSupport': [idl.id(234081465), ],
        'A_maxNumberOfDetectionLocations': [idl.id(192960657), ],
        'A_inertialLocationSupport': [idl.id(176554836), ],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_detectorTypesSupport: Optional[Sequence[P_LDM_Common.T_ShortString]] = None
    A_detectingClassSupport: Optional[Sequence[P_LDM_Common.T_ShortString]] = None
    A_rangeSupport: bool = False
    A_detectionSizeSupport: bool = False
    A_accuracySupport: bool = False
    A_detectionThreatLevelSupport: bool = False
    A_setDetectorStateSupport: bool = False
    A_videoDetectorSupport: bool = False
    A_snapshotSupport: bool = False
    A_rfSupport: bool = False
    A_maxNumberOfDetectionLocations: idl.int16 = 0
    A_inertialLocationSupport: bool = False

P_Tactical_Sensor_PSM.C_Tactical_Sensor_Specification = P_Tactical_Sensor_PSM_C_Tactical_Sensor_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_sensorCurrentStatus': [idl.id(219859602), ],
        'A_falseAlarmProbability': [idl.id(3141405), ],
        'A_detectionProbability': [idl.id(229637417), ],
        'A_sensitivityLevel': [idl.id(175470000), ],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_sensorCurrentStatus: P_LDM_Common.T_EnabledState = P_LDM_Common.T_EnabledState.L_EnabledState_ENABLED
    A_falseAlarmProbability: float = 0.0
    A_detectionProbability: float = 0.0
    A_sensitivityLevel: Optional[idl.uint8] = None

P_Tactical_Sensor_PSM.C_Tactical_Sensor = P_Tactical_Sensor_PSM_C_Tactical_Sensor

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_Video")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_processedVideoStreams': [idl.id(180732230), idl.bound(10)],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor_Video:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_processedVideoStreams: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)

P_Tactical_Sensor_PSM.C_Tactical_Sensor_Video = P_Tactical_Sensor_PSM_C_Tactical_Sensor_Video

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_detectionUniqueID': [idl.key, idl.id(246744424), ],
        'A_confidence': [idl.id(136595483), ],
        'A_detectionClassification': [idl.id(85099305), ],
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
        'A_designatedInfo': [idl.id(44045387), ],
        'A_numberOfDetectionMethods': [idl.id(165807565), ],
        'A_detectionMethods': [idl.id(87615255), idl.bound(32)],
        'A_snapshotAvailable': [idl.id(149581014), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_detectionUniqueID: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_confidence: float = 0.0
    A_detectionClassification: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_detectionClassScore: float = 0.0
    A_detectionForceType: P_Tactical_Sensor_PSM.T_IFFCategory = P_Tactical_Sensor_PSM.T_IFFCategory.L_IFFCategory_UNKNOWN
    A_detectionThreatStatus: P_Tactical_Sensor_PSM.T_EngagementStatus = P_Tactical_Sensor_PSM.T_EngagementStatus.L_EngagementStatus_UNKNOWN
    A_interception: P_Tactical_Sensor_PSM.T_Interception = P_Tactical_Sensor_PSM.T_Interception.L_Interception_UNKNOWN
    A_detectionStatus: P_Tactical_Sensor_PSM.T_DetectionState = P_Tactical_Sensor_PSM.T_DetectionState.L_DetectionState_NONE
    A_type: P_Tactical_Sensor_PSM.T_DetectionType = P_Tactical_Sensor_PSM.T_DetectionType.L_DetectionType_DETECTION
    A_lifeSpan: P_LDM_Common.T_Duration = field(default_factory = P_LDM_Common.T_Duration)
    A_priority: idl.int16 = 0
    A_trajectoryType: P_Tactical_Sensor_PSM.T_Trajectory = P_Tactical_Sensor_PSM.T_Trajectory.L_Trajectory_UNKNOWN
    A_method: Sequence[P_Tactical_Sensor_PSM.T_Sensing_Method] = field(default_factory = list)
    A_spatialParametersAvailable: bool = False
    A_spatialInfo: P_Tactical_Sensor_PSM.T_Spatial_Info = field(default_factory = P_Tactical_Sensor_PSM.T_Spatial_Info)
    A_suspensionCause: P_Tactical_Sensor_PSM.T_SuspensionCause = P_Tactical_Sensor_PSM.T_SuspensionCause.L_SuspensionCause_NOT_SUSPENDED
    A_designatedInfo: Optional[P_LDM_Common.T_ShortString] = None
    A_numberOfDetectionMethods: Optional[idl.uint8] = None
    A_detectionMethods: Optional[Sequence[P_Tactical_Sensor_PSM.T_DetectingMethod]] = None
    A_snapshotAvailable: bool = False

P_Tactical_Sensor_PSM.C_Detection = P_Tactical_Sensor_PSM_C_Detection

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Merged")],
    member_annotations = {
        'A_sourceDetectionsID': [idl.id(119014851), idl.bound(100)],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Merged(P_Tactical_Sensor_PSM.C_Detection):
    A_sourceDetectionsID: Sequence[P_Tactical_Sensor_PSM.T_Detection_Unique_Id] = field(default_factory = list)

P_Tactical_Sensor_PSM.C_Detection_Merged = P_Tactical_Sensor_PSM_C_Detection_Merged

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Split")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_newDetectionsID': [idl.id(265177457), idl.bound(100)],
        'A_sourceDetectionsID': [idl.id(119014851), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Split:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_newDetectionsID: Sequence[P_Tactical_Sensor_PSM.T_Detection_Unique_Id] = field(default_factory = list)
    A_sourceDetectionsID: P_Tactical_Sensor_PSM.T_Detection_Unique_Id = field(default_factory = P_Tactical_Sensor_PSM.T_Detection_Unique_Id)

P_Tactical_Sensor_PSM.C_Detection_Split = P_Tactical_Sensor_PSM_C_Detection_Split

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Radar")],
    member_annotations = {
        'A_detectionMode': [idl.id(82681813), ],
        'A_seniority': [idl.id(265400507), ],
        'A_snr': [idl.id(62025231), ],
        'A_rcs': [idl.id(80690941), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Radar(P_Tactical_Sensor_PSM.C_Detection):
    A_detectionMode: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_seniority: idl.int32 = 0
    A_snr: float = 0.0
    A_rcs: float = 0.0

P_Tactical_Sensor_PSM.C_Detection_Radar = P_Tactical_Sensor_PSM_C_Detection_Radar

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Optronics")],
    member_annotations = {
        'A_opticalErrorRadius': [idl.id(38790974), ],
        'A_absoluteDirectionAvailable': [idl.id(57211100), ],
        'A_sensorLOS': [idl.id(139547978), ],
        'A_sensorLOSAccuracy': [idl.id(254391707), ],
        'A_videoDataAvailable': [idl.id(35928540), ],
        'A_videoStreamSourceID': [idl.id(152966567), ],
        'A_detectionCenterVideoLocation': [idl.id(83507131), ],
        'A_detectionSizeOnVideo': [idl.id(99643024), ],
        'A_detectionVideoAccuracy': [idl.id(216440692), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Optronics(P_Tactical_Sensor_PSM.C_Detection):
    A_opticalErrorRadius: float = 0.0
    A_absoluteDirectionAvailable: bool = False
    A_sensorLOS: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_sensorLOSAccuracy: P_LDM_Common.T_CoordinatePolar3D = field(default_factory = P_LDM_Common.T_CoordinatePolar3D)
    A_videoDataAvailable: bool = False
    A_videoStreamSourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_detectionCenterVideoLocation: P_LDM_Common.T_VideoPosition = field(default_factory = P_LDM_Common.T_VideoPosition)
    A_detectionSizeOnVideo: P_LDM_Common.T_VideoPosition = field(default_factory = P_LDM_Common.T_VideoPosition)
    A_detectionVideoAccuracy: P_LDM_Common.T_VideoPosition = field(default_factory = P_LDM_Common.T_VideoPosition)

P_Tactical_Sensor_PSM.C_Detection_Optronics = P_Tactical_Sensor_PSM_C_Detection_Optronics

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Aps")],
    member_annotations = {
        'A_timeToGo': [idl.id(16001726), ],
        'A_affecting': [idl.id(63400329), ],
        'A_threatFamily': [idl.id(71472818), ],
        'A_threatAronlod': [idl.id(38827912), ],
        'A_actionStatus': [idl.id(170861292), ],
        'A_threatHitPoint': [idl.id(27758138), ],
        'A_threatRefinementInfo': [idl.id(140347192), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Aps(P_Tactical_Sensor_PSM.C_Detection):
    A_timeToGo: P_LDM_Common.T_Duration = field(default_factory = P_LDM_Common.T_Duration)
    A_affecting: bool = False
    A_threatFamily: P_Tactical_Sensor_PSM.T_ThreatFamily = P_Tactical_Sensor_PSM.T_ThreatFamily.L_ThreatFamily_UNKNOWN
    A_threatAronlod: Optional[P_Tactical_Sensor_PSM.T_AronlodThreat] = None
    A_actionStatus: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_threatHitPoint: P_LDM_Common.T_Coordinate3D = field(default_factory = P_LDM_Common.T_Coordinate3D)
    A_threatRefinementInfo: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Tactical_Sensor_PSM.C_Detection_Aps = P_Tactical_Sensor_PSM_C_Detection_Aps

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_ElectronicWarfare")],
    member_annotations = {
        'A_tbdField': [idl.id(267696504), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_ElectronicWarfare(P_Tactical_Sensor_PSM.C_Detection):
    A_tbdField: idl.int16 = 0

P_Tactical_Sensor_PSM.C_Detection_ElectronicWarfare = P_Tactical_Sensor_PSM_C_Detection_ElectronicWarfare

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Snapshot")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_detectionUniqueID': [idl.key, idl.id(246744424), ],
        'A_snapshotID': [idl.id(189009430), ],
        'A_format': [idl.id(2118290), ],
        'A_snapshot': [idl.id(162825686), idl.bound(4096)],
    }
)
class P_Tactical_Sensor_PSM_C_Snapshot:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_detectionUniqueID: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_snapshotID: idl.uint64 = 0
    A_format: P_LDM_Common.T_VeryShortString = field(default_factory = P_LDM_Common.T_VeryShortString)
    A_snapshot: Sequence[idl.uint8] = field(default_factory = idl.array_factory(idl.uint8))

P_Tactical_Sensor_PSM.C_Snapshot = P_Tactical_Sensor_PSM_C_Snapshot

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_C4I")],
    member_annotations = {
        'A_reportedPolygon': [idl.id(262049984), ],
        'A_idC4i': [idl.id(223406803), ],
        'A_polygonType': [idl.id(109888991), ],
        'A_incrimination': [idl.id(92419651), ],
        'A_inTraining': [idl.id(225415504), ],
        'A_missionContext': [idl.id(126027143), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_C4I(P_Tactical_Sensor_PSM.C_Detection):
    A_reportedPolygon: P_Tactical_Sensor_PSM.T_Polygon_Point = field(default_factory = P_Tactical_Sensor_PSM.T_Polygon_Point)
    A_idC4i: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_polygonType: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_incrimination: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_inTraining: bool = False
    A_missionContext: P_LDM_Common.T_RegularString = field(default_factory = P_LDM_Common.T_RegularString)

P_Tactical_Sensor_PSM.C_Detection_C4I = P_Tactical_Sensor_PSM_C_Detection_C4I

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Detection_Fusion")],
    member_annotations = {
        'A_detectionFusedUniqueID': [idl.id(188817672), ],
        'A_polygon': [idl.id(107617462), ],
    }
)
class P_Tactical_Sensor_PSM_C_Detection_Fusion(P_Tactical_Sensor_PSM.C_Detection):
    A_detectionFusedUniqueID: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_polygon: P_Tactical_Sensor_PSM.T_Fusion_Polygon = field(default_factory = P_Tactical_Sensor_PSM.T_Fusion_Polygon)

P_Tactical_Sensor_PSM.C_Detection_Fusion = P_Tactical_Sensor_PSM_C_Detection_Fusion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_C4I_Entity")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_entityUniqueID': [idl.key, idl.id(251199110), ],
        'A_entityClassification': [idl.id(216803846), ],
        'A_entityForceType': [idl.id(197087151), ],
        'A_entityThreatStatus': [idl.id(257735410), ],
        'A_interception': [idl.id(115597617), ],
        'A_entityStatus': [idl.id(59801362), ],
        'A_method': [idl.id(21615206), idl.bound(15)],
        'A_designatedInfo': [idl.id(44045387), ],
        'A_numberOfDetectionMethods': [idl.id(165807565), ],
        'A_entityMethods': [idl.id(217364402), idl.bound(32)],
        'A_reportedPolygon': [idl.id(262049984), idl.bound(300)],
        'A_numberOfPoints': [idl.id(151879854), ],
        'A_idC4i': [idl.id(223406803), ],
        'A_polygonType': [idl.id(109888991), ],
        'A_incrimination': [idl.id(92419651), ],
        'A_inTraining': [idl.id(225415504), ],
        'A_missionContext': [idl.id(126027143), ],
    }
)
class P_Tactical_Sensor_PSM_C_C4I_Entity:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_entityUniqueID: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_entityClassification: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_entityForceType: P_Tactical_Sensor_PSM.T_IFFCategory = P_Tactical_Sensor_PSM.T_IFFCategory.L_IFFCategory_UNKNOWN
    A_entityThreatStatus: P_Tactical_Sensor_PSM.T_EngagementStatus = P_Tactical_Sensor_PSM.T_EngagementStatus.L_EngagementStatus_UNKNOWN
    A_interception: P_Tactical_Sensor_PSM.T_Interception = P_Tactical_Sensor_PSM.T_Interception.L_Interception_UNKNOWN
    A_entityStatus: P_Tactical_Sensor_PSM.T_DetectionState = P_Tactical_Sensor_PSM.T_DetectionState.L_DetectionState_NONE
    A_method: Sequence[P_Tactical_Sensor_PSM.T_Sensing_Method] = field(default_factory = list)
    A_designatedInfo: Optional[P_LDM_Common.T_ShortString] = None
    A_numberOfDetectionMethods: Optional[idl.uint8] = None
    A_entityMethods: Optional[Sequence[P_Tactical_Sensor_PSM.T_DetectingMethod]] = None
    A_reportedPolygon: Optional[Sequence[P_Tactical_Sensor_PSM.T_Polygon_Point]] = None
    A_numberOfPoints: idl.uint16 = 0
    A_idC4i: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_polygonType: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_incrimination: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)
    A_inTraining: bool = False
    A_missionContext: P_LDM_Common.T_RegularString = field(default_factory = P_LDM_Common.T_RegularString)

P_Tactical_Sensor_PSM.C_C4I_Entity = P_Tactical_Sensor_PSM_C_C4I_Entity

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_Enable_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_detectorType': [idl.id(81702893), idl.bound(15)],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor_Enable_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_detectorType: Sequence[P_LDM_Common.T_ShortString] = field(default_factory = list)

P_Tactical_Sensor_PSM.C_Tactical_Sensor_Enable_Cmd = P_Tactical_Sensor_PSM_C_Tactical_Sensor_Enable_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_Disable_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_module': [idl.id(150492439), idl.bound(15)],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor_Disable_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_module: Sequence[P_LDM_Common.T_ShortString] = field(default_factory = list)

P_Tactical_Sensor_PSM.C_Tactical_Sensor_Disable_Cmd = P_Tactical_Sensor_PSM_C_Tactical_Sensor_Disable_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_AssignVideoStream_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_assignedVideoStreams': [idl.id(115399980), idl.bound(10)],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor_AssignVideoStream_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_assignedVideoStreams: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)

P_Tactical_Sensor_PSM.C_Tactical_Sensor_AssignVideoStream_Cmd = P_Tactical_Sensor_PSM_C_Tactical_Sensor_AssignVideoStream_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_Sector_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_azimuthCenter': [idl.id(246239774), ],
        'A_azimuthWidth': [idl.id(85900094), ],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor_Sector_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_azimuthCenter: float = 0.0
    A_azimuthWidth: float = 0.0

P_Tactical_Sensor_PSM.C_Tactical_Sensor_Sector_Cmd = P_Tactical_Sensor_PSM_C_Tactical_Sensor_Sector_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensitivity_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_level': [idl.id(99784018), ],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensitivity_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_level: idl.uint8 = 0

P_Tactical_Sensor_PSM.C_Tactical_Sensitivity_Cmd = P_Tactical_Sensor_PSM_C_Tactical_Sensitivity_Cmd
