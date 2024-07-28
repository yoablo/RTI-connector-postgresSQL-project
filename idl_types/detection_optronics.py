from dataclasses import field
from typing import Sequence

import rti.idl as idl
import rti.types as types

from miscellaneousEnum import MiscellaneousEnum
from detection import Detection

@idl.struct
class SensorLOS:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class SensorLOSAccuracy:
    A_elevation: float = 0.0
    A_azimuth: float = 0.0
    A_range: float = 0.0


@idl.struct
class VideoStreamSourceID:
    A_platformId: idl.int32 = 0
    A_systemId: idl.int16 = 0
    A_moduleId: idl.int16 = 0


@idl.struct
class VideoPosition:
    A_verticalPosition: float = 0.0
    A_horizontalPosition: float = 0.0


@idl.struct(
    member_annotations={
        'DDS_sampleInfo': [MiscellaneousEnum.DDS_SAMPLE_INFO]
    }
)
class DetectionOptronics(Detection):
    A_opticalErrorRadius: float = 0.0
    A_absoluteDirectionAvailable: bool = False
    A_sensorLOS: SensorLOS = SensorLOS()
    A_sensorLOSAccuracy: SensorLOSAccuracy = SensorLOSAccuracy()
    A_videoDataAvailable: bool = False
    A_videoStreamSourceID: VideoStreamSourceID = VideoStreamSourceID()
    A_detectionCenterVideoLocation: VideoPosition = VideoPosition()
    A_detectionSizeOnVideo: VideoPosition = VideoPosition()
    A_detectionVideoAccuracy: VideoPosition = VideoPosition()
    DDS_sampleInfo: Sequence[types.char] = field(default_factory=idl.array_factory(types.char))


x = DetectionOptronics
