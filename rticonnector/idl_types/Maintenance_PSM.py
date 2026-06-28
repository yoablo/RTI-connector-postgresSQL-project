# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Maintenance_PSM.idl
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

P_Maintenance_PSM = idl.get_module("P_Maintenance_PSM")

P_Maintenance_PSM_T_ErrorID = idl.uint16

P_Maintenance_PSM.T_ErrorID = P_Maintenance_PSM_T_ErrorID


@idl.enum
class P_Maintenance_PSM_T_ErrorState(IntEnum):
    L_ErrorState_EXISTS = 0
    L_ErrorState_VANISHED = 1
    L_ErrorState_REPEATED = 2
    L_ErrorState_NOT_EXIST = 3


P_Maintenance_PSM.T_ErrorState = P_Maintenance_PSM_T_ErrorState


@idl.enum
class P_Maintenance_PSM_T_AcknowledgementType(IntEnum):
    L_AcknowledgementType_ACCEPTED = 0
    L_AcknowledgementType_REJECTED = 1
    L_AcknowledgementType_POSTPONED = 2
    L_AcknowledgementType_CANCELED = 3


P_Maintenance_PSM.T_AcknowledgementType = P_Maintenance_PSM_T_AcknowledgementType


@idl.enum
class P_Maintenance_PSM_T_AlertCategory(IntEnum):
    L_AlertCategory_INFO = 0
    L_AlertCategory_WARNING = 1
    L_AlertCategory_EMERGENCY = 2


P_Maintenance_PSM.T_AlertCategory = P_Maintenance_PSM_T_AlertCategory


@idl.enum
class P_Maintenance_PSM_T_SafetyMode(IntEnum):
    L_SafetyMode_SAFE = 0
    L_SafetyMode_ARMED = 1


P_Maintenance_PSM.T_SafetyMode = P_Maintenance_PSM_T_SafetyMode


@idl.enum
class P_Maintenance_PSM_T_OperationalStates(IntEnum):
    L_OperationalStates_OPERATION = 0
    L_OperationalStates_SIMULATION = 1
    L_OperationalStates_BURNING = 2
    L_OperationalStates_INITIALIZATION = 3
    L_OperationalStates_FAULT = 4
    L_OperationalStates_MAINTENANCE = 5
    L_OperationalStates_TECH_LEVEL = 6
    L_OperationalStates_STANDBY = 7
    L_OperationalStates_UNKNOWN = 8


P_Maintenance_PSM.T_OperationalStates = P_Maintenance_PSM_T_OperationalStates


@idl.enum
class P_Maintenance_PSM_T_CalibrationMode(IntEnum):
    L_CalibrationMode_OPTRONICS = 0
    L_CalibrationMode_APS = 1
    L_CalibrationMode_OTHER = 2


P_Maintenance_PSM.T_CalibrationMode = P_Maintenance_PSM_T_CalibrationMode


@idl.enum
class P_Maintenance_PSM_T_MaintenanceMode(IntEnum):
    L_MaintenanceMode_IBIT = 0
    L_MaintenanceMode_SYS_CALIB = 1
    L_MaintenanceMode_GO_DEFAULT = 2


P_Maintenance_PSM.T_MaintenanceMode = P_Maintenance_PSM_T_MaintenanceMode


@idl.enum
class P_Maintenance_PSM_T_ModulePropriety(IntEnum):
    L_ModulePropriety_PROPER = 0
    L_ModulePropriety_FAULTY = 1
    L_ModulePropriety_NOT_EXIST = 2
    L_ModulePropriety_DEGRADED = 3


P_Maintenance_PSM.T_ModulePropriety = P_Maintenance_PSM_T_ModulePropriety


@idl.enum
class P_Maintenance_PSM_T_MaintenanceOperation(IntEnum):
    L_MaintenanceOperation_IBIT = 0
    L_MaintenanceOperation_SYS_CALIB = 1
    L_MaintenanceOperation_GO_DEFAULT = 2
    L_MaintenanceOperation_IBIT_REPORT_REQ = 3
    L_MaintenanceOperation_GET_OPERATION_DATES = 4
    L_MaintenanceOperation_CALIB_VALIDATION = 5


P_Maintenance_PSM.T_MaintenanceOperation = P_Maintenance_PSM_T_MaintenanceOperation


@idl.enum
class P_Maintenance_PSM_T_Action(IntEnum):
    L_Action_START = 0
    L_Action_ABORT = 1
    L_Action_RETRY = 2
    L_Action_CONTINUE = 3


P_Maintenance_PSM.T_Action = P_Maintenance_PSM_T_Action


@idl.enum
class P_Maintenance_PSM_T_OperationStatus(IntEnum):
    L_OperationStatus_SUCCESS = 0
    L_OperationStatus_FAIL = 1
    L_OperationStatus_WAITING = 2
    L_OperationStatus_IN_PROGRESS = 3


P_Maintenance_PSM.T_OperationStatus = P_Maintenance_PSM_T_OperationStatus


@idl.enum
class P_Maintenance_PSM_T_SafetyLevel(IntEnum):
    L_SafetyLevel_NONE = 0
    L_SafetyLevel_WARNNING = 1
    L_SafetyLevel_DANGER = 2


P_Maintenance_PSM.T_SafetyLevel = P_Maintenance_PSM_T_SafetyLevel


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::T_Error")],
    member_annotations={
        "A_status": [
            idl.id(207505413),
        ],
        "A_description": [
            idl.id(133777518),
        ],
        "A_priority": [
            idl.id(261701171),
        ],
    },
)
class P_Maintenance_PSM_T_Error:
    A_status: P_Maintenance_PSM.T_ErrorState = (
        P_Maintenance_PSM.T_ErrorState.L_ErrorState_EXISTS
    )
    A_description: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_priority: idl.uint16 = 0


P_Maintenance_PSM.T_Error = P_Maintenance_PSM_T_Error


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::T_OperationDate")],
    member_annotations={
        "A_operation": [
            idl.id(127010964),
        ],
        "A_date": [
            idl.id(153874871),
        ],
        "A_status": [
            idl.id(207505413),
        ],
    },
)
class P_Maintenance_PSM_T_OperationDate:
    A_operation: P_Maintenance_PSM.T_MaintenanceOperation = (
        P_Maintenance_PSM.T_MaintenanceOperation.L_MaintenanceOperation_IBIT
    )
    A_date: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)
    A_status: P_Maintenance_PSM.T_OperationStatus = (
        P_Maintenance_PSM.T_OperationStatus.L_OperationStatus_SUCCESS
    )


P_Maintenance_PSM.T_OperationDate = P_Maintenance_PSM_T_OperationDate


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::T_ComponentVersion"),
    ],
    member_annotations={
        "A_componentName": [
            idl.id(29316198),
        ],
        "A_version": [
            idl.id(10701666),
        ],
    },
)
class P_Maintenance_PSM_T_ComponentVersion:
    A_componentName: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_version: P_LDM_Common.T_Version = field(default_factory=P_LDM_Common.T_Version)


P_Maintenance_PSM.T_ComponentVersion = P_Maintenance_PSM_T_ComponentVersion


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::T_ComponentRotationalOffset"),
    ],
    member_annotations={
        "A_componentDescription": [
            idl.id(249926398),
        ],
        "A_rotationalOffset": [
            idl.id(110560446),
        ],
    },
)
class P_Maintenance_PSM_T_ComponentRotationalOffset:
    A_componentDescription: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_rotationalOffset: P_LDM_Common.T_RotationalOffset = field(
        default_factory=P_LDM_Common.T_RotationalOffset
    )


P_Maintenance_PSM.T_ComponentRotationalOffset = (
    P_Maintenance_PSM_T_ComponentRotationalOffset
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Resource_Specification"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_resourceTypeName": [
            idl.id(78356829),
        ],
        "A_descriptor": [
            idl.id(52732520),
        ],
        "A_creationDate": [
            idl.id(194068903),
        ],
        "A_restorationDate": [
            idl.id(158268010),
        ],
        "A_softwareUpdateDate": [
            idl.id(264688042),
        ],
        "A_hardwareUpdateDate": [
            idl.id(228270743),
        ],
        "A_companyCode": [
            idl.id(74190848),
        ],
        "A_restorerCode": [
            idl.id(111274484),
        ],
        "A_projectCode": [
            idl.id(202378202),
        ],
        "A_totalOpTime": [
            idl.id(259762017),
        ],
        "A_softwareVersion": [
            idl.id(240315737),
        ],
        "A_hardwareVersion": [
            idl.id(200278849),
        ],
        "A_catalogCode": [
            idl.id(211890284),
        ],
        "A_serialNumber": [
            idl.id(57564667),
        ],
        "A_includedSoftwareSourceID": [idl.id(45603233), idl.bound(5)],
    },
)
class P_Maintenance_PSM_C_Resource_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_resourceTypeName: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_descriptor: P_LDM_Common.T_LongString = field(
        default_factory=P_LDM_Common.T_LongString
    )
    A_creationDate: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_restorationDate: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_softwareUpdateDate: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_hardwareUpdateDate: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_companyCode: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_restorerCode: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_projectCode: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_totalOpTime: P_LDM_Common.T_Duration = field(
        default_factory=P_LDM_Common.T_Duration
    )
    A_softwareVersion: P_LDM_Common.T_Version = field(
        default_factory=P_LDM_Common.T_Version
    )
    A_hardwareVersion: P_LDM_Common.T_Version = field(
        default_factory=P_LDM_Common.T_Version
    )
    A_catalogCode: P_LDM_Common.T_VeryShortString = field(
        default_factory=P_LDM_Common.T_VeryShortString
    )
    A_serialNumber: P_LDM_Common.T_VeryShortString = field(
        default_factory=P_LDM_Common.T_VeryShortString
    )
    A_includedSoftwareSourceID: Sequence[P_LDM_Common.T_Identifier] = field(
        default_factory=list
    )


P_Maintenance_PSM.C_Resource_Specification = P_Maintenance_PSM_C_Resource_Specification


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::C_Error_Report")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_errorID": [
            idl.key,
            idl.id(114815591),
        ],
        "A_errorData": [
            idl.id(114687765),
        ],
    },
)
class P_Maintenance_PSM_C_Error_Report:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_errorID: idl.uint32 = 0
    A_errorData: P_Maintenance_PSM.T_Error = field(
        default_factory=P_Maintenance_PSM.T_Error
    )


P_Maintenance_PSM.C_Error_Report = P_Maintenance_PSM_C_Error_Report


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_SystemTime_Update"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_time": [
            idl.id(234800211),
        ],
    },
)
class P_Maintenance_PSM_C_SystemTime_Update:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_time: P_LDM_Common.T_DateTime = field(default_factory=P_LDM_Common.T_DateTime)


P_Maintenance_PSM.C_SystemTime_Update = P_Maintenance_PSM_C_SystemTime_Update


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::C_Alert_Report")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_alertID": [
            idl.key,
            idl.id(232587608),
        ],
        "A_alertData": [
            idl.id(195394565),
        ],
        "A_category": [
            idl.id(237999199),
        ],
    },
)
class P_Maintenance_PSM_C_Alert_Report:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_alertID: idl.uint32 = 0
    A_alertData: P_Maintenance_PSM.T_Error = field(
        default_factory=P_Maintenance_PSM.T_Error
    )
    A_category: P_Maintenance_PSM.T_AlertCategory = (
        P_Maintenance_PSM.T_AlertCategory.L_AlertCategory_INFO
    )


P_Maintenance_PSM.C_Alert_Report = P_Maintenance_PSM_C_Alert_Report


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::C_System_State")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_state": [
            idl.id(90057368),
        ],
    },
)
class P_Maintenance_PSM_C_System_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_state: P_Maintenance_PSM.T_OperationalStates = (
        P_Maintenance_PSM.T_OperationalStates.L_OperationalStates_OPERATION
    )


P_Maintenance_PSM.C_System_State = P_Maintenance_PSM_C_System_State


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::C_Module_Status")],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_moduleName": [
            idl.id(224125214),
        ],
        "A_status": [
            idl.id(207505413),
        ],
        "A_fieldID": [
            idl.id(191725964),
        ],
    },
)
class P_Maintenance_PSM_C_Module_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_moduleName: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_status: P_Maintenance_PSM.T_ModulePropriety = (
        P_Maintenance_PSM.T_ModulePropriety.L_ModulePropriety_PROPER
    )
    A_fieldID: Optional[idl.uint32] = None


P_Maintenance_PSM.C_Module_Status = P_Maintenance_PSM_C_Module_Status


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Maintenance_Operation_Response"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_maintOperation": [
            idl.id(267210651),
        ],
        "A_operationStatus": [
            idl.id(87817366),
        ],
        "A_reason": [
            idl.id(244844774),
        ],
        "A_progress": [
            idl.id(4719679),
        ],
    },
)
class P_Maintenance_PSM_C_Maintenance_Operation_Response:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_maintOperation: P_Maintenance_PSM.T_MaintenanceOperation = (
        P_Maintenance_PSM.T_MaintenanceOperation.L_MaintenanceOperation_IBIT
    )
    A_operationStatus: P_Maintenance_PSM.T_OperationStatus = (
        P_Maintenance_PSM.T_OperationStatus.L_OperationStatus_SUCCESS
    )
    A_reason: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_progress: idl.int16 = 0


P_Maintenance_PSM.C_Maintenance_Operation_Response = (
    P_Maintenance_PSM_C_Maintenance_Operation_Response
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Maintenance_Operation_Dates"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_numberOfOperations": [
            idl.id(174958052),
        ],
        "A_operationDates": [idl.id(23184982), idl.bound(255)],
    },
)
class P_Maintenance_PSM_C_Maintenance_Operation_Dates:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_numberOfOperations: idl.uint8 = 0
    A_operationDates: Sequence[P_Maintenance_PSM.T_OperationDate] = field(
        default_factory=list
    )


P_Maintenance_PSM.C_Maintenance_Operation_Dates = (
    P_Maintenance_PSM_C_Maintenance_Operation_Dates
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Resource_Specification_Extended"),
    ],
    member_annotations={
        "A_softwareSubversions": [idl.id(74368763), idl.bound(30)],
        "A_hardwareSubversions": [idl.id(206306151), idl.bound(30)],
    },
)
class P_Maintenance_PSM_C_Resource_Specification_Extended(
    P_Maintenance_PSM.C_Resource_Specification
):
    A_softwareSubversions: Sequence[P_Maintenance_PSM.T_ComponentVersion] = field(
        default_factory=list
    )
    A_hardwareSubversions: Sequence[P_Maintenance_PSM.T_ComponentVersion] = field(
        default_factory=list
    )


P_Maintenance_PSM.C_Resource_Specification_Extended = (
    P_Maintenance_PSM_C_Resource_Specification_Extended
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Alert_Report_Extended"),
    ],
    member_annotations={
        "A_reportedEntity": [
            idl.id(40946440),
        ],
        "A_safetyIndication": [
            idl.id(195320259),
        ],
        "A_report": [
            idl.id(17868329),
        ],
    },
)
class P_Maintenance_PSM_C_Alert_Report_Extended(P_Maintenance_PSM.C_Alert_Report):
    A_reportedEntity: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_safetyIndication: P_Maintenance_PSM.T_SafetyLevel = (
        P_Maintenance_PSM.T_SafetyLevel.L_SafetyLevel_NONE
    )
    A_report: P_LDM_Common.T_LongString = field(
        default_factory=P_LDM_Common.T_LongString
    )


P_Maintenance_PSM.C_Alert_Report_Extended = P_Maintenance_PSM_C_Alert_Report_Extended


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Error_Report_Extended"),
    ],
    member_annotations={
        "A_reportedEntity": [
            idl.id(40946440),
        ],
        "A_safetyIndication": [
            idl.id(195320259),
        ],
        "A_transcript": [
            idl.id(130272259),
        ],
    },
)
class P_Maintenance_PSM_C_Error_Report_Extended(P_Maintenance_PSM.C_Error_Report):
    A_reportedEntity: P_LDM_Common.T_ShortString = field(
        default_factory=P_LDM_Common.T_ShortString
    )
    A_safetyIndication: P_Maintenance_PSM.T_SafetyLevel = (
        P_Maintenance_PSM.T_SafetyLevel.L_SafetyLevel_NONE
    )
    A_transcript: P_LDM_Common.T_LongString = field(
        default_factory=P_LDM_Common.T_LongString
    )


P_Maintenance_PSM.C_Error_Report_Extended = P_Maintenance_PSM_C_Error_Report_Extended


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Rotational_Installation_Offsets"),
    ],
    member_annotations={
        "A_sourceID": [
            idl.key,
            idl.id(118386796),
        ],
        "A_timeOfDataGeneration": [
            idl.id(234062147),
        ],
        "A_subjectID": [
            idl.key,
            idl.id(28152324),
        ],
        "A_numberOfModules": [
            idl.id(213065396),
        ],
        "A_modulesOffsets": [idl.id(45072203), idl.bound(15)],
    },
)
class P_Maintenance_PSM_C_Rotational_Installation_Offsets:
    A_sourceID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(
        default_factory=P_LDM_Common.T_DateTime
    )
    A_subjectID: P_LDM_Common.T_Identifier = field(
        default_factory=P_LDM_Common.T_Identifier
    )
    A_numberOfModules: idl.uint8 = 0
    A_modulesOffsets: Sequence[P_Maintenance_PSM.T_ComponentRotationalOffset] = field(
        default_factory=list
    )


P_Maintenance_PSM.C_Rotational_Installation_Offsets = (
    P_Maintenance_PSM_C_Rotational_Installation_Offsets
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_RequestIBIT_Cmd"),
    ],
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
    },
)
class P_Maintenance_PSM_C_RequestIBIT_Cmd:
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


P_Maintenance_PSM.C_RequestIBIT_Cmd = P_Maintenance_PSM_C_RequestIBIT_Cmd


@idl.struct(
    type_annotations=[idl.mutable, idl.type_name("P_Maintenance_PSM::C_AlertAck_Cmd")],
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
        "A_alertID": [
            idl.key,
            idl.id(232587608),
        ],
        "A_actorAck": [
            idl.id(43359988),
        ],
    },
)
class P_Maintenance_PSM_C_AlertAck_Cmd:
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
    A_alertID: idl.uint32 = 0
    A_actorAck: P_Maintenance_PSM.T_AcknowledgementType = (
        P_Maintenance_PSM.T_AcknowledgementType.L_AcknowledgementType_ACCEPTED
    )


P_Maintenance_PSM.C_AlertAck_Cmd = P_Maintenance_PSM_C_AlertAck_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_SetCalibrationMode_Cmd"),
    ],
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
        "A_calibrationMode": [
            idl.id(133955208),
        ],
    },
)
class P_Maintenance_PSM_C_SetCalibrationMode_Cmd:
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
    A_calibrationMode: P_Maintenance_PSM.T_CalibrationMode = (
        P_Maintenance_PSM.T_CalibrationMode.L_CalibrationMode_OPTRONICS
    )


P_Maintenance_PSM.C_SetCalibrationMode_Cmd = P_Maintenance_PSM_C_SetCalibrationMode_Cmd


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Set_MaintenanceMode_Cmd"),
    ],
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
        "A_maintenanceMode": [
            idl.id(116800824),
        ],
    },
)
class P_Maintenance_PSM_C_Set_MaintenanceMode_Cmd:
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
    A_maintenanceMode: P_Maintenance_PSM.T_MaintenanceMode = (
        P_Maintenance_PSM.T_MaintenanceMode.L_MaintenanceMode_IBIT
    )


P_Maintenance_PSM.C_Set_MaintenanceMode_Cmd = (
    P_Maintenance_PSM_C_Set_MaintenanceMode_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Maintenance_Operation_Activate_Cmd"),
    ],
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
        "A_operation": [
            idl.id(127010964),
        ],
        "A_action": [
            idl.id(224299759),
        ],
        "A_numberOfModules": [
            idl.id(213065396),
        ],
        "A_modules": [idl.id(151275763), idl.bound(32)],
    },
)
class P_Maintenance_PSM_C_Maintenance_Operation_Activate_Cmd:
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
    A_operation: P_Maintenance_PSM.T_MaintenanceOperation = (
        P_Maintenance_PSM.T_MaintenanceOperation.L_MaintenanceOperation_IBIT
    )
    A_action: P_Maintenance_PSM.T_Action = P_Maintenance_PSM.T_Action.L_Action_START
    A_numberOfModules: idl.uint8 = 0
    A_modules: Sequence[idl.int16] = field(default_factory=idl.array_factory(idl.int16))


P_Maintenance_PSM.C_Maintenance_Operation_Activate_Cmd = (
    P_Maintenance_PSM_C_Maintenance_Operation_Activate_Cmd
)


@idl.struct(
    type_annotations=[
        idl.mutable,
        idl.type_name("P_Maintenance_PSM::C_Set_Operational_State_Cmd"),
    ],
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
        "A_state": [
            idl.id(90057368),
        ],
    },
)
class P_Maintenance_PSM_C_Set_Operational_State_Cmd:
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
    A_state: P_Maintenance_PSM.T_OperationalStates = (
        P_Maintenance_PSM.T_OperationalStates.L_OperationalStates_OPERATION
    )


P_Maintenance_PSM.C_Set_Operational_State_Cmd = (
    P_Maintenance_PSM_C_Set_Operational_State_Cmd
)
