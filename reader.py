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

        qos_provider = dds.QosProvider(QOS_PROVIDER)

        self.participant = dds.DomainParticipant(
            domain_id, qos_provider.participant_qos
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

        # Extract key fields and create the QueryCondition
        self.filter_keys = filter_keys
        key_field_values = [f"{key.A_platformId}.{key.A_systemId}.{key.A_moduleId}" for key in filter_keys]
        self.query_condition = dds.QueryCondition(
            self.reader_default,
            dds.DataState.any_data,
            "key_field IN (%s)" % ",".join(["'%s'" % key for key in key_field_values])
        )

    def execute_subscribe_event(self, *args, **kwargs):
        return self.subscribe_event(*args, **kwargs)

    async def run(self, sample_count: int):
        selector = self.reader_default.select().condition(self.query_condition)
        async for data in selector.take_data_async():
            self.execute_subscribe_event(data)
            self.samples_read += 1
            if self.samples_read >= sample_count:
                break


if __name__ == "__main__":
    def test_event(data):
        print(f"check the data: {str(data)}")


    try:
        filter_keys = [
            P_LDM_Common_T_Identifier(A_platformId=1, A_systemId=2, A_moduleId=3),
            P_LDM_Common_T_Identifier(A_platformId=4, A_systemId=5, A_moduleId=6),
            P_LDM_Common_T_Identifier(A_platformId=7, A_systemId=8, A_moduleId=9)
        ]

        # Pass the filter keys to the ProfilesExampleSubscriber constructor
        subscriber = ProfilesExampleSubscriber("P_Tactical_Sensor_PSM::C_Detection_Optronics",
                                               P_Tactical_Sensor_PSM_C_Detection_Optronics, test_event, filter_keys)
        rti.asyncio.run(subscriber.run(sys.maxsize))

    except KeyboardInterrupt:
        pass
