from builtins import function
from sys import maxsize
import rti.asyncio
import rti.connextdds as dds
from loguru import logger


import constants as const
from Configuration.TopicData import StructEnum, topic_data_dict


class ProfilesExampleSubscriber:
    def __init__(self, struct_enum: StructEnum, subscribe_event):
        topic_name = topic_data_dict[struct_enum].topic_name
        topic_struct = topic_data_dict[struct_enum].topic_struct

        qos_provider = dds.QosProvider(const.QOS_PROVIDER)
        self.participant = dds.DomainParticipant(
            int(const.DOMAIN_ID), qos_provider.participant_qos
        )
        self.subscriber = dds.Subscriber(
            self.participant, qos_provider.subscriber_qos
        )
        self.topic = dds.Topic(
            self.participant,
            topic_name,
            topic_struct,
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
        self.samples_read = 0

    def execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    async def run(self, sample_count: int):

        async for data in self.reader_default.take_data_async():
            self.execute_subscribe_event(data)
            logger.trace(f'{data}')
            self.samples_read += 1
            if self.samples_read >= sample_count:
                break


def run(struct_enum: StructEnum, subscribe_event: function):
    try:
        subscriber = ProfilesExampleSubscriber(struct_enum, subscribe_event)
        rti.asyncio.run(subscriber.run(maxsize))
    except KeyboardInterrupt:
        pass
