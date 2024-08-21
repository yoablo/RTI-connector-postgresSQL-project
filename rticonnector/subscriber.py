import rti.asyncio
import rti.connextdds as dds
import threading
from loguru import logger
from typing import Callable, Union

from rticonnector.TopicData import StructEnum, topic_data_dict
from rticonnector.idl_types.LDM_Common import P_LDM_Common_T_Identifier
from rticonnector.constants import DEFAULT_DOMAIN_ID, QOS_PROVIDER, PROFILE_NAME


class Subscriber:
    def __init__(self, struct_enum: StructEnum, subscribe_event: Callable,
                 filter_keys: Union[list[P_LDM_Common_T_Identifier], str, None], domain_id=DEFAULT_DOMAIN_ID):
        self.topic_name = topic_data_dict[struct_enum].topic_name
        self.topic_struct = topic_data_dict[struct_enum].topic_struct
        self.filter_keys = filter_keys

        qos_provider = dds.QosProvider(QOS_PROVIDER)

        self.participant = dds.DomainParticipant(
            domain_id, qos_provider.participant_qos
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
        if filter_keys is not None:
            if isinstance(filter_keys, str):
                filter_expression = dds.Filter(filter_keys)
            elif isinstance(filter_keys, list):
                filter_expression = dds.Filter(self.__get_filter_expression())
            else:
                raise ValueError("Invalid type for filter_keys. Must be str or list.")
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

    def __execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    def __get_filter_expression(self) -> str:
        return " OR ".join(map(lambda key: f"(A_sourceID.A_platformId = {key.A_platformId} "
                                           f"AND A_sourceID.A_moduleId = {key.A_moduleId} "
                                           f"AND A_sourceID.A_systemId = {key.A_systemId})",
                               self.filter_keys))

    async def __run(self):
        async for data in self.reader_default.take_data_async():
            self.__execute_subscribe_event(data)
            logger.trace(f'{data}')

    def __subscribe_thread(self):
        asyncio.run(self.__run())

    def subscribe(self):
        subscription_thread = threading.Thread(target=self.__subscribe_thread, daemon=True)
        subscription_thread.start()
