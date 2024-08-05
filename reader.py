import rti.asyncio
import rti.idl as idl
import rti.connextdds as dds
from loguru import logger
from typing import Callable
from Configuration.TopicData import StructEnum, topic_data_dict
from auto_idl_types.LDM_Common import P_LDM_Common_T_Identifier
from constants import DEFAULT_DOMAIN_ID, QOS_PROVIDER, PROFILE_NAME


class Subscriber:
    def __init__(self, struct_enum: StructEnum, subscribe_event: Callable,
                 filter_keys: list[P_LDM_Common_T_Identifier], domain_id=DEFAULT_DOMAIN_ID):
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

        filter_test = dds.Filter(self.__get_filter_expression())
        self.filtered_topic = dds.ContentFilteredTopic(self.topic, self.topic.name + "_filtered", filter_test)

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
            self.__execute_subscribe_event(data)
            logger.trace(f'{data}')

    def __get_filter_expression(self) -> str:
        return " OR ".join(map(lambda key: f"(A_sourceID.A_platformId = {key.A_platformId} "
                                           f"AND A_sourceID.A_moduleId = {key.A_moduleId} "
                                           f"AND A_sourceID.A_systemId = {key.A_systemId})",
                               self.filter_keys))

    def subscribe(self):
        try:
            rti.asyncio.run(self.__run())
        except KeyboardInterrupt:
            pass
