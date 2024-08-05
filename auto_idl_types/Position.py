from dataclasses import field
import rti.idl as idl

from auto_idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet


P_LDM_Common = P_LDM_Common_Objet
P_Navigation_PSM = idl.get_module("P_Navigation_PSM")


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Navigation_PSM::C_Position")],
    member_annotations={
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_currentPosition': [idl.id(139922608), ],
    }
)
class P_Navigation_PSM_C_Position:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_currentPosition: P_LDM_Common.T_Coordinate3D = field(default_factory=P_LDM_Common.T_Coordinate3D)


P_Navigation_PSM.C_Position = P_Navigation_PSM_C_Position
