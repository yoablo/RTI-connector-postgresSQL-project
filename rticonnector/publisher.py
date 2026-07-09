import threading
from asyncio import run
from threading import Thread
import rti.connextdds as dds
from rti.idl import struct as idl_struct

from rticonnector.utils import get_qos_file
from rticonnector.constants import PROFILE_NAME, DEFAULT_DOMAIN_ID
from rticonnector.topic_data import TopicEnum, topic_data_dict


class Publisher:
    def __init__(
        self,
        topic_enum: TopicEnum,
        qos_file_path: str = None,
        domain_id=DEFAULT_DOMAIN_ID,
    ):
        self.topic_name = topic_data_dict[topic_enum].topic_name
        self.topic_struct = topic_data_dict[topic_enum].topic_struct
        qos_provider = dds.QosProvider(get_qos_file(qos_file_path))

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
            publisher, topic, qos_provider.datawriter_qos_from_profile(PROFILE_NAME)
        )

    async def __run(self, struct_to_publish: idl_struct):
        self.writer_default.write(struct_to_publish)

    def __publish_thread(self, struct_to_publish: idl_struct):
        run(self.__run(struct_to_publish))

    def publish(self, struct_to_publish: idl_struct):
        publish_thread = Thread(
            target=self.__publish_thread, args=(struct_to_publish,), daemon=True
        )
        publish_thread.start()
