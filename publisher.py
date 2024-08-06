import rti.asyncio
import rti.connextdds as dds
from rti.idl import struct as idl_struct
from constants import PROFILE_NAME, QOS_PROVIDER, DEFAULT_DOMAIN_ID
from TopicData import StructEnum, topic_data_dict


class Publisher:
    def __init__(self, struct_enum: StructEnum, domain_id: DEFAULT_DOMAIN_ID):
        self.topic_name = topic_data_dict[struct_enum].topic_name
        self.topic_struct = topic_data_dict[struct_enum].topic_struct
        qos_provider = dds.QosProvider(QOS_PROVIDER)

        self.participant = dds.DomainParticipant(
            domain_id, qos_provider.participant_qos
        )
        publisher = dds.Publisher(self.participant, qos_provider.publisher_qos)
        topic = dds.Topic(
            self.participant,
            self.topic_name,
            self.topic_struct,
            qos_provider.topic_qos,
        )
        self.writer_default = dds.DataWriter(
            publisher,
            topic,
            qos_provider.datawriter_qos_from_profile(
                PROFILE_NAME
            ),
        )

    async def __run(self, struct_to_publish: idl_struct):
        self.writer_default.write(struct_to_publish)

    def publish(self, struct_to_publish: idl_struct):
        try:
            rti.asyncio.run(self.__run(struct_to_publish))
        except KeyboardInterrupt:
            pass
