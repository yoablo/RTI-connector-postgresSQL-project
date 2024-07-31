import sys
import asyncio
from rti.idl import struct
import rti.asyncio
import rti.connextdds as dds
import constants as const
from auto_idl_types.DetectionOptronics import P_Tactical_Sensor_PSM_C_Detection_Optronics


class ProfilesExamplePublisher:
    def __init__(self, topic_name: str, topic_struct: struct):

        # Retrieve QoS from custom profile XML and USER_QOS_PROFILES.xml
        qos_provider = dds.QosProvider(const.QOS_PROVIDER)

        # Create a DomainParticipant with the default QoS of the provider.
        self.participant = dds.DomainParticipant(
            const.DOMAIN_ID, qos_provider.participant_qos
        )

        # Create a Publisher with default QoS.
        publisher = dds.Publisher(self.participant, qos_provider.publisher_qos)

        # Create a Topic with default QoS.
        topic = dds.Topic(
            self.participant,
            topic_name,
            topic_struct,
            qos_provider.topic_qos,
        )

        # Create a DataWriter with the QoS profile "Default",
        # from QoS library "Barak_Library".
        self.writer_default = dds.DataWriter(
            publisher,
            topic,
            qos_provider.datawriter_qos_from_profile(
                const.PROFILE_NAME
            ),
        )

        self.samples_written = 0

    async def run(self, sample_count: int):
        sample = P_Tactical_Sensor_PSM_C_Detection_Optronics()
        while self.samples_written < sample_count:
            # Send the sample using the DataWriter with "Default" durability.
            sample.A_confidence = 2.2
            print(f"* Writing {sample}")
            self.writer_default.write(sample)

            self.samples_written += 1
            await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        # rti.asyncio.run(ProfilesExamplePublisher("test!!!!!!!!!", ProfilesExample).run(sys.maxsize))
        rti.asyncio.run(ProfilesExamplePublisher("P_Tactical_Sensor_PSM::C_Detection_Optronics",
                                                 P_Tactical_Sensor_PSM_C_Detection_Optronics).run(sys.maxsize))

    except KeyboardInterrupt:
        pass
