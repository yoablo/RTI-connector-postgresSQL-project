from constants_2 import (
    Random_16_Digit_ID,
    classification_name,
    delay_seconds,
    nanoseconds_conversion_to_seconds,
    truely_random_16_digit_ID_start_var,
    truely_random_16_digit_ID_end_var,
    chance_for_ID,
)
import random
import time
from rticonnector.idl_types.LDM_Common import P_LDM_Common
from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection


def get_string_from_short_string(short_string: P_LDM_Common.T_ShortString) -> str:
    return "".join(chr(num_character) for num_character in short_string.value)


def set_string_to_short_string(short_string: P_LDM_Common.T_ShortString, text: str):
    short_string.value.clear()
    short_string.value.extend(ord(character) for character in text)


def simulate_publish(pub: object, detection: object):
    print("Simulator thread started")

    while True:
        detection = P_Tactical_Sensor_PSM_C_Detection()
        detection.A_detectionUniqueID.A_msb = choose_random_id_or_enum()

        detection.A_detectionUniqueID.A_lsb = choose_random_id_or_enum()

        detection.A_timeOfDataGeneration.A_seconds = (
            time.time_ns() // nanoseconds_conversion_to_seconds
        )

        set_string_to_short_string(
            detection.A_detectionClassification,
            random.choice(list(classification_name)).value,
        )

        print(
            f"Simulating: {detection.A_detectionUniqueID.A_msb}, {detection.A_detectionUniqueID.A_lsb}, {get_string_from_short_string(detection.A_detectionClassification)}"
        )

        time.sleep(delay_seconds)
        pub.publish(detection)


def choose_random_id_or_enum():
    if random.random() < chance_for_ID:
        returned_id = random.choice(list(Random_16_Digit_ID)).value
    else:
        returned_id = random.randint(
            truely_random_16_digit_ID_start_var, truely_random_16_digit_ID_end_var
        )

    return returned_id
