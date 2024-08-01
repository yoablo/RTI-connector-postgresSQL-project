import rti.asyncio
import rti.connextdds as dds
from rti import idl

import constants
from Configuration.TopicData import StructEnum, topic_data_dict
from auto_idl_types.DetectionOptronics import P_Tactical_Sensor_PSM_C_Detection_Optronics


class ProfilesExamplePublisher:
    def __init__(self, struct_enum: StructEnum):
        topic_name = topic_data_dict[struct_enum].topic_name
        topic_struct = topic_data_dict[struct_enum].topic_struct
        qos_provider = dds.QosProvider(constants.QOS_PROVIDER)

        self.participant = dds.DomainParticipant(
            constants.DOMAIN_ID, qos_provider.participant_qos
        )
        publisher = dds.Publisher(self.participant, qos_provider.publisher_qos)
        topic = dds.Topic(
            self.participant,
            topic_name,
            topic_struct,
            qos_provider.topic_qos,
        )
        self.writer_default = dds.DataWriter(
            publisher,
            topic,
            qos_provider.datawriter_qos_from_profile(
                constants.PROFILE_NAME
            ),
        )
        self.samples_written = 0

    async def run(self, struct_to_write):
        self.writer_default.write(struct_to_write)


def write(struct_enum: StructEnum, struct_to_write: idl.struct):
    try:
        rti.asyncio.run(ProfilesExamplePublisher(struct_enum).run(struct_to_write))
    except KeyboardInterrupt:
        pass
