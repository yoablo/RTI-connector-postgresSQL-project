import random
import time

from rticonnector.publisher import Publisher
from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection
from rticonnector.utils import char_sequence_to_string, string_to_char_sequence

from sqlalchemy import BigInteger

from constants_2 import DELAY_SECONDS, NANOSECONDS_CONVERSION_TO_SECONDS, \
    TRUELY_RANDOM_16_DIGIT_ID_START_VAR, TRUELY_RANDOM_16_DIGIT_ID_END_VAR, CHANCE_FOR_ID
from classes_file import Random16DigitID, ClassificationName


def simulate_publish(publisher: Publisher, detection: P_Tactical_Sensor_PSM_C_Detection):
    print("Simulator thread started")

    while True:
        detection = P_Tactical_Sensor_PSM_C_Detection()

        detection.A_detectionUniqueID.A_msb = choose_random_id_or_enum()
        detection.A_detectionUniqueID.A_lsb = choose_random_id_or_enum()
        detection.A_timeOfDataGeneration.A_seconds = (time.time_ns() // NANOSECONDS_CONVERSION_TO_SECONDS)
        detection.A_detectionClassification.value = string_to_char_sequence(
            random.choice(list(ClassificationName)).value)

        print(
            f"Simulating: {detection.A_detectionUniqueID.A_msb}, {detection.A_detectionUniqueID.A_lsb}, {char_sequence_to_string(detection.A_detectionClassification.value)}")

        time.sleep(DELAY_SECONDS)
        publisher.publish(detection)


def choose_random_id_or_enum() -> BigInteger:
    if random.random() < CHANCE_FOR_ID:
        returned_id = random.choice(list(Random16DigitID)).value
    else:
        returned_id = random.randint(TRUELY_RANDOM_16_DIGIT_ID_START_VAR, TRUELY_RANDOM_16_DIGIT_ID_END_VAR)

    return returned_id
