import rti.asyncio  # we are not using it directly but removing it will get en error
import asyncio
import rti.connextdds as dds
import threading
from loguru import logger
from typing import Callable, Union

from rticonnector.TopicData import StructEnum, topic_data_dict
from rticonnector.constants import DEFAULT_DOMAIN_ID, PROFILE_NAME, QOS_FILE_PATH
from rticonnector.idl_types.LDM_Common import P_LDM_Common_T_Identifier


class Subscriber:
    def __init__(self, struct_enum: StructEnum, subscribe_event: Callable,
                 filter_keys: Union[list[P_LDM_Common_T_Identifier], str, None], domain_id=DEFAULT_DOMAIN_ID):
        self.struct_enum = struct_enum
        qos_provider = dds.QosProvider(QOS_FILE_PATH)

        self.participant = dds.DomainParticipant(
            domain_id, qos_provider.participant_qos
        )
        self.subscriber = dds.Subscriber(
            self.participant, qos_provider.subscriber_qos
        )
        self.topic = dds.Topic(
            self.participant,
            topic_data_dict[struct_enum].topic_name,
            topic_data_dict[struct_enum].topic_struct,
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
            self.__execute_subscribe_event(self.struct_enum, data)
            logger.trace(f'called the subscribe event with {self.struct_enum}, where {data = }')

    def __subscribe_thread(self):
        asyncio.run(self.__run())

    def subscribe(self):
        subscription_thread = threading.Thread(target=self.__subscribe_thread, daemon=True)
        subscription_thread.start()
