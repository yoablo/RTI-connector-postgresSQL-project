import rti.asyncio
import rti.connextdds as dds
import rti.idl as idl

from auto_idl_types.LDM_Common import P_LDM_Common_T_Identifier
from constants import DEFAULT_DOMAIN_ID, QOS_PROVIDER, PROFILE_NAME

from typing import Callable
from loguru import logger
from Configuration.TopicData import StructEnum, topic_data_dict


class Subscriber:
    def __init__(self, struct_enum: StructEnum, subscribe_event: Callable,
                 filter_keys: list[P_LDM_Common_T_Identifier], domain_id=DEFAULT_DOMAIN_ID):
        self.topic_name = topic_data_dict[struct_enum].topic_name
        self.topic_struct = topic_data_dict[struct_enum].topic_struct

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

        # Extract key fields and create the ContentFilteredTopic
        expressions = []
        for key in filter_keys:
            expr = f"(A_sourceID.A_platformId = {key.A_platformId} AND " \
                   f"A_sourceID.A_moduleId = {key.A_moduleId} AND " \
                   f"A_sourceID.A_systemId = {key.A_systemId})"
            expressions.append(expr)

        expression = " OR ".join(expressions)
        filter_test = dds.Filter(expression)

        self.filtered_topic = dds.ContentFilteredTopic(self.topic, self.topic.name + "_filtered", filter_test)

        # Create a DataReader with the QoS profile "Default",
        # which is in the QoS library "Barak_Library".
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

    def subscribe(self):
        try:
            rti.asyncio.run(self.__run())
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    def test_event(data):
        print(f"check the data: {str(data)}")


    try:
        # Create a list of P_LDM_Common_T_Identifier objects
        filter_keys = [
            P_LDM_Common_T_Identifier(A_platformId=1, A_systemId=14, A_moduleId=1),
            P_LDM_Common_T_Identifier(A_platformId=1, A_systemId=21, A_moduleId=1),
        ]

        # Pass the filter keys to the ProfilesExampleSubscriber constructor
        subscriber = Subscriber(StructEnum.DETECTION_OPTRONICS, test_event, filter_keys)
        subscriber.subscribe()

    except KeyboardInterrupt:
        pass
