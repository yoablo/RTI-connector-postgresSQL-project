from os import getenv
import rti.asyncio  # we are not using it directly but removing it will get en error
import asyncio
import rti.connextdds as dds
import threading
from loguru import logger
from typing import Callable, Union

from rticonnector.topic_data import TopicEnum, topic_data_dict
from rticonnector.constants import DEFAULT_DOMAIN_ID, PROFILE_NAME
from rticonnector.idl_types.LDM_Common import P_LDM_Common_T_Identifier


class Subscriber:
    def __init__(self, topic_enum: TopicEnum, subscribe_event: Callable,
                 filter_keys: Union[list[P_LDM_Common_T_Identifier], str, None], qos_file_path: str = None,
                 domain_id=DEFAULT_DOMAIN_ID):
        self.topic_enum = topic_enum
        if qos_file_path is None:
            qos_file_path = getenv('QOS_FILE_PATH')
            if qos_file_path is None:
                raise ValueError('Env variable "QOS_FILE_PATH" is not set. please provide the path to the qos file.')
        qos_provider = dds.QosProvider(qos_file_path)

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
        if filter_keys is not None:
            if isinstance(filter_keys, str):
                filter_expression = dds.Filter(filter_keys)
            elif isinstance(filter_keys, list):
                filter_expression = dds.Filter(self.__get_filter_expression(filter_keys))
            else:
                raise ValueError("Invalid type for filter_keys. Must be str or list of P_LDM_Common_T_Identifier type")
            self.filtered_topic = dds.ContentFilteredTopic(self.topic, self.topic.name + "_filtered", filter_expression)
        else:
            self.filtered_topic = self.topic

        self.reader_default = dds.DataReader(
            self.subscriber,
            self.filtered_topic,
            qos_provider.datareader_qos_from_profile(
                PROFILE_NAME
            ),
        )
        self.subscribe_event = subscribe_event

    @staticmethod
    def __get_filter_expression(filter_keys) -> str:
        return " OR ".join(map(lambda key: f"(A_sourceID.A_platformId = {key.A_platformId} "
                                           f"AND A_sourceID.A_moduleId = {key.A_moduleId} "
                                           f"AND A_sourceID.A_systemId = {key.A_systemId})",
                               filter_keys))

    def __execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    async def __run(self):
        async for data in self.reader_default.take_data_async():
            self.__execute_subscribe_event(self.topic_enum, data)
            logger.trace(f'called the subscribe event with {self.topic_enum}, where {data = }')

    def __subscribe_thread(self):
        asyncio.run(self.__run())

    def subscribe(self):
        subscription_thread = threading.Thread(target=self.__subscribe_thread, daemon=True)
        subscription_thread.start()
