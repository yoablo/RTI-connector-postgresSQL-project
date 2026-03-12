
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from Video_PSM.idl
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

P_Video_PSM = idl.get_module("P_Video_PSM")

@idl.alias(
    annotations = [idl.bound(20),]
)
class P_Video_PSM_T_FieldOfViewArray:
    value: Sequence[float] = field(default_factory = idl.array_factory(float))

P_Video_PSM.T_FieldOfViewArray = P_Video_PSM_T_FieldOfViewArray

@idl.enum
class P_Video_PSM_T_ContinuousState(IntEnum):
    L_ContinuousState_STATIC = 0
    L_ContinuousState_TRANSITION_UP = 1
    L_ContinuousState_TRANSITION_DOWN = 2

P_Video_PSM.T_ContinuousState = P_Video_PSM_T_ContinuousState

@idl.enum
class P_Video_PSM_T_Polarity(IntEnum):
    L_Polarity_WHITE_HOT = 0
    L_Polarity_BLACK_HOT = 1
    L_Polarity_POL_UNKNOWN = 2

P_Video_PSM.T_Polarity = P_Video_PSM_T_Polarity

@idl.enum
class P_Video_PSM_T_Emphasis(IntEnum):
    L_Emphasis_SCENE_PLUS = 0
    L_Emphasis_SCENE = 1
    L_Emphasis_NEUTRAL = 2
    L_Emphasis_TARGET = 3
    L_Emphasis_TARGET_PLUS = 4
    L_Emphasis_FAILURE = 5
    L_Emphasis_NORMAL = 6
    L_Emphasis_EMPH_A = 7
    L_Emphasis_EMPH_B = 8
    L_Emphasis_EMPH_C = 9
    L_Emphasis_EMPH_D = 10
    L_Emphasis_EMPH_E = 11

P_Video_PSM.T_Emphasis = P_Video_PSM_T_Emphasis

@idl.enum
class P_Video_PSM_T_ReticleColor(IntEnum):
    L_ReticleColor_BRIGHTER = 0
    L_ReticleColor_DARKER = 1
    L_ReticleColor_WHITE = 2
    L_ReticleColor_BLACK = 3

P_Video_PSM.T_ReticleColor = P_Video_PSM_T_ReticleColor

@idl.enum
class P_Video_PSM_T_CalibrationMode(IntEnum):
    L_CalibrationMode_BS = 0
    L_CalibrationMode_LIMITS = 1
    L_CalibrationMode_OTHER = 2

P_Video_PSM.T_CalibrationMode = P_Video_PSM_T_CalibrationMode

@idl.enum
class P_Video_PSM_T_NUC_State(IntEnum):
    L_NUC_State_NOT_DONE = 0
    L_NUC_State_IN_PROGRESS = 1
    L_NUC_State_REQUIRED = 2
    L_NUC_State_ABORTED = 3
    L_NUC_State_COMPLETED = 4
    L_NUC_State_FAILED = 5

P_Video_PSM.T_NUC_State = P_Video_PSM_T_NUC_State

@idl.enum
class P_Video_PSM_T_MediaType(IntEnum):
    L_MediaType_FRAME = 0
    L_MediaType_VIDEO = 1

P_Video_PSM.T_MediaType = P_Video_PSM_T_MediaType

@idl.enum
class P_Video_PSM_T_CaptureMode(IntEnum):
    L_CaptureMode_IDLE = 0
    L_CaptureMode_CAPTURE = 1
    L_CaptureMode_FAILED = 2
    L_CaptureMode_SUCCESS = 3

P_Video_PSM.T_CaptureMode = P_Video_PSM_T_CaptureMode

@idl.enum
class P_Video_PSM_T_ReticleMove(IntEnum):
    L_ReticleMove_UP = 0
    L_ReticleMove_RIGHT = 1
    L_ReticleMove_DOWN = 2
    L_ReticleMove_LEFT = 3
    L_ReticleMove_APPROVE = 4
    L_ReticleMove_DISCARD = 5

P_Video_PSM.T_ReticleMove = P_Video_PSM_T_ReticleMove

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::T_Video_Input")],
    member_annotations = {
        'A_sourceID': [idl.id(118386796), ],
        'A_channelDescription': [idl.id(70585959), ],
    }
)
class P_Video_PSM_T_Video_Input:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_channelDescription: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Video_PSM.T_Video_Input = P_Video_PSM_T_Video_Input

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::T_Video_Output")],
    member_annotations = {
        'A_sourceID': [idl.id(118386796), ],
        'A_displayDescription': [idl.id(184479310), ],
    }
)
class P_Video_PSM_T_Video_Output:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_displayDescription: P_LDM_Common.T_ShortString = field(default_factory = P_LDM_Common.T_ShortString)

P_Video_PSM.T_Video_Output = P_Video_PSM_T_Video_Output

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Source_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_providedVideoStream': [idl.id(32120064), idl.bound(10)],
        'A_videoRoutingSupport': [idl.id(235635679), ],
        'A_turnVideoOnOffSupport': [idl.id(87475786), ],
    }
)
class P_Video_PSM_C_Video_Source_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_providedVideoStream: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_videoRoutingSupport: bool = False
    A_turnVideoOnOffSupport: bool = False

P_Video_PSM.C_Video_Source_Specification = P_Video_PSM_C_Video_Source_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Routing_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_inputVideoChannels': [idl.id(109004885), idl.bound(30)],
        'A_outputVideoChannels': [idl.id(30645112), idl.bound(30)],
    }
)
class P_Video_PSM_C_Video_Routing_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_inputVideoChannels: Sequence[P_Video_PSM.T_Video_Input] = field(default_factory = list)
    A_outputVideoChannels: Sequence[P_Video_PSM.T_Video_Output] = field(default_factory = list)

P_Video_PSM.C_Video_Routing_Specification = P_Video_PSM_C_Video_Routing_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Media_Capture_Service_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_capturedVideoStream': [idl.id(109310280), ],
        'A_captureFrameSupported': [idl.id(14591882), ],
        'A_captureVideoSupported': [idl.id(217319292), ],
        'A_cachedDuration': [idl.id(145225100), ],
    }
)
class P_Video_PSM_C_Media_Capture_Service_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_capturedVideoStream: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_captureFrameSupported: bool = False
    A_captureVideoSupported: bool = False
    A_cachedDuration: idl.uint32 = 0

P_Video_PSM.C_Media_Capture_Service_Specification = P_Video_PSM_C_Media_Capture_Service_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Routing")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_inputVideo': [idl.id(1027070), ],
        'A_outputVideo': [idl.id(124294394), ],
    }
)
class P_Video_PSM_C_Video_Routing:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_inputVideo: P_Video_PSM.T_Video_Input = field(default_factory = P_Video_PSM.T_Video_Input)
    A_outputVideo: P_Video_PSM.T_Video_Output = field(default_factory = P_Video_PSM.T_Video_Output)

P_Video_PSM.C_Video_Routing = P_Video_PSM_C_Video_Routing

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Rtsp")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_uri': [idl.id(39570703), ],
    }
)
class P_Video_PSM_C_Rtsp:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_uri: P_LDM_Common.T_MediumString = field(default_factory = P_LDM_Common.T_MediumString)

P_Video_PSM.C_Rtsp = P_Video_PSM_C_Rtsp

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Stream_Specification")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_rtspSupport': [idl.id(163897032), ],
        'A_zoomSupport': [idl.id(131857587), ],
        'A_focusSupport': [idl.id(83388988), ],
        'A_focusContinuousSupport': [idl.id(190923565), ],
        'A_gainSupport': [idl.id(155128789), ],
        'A_gainContinuousSupport': [idl.id(30143047), ],
        'A_levelSupport': [idl.id(18472892), ],
        'A_levelContinuousSupport': [idl.id(132077521), ],
        'A_polaritySupport': [idl.id(217684417), ],
        'A_emphasisSupport': [idl.id(82789507), ],
        'A_panoramaSupport': [idl.id(160958260), ],
        'A_vmdSupport': [idl.id(197891456), ],
        'A_atrSupport': [idl.id(49667066), ],
        'A_reticleOnVideoSupport': [idl.id(233940577), ],
        'A_reticleColorControlSupport': [idl.id(124485842), ],
        'A_fusionStreamsSupport': [idl.id(37782892), idl.bound(10)],
        'A_markerVisibleSupport': [idl.id(130175417), ],
        'A_digitalImageStablizationSupport': [idl.id(15230058), ],
        'A_nucSupport': [idl.id(154515907), ],
        'A_streamResolution': [idl.id(82728130), ],
        'A_focusAreaSupport': [idl.id(217628054), ],
    }
)
class P_Video_PSM_C_Video_Stream_Specification:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_rtspSupport: bool = False
    A_zoomSupport: bool = False
    A_focusSupport: bool = False
    A_focusContinuousSupport: bool = False
    A_gainSupport: bool = False
    A_gainContinuousSupport: bool = False
    A_levelSupport: bool = False
    A_levelContinuousSupport: bool = False
    A_polaritySupport: bool = False
    A_emphasisSupport: bool = False
    A_panoramaSupport: bool = False
    A_vmdSupport: bool = False
    A_atrSupport: bool = False
    A_reticleOnVideoSupport: bool = False
    A_reticleColorControlSupport: bool = False
    A_fusionStreamsSupport: Sequence[P_LDM_Common.T_Identifier] = field(default_factory = list)
    A_markerVisibleSupport: bool = False
    A_digitalImageStablizationSupport: bool = False
    A_nucSupport: bool = False
    A_streamResolution: P_LDM_Common.T_Resolution = field(default_factory = P_LDM_Common.T_Resolution)
    A_focusAreaSupport: bool = False

P_Video_PSM.C_Video_Stream_Specification = P_Video_PSM_C_Video_Stream_Specification

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Stream_Zoom_Support")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_continuousSupport': [idl.id(85191538), ],
        'A_maximumZoomValue': [idl.id(116739902), ],
        'A_minimumZoomValue': [idl.id(2979867), ],
        'A_discreteFovSupport': [idl.id(152204344), ],
    }
)
class P_Video_PSM_C_Video_Stream_Zoom_Support:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_continuousSupport: bool = False
    A_maximumZoomValue: float = 0.0
    A_minimumZoomValue: float = 0.0
    A_discreteFovSupport: P_Video_PSM.T_FieldOfViewArray = field(default_factory = P_Video_PSM.T_FieldOfViewArray)

P_Video_PSM.C_Video_Stream_Zoom_Support = P_Video_PSM_C_Video_Stream_Zoom_Support

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Zoom")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_zoom': [idl.id(90421831), ],
        'A_fov': [idl.id(201205967), ],
        'A_zoomState': [idl.id(2015899), ],
    }
)
class P_Video_PSM_C_Zoom:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_zoom: float = 0.0
    A_fov: float = 0.0
    A_zoomState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC

P_Video_PSM.C_Zoom = P_Video_PSM_C_Zoom

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Focus")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_focusState': [idl.id(249918844), ],
        'A_focusAutoState': [idl.id(90074730), ],
        'A_focusValue': [idl.id(62995168), ],
        'A_upperBound': [idl.id(255084777), ],
        'A_lowerBound': [idl.id(69335551), ],
    }
)
class P_Video_PSM_C_Focus:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_focusState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC
    A_focusAutoState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_focusValue: float = 0.0
    A_upperBound: bool = False
    A_lowerBound: bool = False

P_Video_PSM.C_Focus = P_Video_PSM_C_Focus

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Polarity")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_polarityState': [idl.id(39317794), ],
    }
)
class P_Video_PSM_C_Polarity:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_polarityState: P_Video_PSM.T_Polarity = P_Video_PSM.T_Polarity.L_Polarity_WHITE_HOT

P_Video_PSM.C_Polarity = P_Video_PSM_C_Polarity

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Stream_Level_Support")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_maximumLevelValue': [idl.id(110005254), ],
        'A_minimumLevelValue': [idl.id(16509416), ],
        'A_stepSize': [idl.id(1540071), ],
    }
)
class P_Video_PSM_C_Video_Stream_Level_Support:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_maximumLevelValue: float = 0.0
    A_minimumLevelValue: float = 0.0
    A_stepSize: float = 0.0

P_Video_PSM.C_Video_Stream_Level_Support = P_Video_PSM_C_Video_Stream_Level_Support

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Level")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_levelState': [idl.id(96505194), ],
        'A_autoLevelState': [idl.id(186342667), ],
        'A_level': [idl.id(99784018), ],
    }
)
class P_Video_PSM_C_Level:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_levelState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC
    A_autoLevelState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_level: float = 0.0

P_Video_PSM.C_Level = P_Video_PSM_C_Level

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Stream_Gain_Support")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_maximumGainValue': [idl.id(241424803), ],
        'A_minimumGainValue': [idl.id(244154142), ],
        'A_stepSize': [idl.id(1540071), ],
    }
)
class P_Video_PSM_C_Video_Stream_Gain_Support:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_maximumGainValue: float = 0.0
    A_minimumGainValue: float = 0.0
    A_stepSize: float = 0.0

P_Video_PSM.C_Video_Stream_Gain_Support = P_Video_PSM_C_Video_Stream_Gain_Support

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Gain")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_gainState': [idl.id(38208831), ],
        'A_autoGainState': [idl.id(140703665), ],
        'A_gain': [idl.id(61276318), ],
    }
)
class P_Video_PSM_C_Gain:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_gainState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC
    A_autoGainState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_gain: float = 0.0

P_Video_PSM.C_Gain = P_Video_PSM_C_Gain

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Emphasis")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_emphasisState': [idl.id(97685341), ],
    }
)
class P_Video_PSM_C_Emphasis:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_emphasisState: P_Video_PSM.T_Emphasis = P_Video_PSM.T_Emphasis.L_Emphasis_SCENE_PLUS

P_Video_PSM.C_Emphasis = P_Video_PSM_C_Emphasis

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Fusion")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fusionState': [idl.id(32288876), ],
        'A_fusionedStream': [idl.key, idl.id(215548769), ],
    }
)
class P_Video_PSM_C_Fusion:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fusionState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_fusionedStream: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Video_PSM.C_Fusion = P_Video_PSM_C_Fusion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Marker_Visible_Mode")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_markerVisibleMode': [idl.id(254955803), ],
    }
)
class P_Video_PSM_C_Marker_Visible_Mode:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_markerVisibleMode: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Marker_Visible_Mode = P_Video_PSM_C_Marker_Visible_Mode

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Digital_Image_Stabilization")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_stabilizationState': [idl.id(7339653), ],
    }
)
class P_Video_PSM_C_Digital_Image_Stabilization:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_stabilizationState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Digital_Image_Stabilization = P_Video_PSM_C_Digital_Image_Stabilization

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Turbulance_State")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_actionRequest': [idl.id(221292372), ],
    }
)
class P_Video_PSM_C_Turbulance_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_actionRequest: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Turbulance_State = P_Video_PSM_C_Turbulance_State

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_On_Video_State")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_reticleOnVideo': [idl.id(47002144), ],
        'A_combinedReticles': [idl.id(124118156), ],
        'A_reticleColor': [idl.id(9266429), ],
    }
)
class P_Video_PSM_C_Reticle_On_Video_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_reticleOnVideo: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_combinedReticles: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON
    A_reticleColor: P_LDM_Common.T_VeryShortString = field(default_factory = P_LDM_Common.T_VeryShortString)

P_Video_PSM.C_Reticle_On_Video_State = P_Video_PSM_C_Reticle_On_Video_State

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_NUC_State")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_streamNUCState': [idl.id(164390981), ],
    }
)
class P_Video_PSM_C_NUC_State:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_streamNUCState: P_Video_PSM.T_NUC_State = P_Video_PSM.T_NUC_State.L_NUC_State_NOT_DONE

P_Video_PSM.C_NUC_State = P_Video_PSM_C_NUC_State

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Stream_Position")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_position': [idl.id(26705633), ],
    }
)
class P_Video_PSM_C_Video_Stream_Position:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_position: P_LDM_Common.T_PixelsVideoPosition = field(default_factory = P_LDM_Common.T_PixelsVideoPosition)

P_Video_PSM.C_Video_Stream_Position = P_Video_PSM_C_Video_Stream_Position

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Stream_Relative_Position")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_deviation': [idl.id(45566643), ],
        'A_fov': [idl.id(201205967), ],
    }
)
class P_Video_PSM_C_Video_Stream_Relative_Position:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_deviation: P_LDM_Common.T_PixelsVideoPosition = field(default_factory = P_LDM_Common.T_PixelsVideoPosition)
    A_fov: float = 0.0

P_Video_PSM.C_Video_Stream_Relative_Position = P_Video_PSM_C_Video_Stream_Relative_Position

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Media_Captured_Event")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_requestGuid': [idl.id(90086053), ],
        'A_mediaType': [idl.id(43505626), ],
        'A_capturedVideoExist': [idl.id(210836835), ],
        'A_captureState': [idl.id(153766323), ],
        'A_mediaPath': [idl.id(233901319), ],
        'A_fileName': [idl.id(11054836), ],
        'A_capturedStreamID': [idl.id(211917065), ],
    }
)
class P_Video_PSM_C_Media_Captured_Event:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_requestGuid: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_mediaType: P_Video_PSM.T_MediaType = P_Video_PSM.T_MediaType.L_MediaType_FRAME
    A_capturedVideoExist: bool = False
    A_captureState: P_Video_PSM.T_CaptureMode = P_Video_PSM.T_CaptureMode.L_CaptureMode_IDLE
    A_mediaPath: P_LDM_Common.T_MediumString = field(default_factory = P_LDM_Common.T_MediumString)
    A_fileName: P_LDM_Common.T_MediumString = field(default_factory = P_LDM_Common.T_MediumString)
    A_capturedStreamID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Video_PSM.C_Media_Captured_Event = P_Video_PSM_C_Media_Captured_Event

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Media_Capture_Service")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_requestGuid': [idl.id(90086053), ],
        'A_currentlyCapturedStreamID': [idl.id(129464831), ],
        'A_workingMode': [idl.id(217274201), ],
        'A_processState': [idl.id(161616526), ],
    }
)
class P_Video_PSM_C_Media_Capture_Service:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_requestGuid: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_currentlyCapturedStreamID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_workingMode: P_Video_PSM.T_CaptureMode = P_Video_PSM.T_CaptureMode.L_CaptureMode_IDLE
    A_processState: P_LDM_Common.T_EnabledState = P_LDM_Common.T_EnabledState.L_EnabledState_ENABLED

P_Video_PSM.C_Media_Capture_Service = P_Video_PSM_C_Media_Capture_Service

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_ATR_Status")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_active': [idl.id(67765464), ],
    }
)
class P_Video_PSM_C_ATR_Status:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_active: bool = False

P_Video_PSM.C_ATR_Status = P_Video_PSM_C_ATR_Status

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_Position")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_position': [idl.id(26705633), ],
    }
)
class P_Video_PSM_C_Reticle_Position:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_position: P_LDM_Common.T_PixelsVideoPosition = field(default_factory = P_LDM_Common.T_PixelsVideoPosition)

P_Video_PSM.C_Reticle_Position = P_Video_PSM_C_Reticle_Position

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Routing_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_inputVideo': [idl.id(1027070), ],
        'A_outputVideo': [idl.id(124294394), ],
    }
)
class P_Video_PSM_C_Video_Routing_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_inputVideo: P_Video_PSM.T_Video_Input = field(default_factory = P_Video_PSM.T_Video_Input)
    A_outputVideo: P_Video_PSM.T_Video_Output = field(default_factory = P_Video_PSM.T_Video_Output)

P_Video_PSM.C_Video_Routing_Cmd = P_Video_PSM_C_Video_Routing_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Zoom_SetFov_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fov': [idl.id(201205967), ],
    }
)
class P_Video_PSM_C_Zoom_SetFov_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fov: float = 0.0

P_Video_PSM.C_Zoom_SetFov_Cmd = P_Video_PSM_C_Zoom_SetFov_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Zoom_SetContinuousZoom_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_zoomState': [idl.id(2015899), ],
    }
)
class P_Video_PSM_C_Zoom_SetContinuousZoom_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_zoomState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC

P_Video_PSM.C_Zoom_SetContinuousZoom_Cmd = P_Video_PSM_C_Zoom_SetContinuousZoom_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Focus_SetAutoState_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_autoState': [idl.id(27783927), ],
    }
)
class P_Video_PSM_C_Focus_SetAutoState_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_autoState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Focus_SetAutoState_Cmd = P_Video_PSM_C_Focus_SetAutoState_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Focus_SetContinuousFocus_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_focusState': [idl.id(249918844), ],
    }
)
class P_Video_PSM_C_Focus_SetContinuousFocus_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_focusState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC

P_Video_PSM.C_Focus_SetContinuousFocus_Cmd = P_Video_PSM_C_Focus_SetContinuousFocus_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Focus_NextFocus_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Focus_NextFocus_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Focus_NextFocus_Cmd = P_Video_PSM_C_Focus_NextFocus_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Focus_PrevFocus_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Focus_PrevFocus_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Focus_PrevFocus_Cmd = P_Video_PSM_C_Focus_PrevFocus_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Polarity_InvertPolarity_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Polarity_InvertPolarity_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Polarity_InvertPolarity_Cmd = P_Video_PSM_C_Polarity_InvertPolarity_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Level_SetAutoState_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_autoState': [idl.id(27783927), ],
    }
)
class P_Video_PSM_C_Level_SetAutoState_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_autoState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Level_SetAutoState_Cmd = P_Video_PSM_C_Level_SetAutoState_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Level_SetContinuousLevel_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_levelState': [idl.id(96505194), ],
    }
)
class P_Video_PSM_C_Level_SetContinuousLevel_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_levelState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC

P_Video_PSM.C_Level_SetContinuousLevel_Cmd = P_Video_PSM_C_Level_SetContinuousLevel_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Level_NudgeLevel_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_numberOfSteps': [idl.id(120556509), ],
    }
)
class P_Video_PSM_C_Level_NudgeLevel_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_numberOfSteps: idl.int32 = 0

P_Video_PSM.C_Level_NudgeLevel_Cmd = P_Video_PSM_C_Level_NudgeLevel_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Gain_SetAutoState_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_autoState': [idl.id(27783927), ],
    }
)
class P_Video_PSM_C_Gain_SetAutoState_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_autoState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Gain_SetAutoState_Cmd = P_Video_PSM_C_Gain_SetAutoState_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Gain_SetContinuousGain_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_gainState': [idl.id(38208831), ],
    }
)
class P_Video_PSM_C_Gain_SetContinuousGain_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_gainState: P_Video_PSM.T_ContinuousState = P_Video_PSM.T_ContinuousState.L_ContinuousState_STATIC

P_Video_PSM.C_Gain_SetContinuousGain_Cmd = P_Video_PSM_C_Gain_SetContinuousGain_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Gain_NudgeGain_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_numberOfSteps': [idl.id(120556509), ],
    }
)
class P_Video_PSM_C_Gain_NudgeGain_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_numberOfSteps: idl.int32 = 0

P_Video_PSM.C_Gain_NudgeGain_Cmd = P_Video_PSM_C_Gain_NudgeGain_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Emphasis_NextEmphasis_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Emphasis_NextEmphasis_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Emphasis_NextEmphasis_Cmd = P_Video_PSM_C_Emphasis_NextEmphasis_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Emphasis_PrevEmphasis_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Emphasis_PrevEmphasis_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Emphasis_PrevEmphasis_Cmd = P_Video_PSM_C_Emphasis_PrevEmphasis_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Panorama_StartPanorama_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_videoStreamID_Ref': [idl.id(22336308), ],
        'A_fov': [idl.id(201205967), ],
        'A_boundaryPoints': [idl.id(30142147), idl.bound(2)],
    }
)
class P_Video_PSM_C_Panorama_StartPanorama_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_videoStreamID_Ref: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_fov: float = 0.0
    A_boundaryPoints: Sequence[P_LDM_Common.T_RotationalPosition] = field(default_factory = list)

P_Video_PSM.C_Panorama_StartPanorama_Cmd = P_Video_PSM_C_Panorama_StartPanorama_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Panorama_StopPanorama_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Panorama_StopPanorama_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Panorama_StopPanorama_Cmd = P_Video_PSM_C_Panorama_StopPanorama_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Source_TurnVideoOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Video_Source_TurnVideoOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Video_Source_TurnVideoOn_Cmd = P_Video_PSM_C_Video_Source_TurnVideoOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Video_Source_TurnVideoOff_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Video_Source_TurnVideoOff_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Video_Source_TurnVideoOff_Cmd = P_Video_PSM_C_Video_Source_TurnVideoOff_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_ATR_TurnOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_ATR_TurnOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_ATR_TurnOn_Cmd = P_Video_PSM_C_ATR_TurnOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_ATR_TurnOff_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_ATR_TurnOff_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_ATR_TurnOff_Cmd = P_Video_PSM_C_ATR_TurnOff_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_VMD_TurnOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_VMD_TurnOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_VMD_TurnOn_Cmd = P_Video_PSM_C_VMD_TurnOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_VMD_TurnOff_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_VMD_TurnOff_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_VMD_TurnOff_Cmd = P_Video_PSM_C_VMD_TurnOff_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Fusion_TurnOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fusionRequestedStream': [idl.id(77118149), ],
    }
)
class P_Video_PSM_C_Fusion_TurnOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fusionRequestedStream: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Video_PSM.C_Fusion_TurnOn_Cmd = P_Video_PSM_C_Fusion_TurnOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Fusion_TurnOff_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_fusionRequestedStream': [idl.id(77118149), ],
    }
)
class P_Video_PSM_C_Fusion_TurnOff_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_fusionRequestedStream: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)

P_Video_PSM.C_Fusion_TurnOff_Cmd = P_Video_PSM_C_Fusion_TurnOff_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Marker_Visible_TurnOn_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Marker_Visible_TurnOn_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Marker_Visible_TurnOn_Cmd = P_Video_PSM_C_Marker_Visible_TurnOn_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Marker_Visible_TurnOff_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Marker_Visible_TurnOff_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Marker_Visible_TurnOff_Cmd = P_Video_PSM_C_Marker_Visible_TurnOff_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_Color_Control_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_reticleRequestedColor': [idl.id(105750328), ],
    }
)
class P_Video_PSM_C_Reticle_Color_Control_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_reticleRequestedColor: P_Video_PSM.T_ReticleColor = P_Video_PSM.T_ReticleColor.L_ReticleColor_BRIGHTER

P_Video_PSM.C_Reticle_Color_Control_Cmd = P_Video_PSM_C_Reticle_Color_Control_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Emphasis_NeutralEmphasis_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Emphasis_NeutralEmphasis_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Emphasis_NeutralEmphasis_Cmd = P_Video_PSM_C_Emphasis_NeutralEmphasis_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Digital_Image_Stabilization_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_imageStateRequest': [idl.id(65037255), ],
    }
)
class P_Video_PSM_C_Digital_Image_Stabilization_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_imageStateRequest: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Digital_Image_Stabilization_Cmd = P_Video_PSM_C_Digital_Image_Stabilization_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Turbulence_Action_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_turbulanceState': [idl.id(91115932), ],
    }
)
class P_Video_PSM_C_Turbulence_Action_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_turbulanceState: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Turbulence_Action_Cmd = P_Video_PSM_C_Turbulence_Action_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_On_Video_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_reticleOnVideo': [idl.id(47002144), ],
    }
)
class P_Video_PSM_C_Reticle_On_Video_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_reticleOnVideo: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Reticle_On_Video_Cmd = P_Video_PSM_C_Reticle_On_Video_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_NUC_Start_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_NUC_Start_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_NUC_Start_Cmd = P_Video_PSM_C_NUC_Start_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Set_Touch_Focus_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_position': [idl.id(26705633), ],
    }
)
class P_Video_PSM_C_Set_Touch_Focus_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_position: P_LDM_Common.T_PixelsVideoPosition = field(default_factory = P_LDM_Common.T_PixelsVideoPosition)

P_Video_PSM.C_Set_Touch_Focus_Cmd = P_Video_PSM_C_Set_Touch_Focus_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Emphasis_SetEmphasis_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_emphasisState': [idl.id(97685341), ],
    }
)
class P_Video_PSM_C_Emphasis_SetEmphasis_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_emphasisState: P_Video_PSM.T_Emphasis = P_Video_PSM.T_Emphasis.L_Emphasis_SCENE_PLUS

P_Video_PSM.C_Emphasis_SetEmphasis_Cmd = P_Video_PSM_C_Emphasis_SetEmphasis_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Capture_Media_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_captureFrame': [idl.id(69860259), ],
        'A_captureVideo': [idl.id(6980627), ],
        'A_requestID': [idl.id(142424133), ],
        'A_selectedVideoStream': [idl.id(206689049), ],
        'A_duration': [idl.id(97018475), ],
    }
)
class P_Video_PSM_C_Capture_Media_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_captureFrame: bool = False
    A_captureVideo: bool = False
    A_requestID: P_LDM_Common.T_Uuid = field(default_factory = P_LDM_Common.T_Uuid)
    A_selectedVideoStream: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_duration: idl.uint32 = 0

P_Video_PSM.C_Capture_Media_Cmd = P_Video_PSM_C_Capture_Media_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_Fix_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_action': [idl.id(224299759), ],
        'A_stepSize': [idl.id(1540071), ],
    }
)
class P_Video_PSM_C_Reticle_Fix_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_action: P_Video_PSM.T_ReticleMove = P_Video_PSM.T_ReticleMove.L_ReticleMove_UP
    A_stepSize: idl.int32 = 0

P_Video_PSM.C_Reticle_Fix_Cmd = P_Video_PSM_C_Reticle_Fix_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_Combine_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_combinedReticles': [idl.id(124118156), ],
    }
)
class P_Video_PSM_C_Reticle_Combine_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_combinedReticles: P_LDM_Common.T_OnOff = P_LDM_Common.T_OnOff.L_OnOff_ON

P_Video_PSM.C_Reticle_Combine_Cmd = P_Video_PSM_C_Reticle_Combine_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_GetPosition_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
    }
)
class P_Video_PSM_C_Reticle_GetPosition_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)

P_Video_PSM.C_Reticle_GetPosition_Cmd = P_Video_PSM_C_Reticle_GetPosition_Cmd

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("P_Video_PSM::C_Reticle_SetColor_Cmd")],
    member_annotations = {
        'A_sourceID': [idl.key, idl.id(118386796), ],
        'A_recipientID': [idl.key, idl.id(214190224), ],
        'A_referenceNum': [idl.id(249600164), ],
        'A_timeOfDataGeneration': [idl.id(234062147), ],
        'A_reticleColor': [idl.id(9266429), ],
    }
)
class P_Video_PSM_C_Reticle_SetColor_Cmd:
    A_sourceID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_recipientID: P_LDM_Common.T_Identifier = field(default_factory = P_LDM_Common.T_Identifier)
    A_referenceNum: idl.int32 = 0
    A_timeOfDataGeneration: P_LDM_Common.T_DateTime = field(default_factory = P_LDM_Common.T_DateTime)
    A_reticleColor: P_LDM_Common.T_VeryShortString = field(default_factory = P_LDM_Common.T_VeryShortString)

P_Video_PSM.C_Reticle_SetColor_Cmd = P_Video_PSM_C_Reticle_SetColor_Cmd
