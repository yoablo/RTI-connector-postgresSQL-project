import sys
import os
import rti.asyncio
import rti.connextdds as dds
import rti.idl as idl
import constants as const
from profiles import ProfilesExample
from loguru import logger


# todo: CHECK how project pack
class ProfilesExampleSubscriber:
    def __init__(self, topic_name: str, topic_struct: idl.struct, subscribe_event):

        self.subscribe_event = subscribe_event

        # Retrieve QoS from custom profile XML and USER_QOS_PROFILES.xml
        qos_provider = dds.QosProvider(const.QOS_PROVIDER)

        # Create a DomainParticipant with the default QoS of the provider.
        self.participant = dds.DomainParticipant(
            int(const.DOMAIN_ID), qos_provider.participant_qos
        )

        # Create a Subscriber with default QoS.
        self.subscriber = dds.Subscriber(
            self.participant, qos_provider.subscriber_qos
        )

        # Create a Topic with default QoS.
        self.topic = dds.Topic(
            self.participant,
            topic_name,
            topic_struct,
            qos_provider.topic_qos,
        )

        # Create a DataReader with the QoS profile "Default",
        # which is in the QoS library "Barak_Library".
        self.reader_default = dds.DataReader(
            self.subscriber,
            self.topic,
            qos_provider.datareader_qos_from_profile(
                const.PROFILE_NAME
            ),
        )

        self.samples_read = 0

    def execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    async def run(self, sample_count: int):  # TODO: change the name and run start the TH
        async for data in self.reader_default.take_data_async():
            self.execute_subscribe_event(data)
            # TODO: loguru
            self.samples_read += 1
            if self.samples_read >= sample_count:
                break


if __name__ == "__main__":
    def test_event(data):
        print(f"check the data:  {str(data)}")

    try:
        subscriber = ProfilesExampleSubscriber("test!!!!!!!!!", ProfilesExample, test_event)
        rti.asyncio.run(subscriber.run(sys.maxsize))
    except KeyboardInterrupt:
        pass
