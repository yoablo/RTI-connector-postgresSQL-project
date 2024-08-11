from dataclasses import field
from typing import Sequence, Optional
import rti.idl as idl

from rticonnector.idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet
from rticonnector.idl_types.Detection import P_Tactical_Sensor_PSM as P_Tactical_Sensor_PSM_Object

P_LDM_Common = P_LDM_Common_Objet


@idl.alias(
    annotations=[idl.bound(20), ]
)
class P_LDM_Common_T_ShortString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_ShortString = P_LDM_Common_T_ShortString
P_LDM_Common.T_Descriptor = P_LDM_Common.T_ShortString

P_Tactical_Sensor_PSM = P_Tactical_Sensor_PSM_Object


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor_Specification")],
    member_annotations={
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
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
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
