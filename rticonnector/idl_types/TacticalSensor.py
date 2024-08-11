from dataclasses import field
from typing import Optional
import rti.idl as idl

from rticonnector.idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet

P_LDM_Common = P_LDM_Common_Objet

P_Tactical_Sensor_PSM = idl.get_module("P_Tactical_Sensor_PSM")


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Tactical_Sensor_PSM::C_Tactical_Sensor")],
    member_annotations={
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_sensorCurrentStatus': [idl.id(219859602), ],
        'A_falseAlarmProbability': [idl.id(3141405), ],
        'A_detectionProbability': [idl.id(229637417), ],
        'A_sensitivityLevel': [idl.id(175470000), ],
    }
)
class P_Tactical_Sensor_PSM_C_Tactical_Sensor:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_sensorCurrentStatus: P_LDM_Common.T_EnabledState = P_LDM_Common.T_EnabledState.L_EnabledState_ENABLED
    A_falseAlarmProbability: float = 0.0
    A_detectionProbability: float = 0.0
    A_sensitivityLevel: Optional[idl.uint8] = None


P_Tactical_Sensor_PSM.C_Tactical_Sensor = P_Tactical_Sensor_PSM_C_Tactical_Sensor
