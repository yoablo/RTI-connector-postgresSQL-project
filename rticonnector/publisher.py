import asyncio
import threading

import rti.asyncio
import rti.connextdds as dds
from rti.idl import struct as idl_struct
from rticonnector.constants import PROFILE_NAME, DEFAULT_DOMAIN_ID
from rticonnector.TopicData import StructEnum, topic_data_dict


class Publisher:
    def __init__(self, struct_enum: StructEnum, qos_file_path: str, domain_id=DEFAULT_DOMAIN_ID):
        self.topic_name = topic_data_dict[struct_enum].topic_name
        self.topic_struct = topic_data_dict[struct_enum].topic_struct
        qos_provider = dds.QosProvider(qos_file_path)

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

    def __publish_thread(self, struct_to_publish: idl_struct):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.__run(struct_to_publish))
        except KeyboardInterrupt:
            pass
        finally:
            loop.close()

    def publish(self, struct_to_publish: idl_struct):
        publish_thread = threading.Thread(target=self.__publish_thread, args=(struct_to_publish,), daemon=True)
        publish_thread.start()