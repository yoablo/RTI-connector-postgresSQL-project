from dataclasses import field
from typing import Sequence
import rti.idl as idl

from auto_idl_types.LDM_Common import P_LDM_Common as P_LDM_Common_Objet


P_LDM_Common = P_LDM_Common_Objet


@idl.alias(
    annotations=[idl.bound(10), ]
)
class P_LDM_Common_T_VeryShortString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_VeryShortString = P_LDM_Common_T_VeryShortString


@idl.alias(
    annotations=[idl.bound(20), ]
)
class P_LDM_Common_T_ShortString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_ShortString = P_LDM_Common_T_ShortString


@idl.alias(
    annotations=[idl.bound(500), ]
)
class P_LDM_Common_T_LongString:
    value: Sequence[idl.char] = field(default_factory=idl.array_factory(idl.char))


P_LDM_Common.T_LongString = P_LDM_Common_T_LongString

P_Maintenance_PSM = idl.get_module("P_Maintenance_PSM")


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::C_Resource_Specification")],
    member_annotations={
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_resourceTypeName': [idl.id(78356829), ],
        'A_descriptor': [idl.id(52732520), ],
        'A_creationDate': [idl.id(194068903), ],
        'A_restorationDate': [idl.id(158268010), ],
        'A_softwareUpdateDate': [idl.id(264688042), ],
        'A_hardwareUpdateDate': [idl.id(228270743), ],
        'A_companyCode': [idl.id(74190848), ],
        'A_restorerCode': [idl.id(111274484), ],
        'A_projectCode': [idl.id(202378202), ],
        'A_totalOpTime': [idl.id(259762017), ],
        'A_softwareVersion': [idl.id(240315737), ],
        'A_hardwareVersion': [idl.id(200278849), ],
        'A_catalogCode': [idl.id(211890284), ],
        'A_serialNumber': [idl.id(57564667), ],
        'A_includedSoftwareSourceID': [idl.id(45603233), idl.bound(5)],
    }
)
class P_Maintenance_PSM_C_Resource_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory=P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_resourceTypeName: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)
    A_descriptor: P_LDM_Common.T_LongString = field(default_factory=P_LDM_Common.T_LongString)
    A_creationDate: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_restorationDate: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_softwareUpdateDate: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_hardwareUpdateDate: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_companyCode: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)
    A_restorerCode: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)
    A_projectCode: P_LDM_Common.T_ShortString = field(default_factory=P_LDM_Common.T_ShortString)
    A_totalOpTime: P_LDM_Common.T_Duration = field(default_factory=P_LDM_Common.T_Duration)
    A_softwareVersion: P_LDM_Common.T_Version = field(default_factory=P_LDM_Common.T_Version)
    A_hardwareVersion: P_LDM_Common.T_Version = field(default_factory=P_LDM_Common.T_Version)
    A_catalogCode: P_LDM_Common.T_VeryShortString = field(default_factory=P_LDM_Common.T_VeryShortString)
    A_serialNumber: P_LDM_Common.T_VeryShortString = field(default_factory=P_LDM_Common.T_VeryShortString)
    A_includedSoftwareSourceID: Sequence[P_LDM_Common.T_Identifier] = field(default_factory=list)


P_Maintenance_PSM.C_Resource_Specification = P_Maintenance_PSM_C_Resource_Specification
