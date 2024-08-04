import sys
import rti.asyncio
import rti.connextdds as dds
import rti.idl as idl

from constants import DEFAULT_DOMAIN_ID, QOS_PROVIDER, PROFILE_NAME
from auto_idl_types.DetectionOptronics import P_Tactical_Sensor_PSM_C_Detection_Optronics, P_LDM_Common_T_Identifier


class ProfilesExampleSubscriber:
    def __init__(self, topic_name: str, topic_struct: idl.struct, subscribe_event, filter_keys: list,
                 domain_id=DEFAULT_DOMAIN_ID):
        self.subscribe_event = subscribe_event

        # Retrieve QoS from custom profile XML and USER_QOS_PROFILES.xml
        qos_provider = dds.QosProvider(QOS_PROVIDER)

        # Create a DomainParticipant with the default QoS of the provider.
        self.participant = dds.DomainParticipant(
            domain_id, qos_provider.participant_qos
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
                PROFILE_NAME
            ),
        )

        self.samples_read = 0

        # Extract key fields and create the ContentFilteredTopic
        self.filter_keys = filter_keys
        key_field_values = [f"{key.A_platformId}.{key.A_systemId}.{key.A_moduleId}" for key in filter_keys]
        # Join the key field values for the filter expression
        filter_expression = " OR ".join([f"A_sourceID = {key}" for key in key_field_values])
        filter_test = dds.Filter(filter_expression)

        # Create the ContentFilteredTopic
        self.filtered_topic = dds.ContentFilteredTopic(self.topic, self.topic.name + "_filtered", filter_test)

    # Update the DataReader to use the filtered topic
        self.reader_default = dds.DataReader(
            self.subscriber,
            self.filtered_topic,
            qos_provider.datareader_qos_from_profile(
                PROFILE_NAME
            ),
        )


def execute_subscribe_event(self, *args, **kwargs):
    return self.subscribe_event(*args, **kwargs)


async def run(self, sample_count: int):
    async for data in self.reader_default.take_data_async():
        self.execute_subscribe_event(data)
        self.samples_read += 1
        if self.samples_read >= sample_count:
            break


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
        subscriber = ProfilesExampleSubscriber("P_Tactical_Sensor_PSM::C_Detection_Optronics",
                                               P_Tactical_Sensor_PSM_C_Detection_Optronics, test_event, filter_keys)
        rti.asyncio.run(subscriber.run(sys.maxsize))

    except KeyboardInterrupt:
        pass
