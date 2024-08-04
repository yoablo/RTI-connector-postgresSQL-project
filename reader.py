import rti.asyncio
import rti.connextdds as dds
from loguru import logger

import constants as const
from Configuration.TopicData import StructEnum, topic_data_dict


class Subscriber:
    def __init__(self, struct_enum: StructEnum, subscribe_event):
        self.topic_name = topic_data_dict[struct_enum].topic_name
        self.topic_struct = topic_data_dict[struct_enum].topic_struct

        qos_provider = dds.QosProvider(const.QOS_PROVIDER)
        self.participant = dds.DomainParticipant(
            int(const.DOMAIN_ID), qos_provider.participant_qos
        )
        self.subscriber = dds.Subscriber(
            self.participant, qos_provider.subscriber_qos
        )
        self.topic = dds.Topic(
            self.participant,
            self.topic_name,
            self.topic_struct,
            qos_provider.topic_qos,
        )
        self.reader_default = dds.DataReader(
            self.subscriber,
            self.topic,
            qos_provider.datareader_qos_from_profile(
                const.PROFILE_NAME
            ),
        )
        self.subscribe_event = subscribe_event

    def __execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    async def __run(self):
        async for data in self.reader_default.take_data_async():
            self.__execute_subscribe_event(data)
            logger.trace(f'{data}')

    def subscribe(self):
        try:
            rti.asyncio.run(self.__run())
        except KeyboardInterrupt:
            pass
