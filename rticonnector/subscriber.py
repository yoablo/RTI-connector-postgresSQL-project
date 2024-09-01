import rti.asyncio  # we are not using it directly but removing it will get en error
from asyncio import run
from loguru import logger
from threading import Thread
import rti.connextdds as dds
from typing import Callable, Union

from rticonnector.utils import get_qos_file
from rticonnector.topic_data import TopicEnum, topic_data_dict
from rticonnector.constants import DEFAULT_DOMAIN_ID, PROFILE_NAME


class Subscriber:
    def __init__(self, topic_enum: TopicEnum, subscribe_event: Callable, filter_str: str, qos_file_path: str = None,
                 domain_id=DEFAULT_DOMAIN_ID):
        self.topic_enum = topic_enum
        qos_provider = dds.QosProvider(get_qos_file(qos_file_path))

        self.participant = dds.DomainParticipant(
            domain_id, qos_provider.participant_qos
        )
        self.subscriber = dds.Subscriber(
            self.participant, qos_provider.subscriber_qos
        )
        self.topic = dds.Topic(
            self.participant,
            topic_data_dict[topic_enum].topic_name,
            topic_data_dict[topic_enum].topic_struct,
            qos_provider.topic_qos,
        )

        self.filtered_topic = self.topic if filter_str == "" else\
            dds.ContentFilteredTopic(self.topic, self.topic.name + "_filtered", dds.Filter(filter_str))

        self.reader_default = dds.DataReader(
            self.subscriber,
            self.filtered_topic,
            qos_provider.datareader_qos_from_profile(
                PROFILE_NAME
            ),
        )
        self.subscribe_event = subscribe_event

    def __execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    async def __run(self):
        async for data in self.reader_default.take_data_async():
            self.__execute_subscribe_event(self.topic_enum, data)
            logger.trace(f'called the subscribe event with {self.topic_enum}, where {data = }')

    def __subscribe_thread(self):
        run(self.__run())

    def subscribe(self):
        subscription_thread = Thread(target=self.__subscribe_thread, daemon=True)
        subscription_thread.start()
