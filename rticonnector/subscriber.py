import threading
from typing import Callable

import rti.connextdds as dds
from loguru import logger

from rticonnector.constants import DEFAULT_DOMAIN_ID, PROFILE_NAME
from rticonnector.topic_data import TopicEnum, topic_data_dict
from rticonnector.utils import get_qos_file


class Subscriber(threading.Thread):
    def __init__(self, topic_enum: TopicEnum, subscribe_event: Callable, filter_str: str, qos_file_path: str = None,
                 domain_id=DEFAULT_DOMAIN_ID):
        super().__init__(daemon=True)
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

        self.filtered_topic = dds.ContentFilteredTopic(self.topic, self.topic.name, dds.Filter(filter_str)) \
            if filter_str != "" else self.topic

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

    def run(self):
        while True:
            for data in self.reader_default.take_data():
                self.__execute_subscribe_event(self.topic_enum, data)
                logger.trace(f'called the subscribe event with {self.topic_enum}, where {data = }')
