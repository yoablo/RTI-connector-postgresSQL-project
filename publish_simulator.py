from constants_2 import Random_16_Digit_ID , classification_name
import random
import time
from rticonnector.idl_types.Tactical_Sensor_PSM import (P_Tactical_Sensor_PSM_C_Detection)

def get_from_short_string(short_string):
    return ''.join(chr(num_character) for num_character in short_string.value)

def set_string_to_short_string(short_string, text):
    short_string.value.clear()
    short_string.value.extend(ord(character) for character in text)

def simulate_publish(pub, detection):
    print("Simulator thread started")

    while True:
        detection = P_Tactical_Sensor_PSM_C_Detection()
        detection.A_detectionUniqueID.A_msb = random_id_or_enum()
        detection.A_detectionUniqueID.A_lsb = random_id_or_enum()
        detection.A_timeOfDataGeneration.A_seconds = (time.time_ns() // 1_000_000_000)
        set_string_to_short_string(detection.A_detectionClassification,random.choice(list(classification_name)).value)

        print(f"Simulating: "f"{detection.A_detectionUniqueID.A_msb}, "f"{detection.A_detectionUniqueID.A_lsb}, "f"{get_from_short_string(detection.A_detectionClassification)}")

        time.sleep(1)
        pub.publish(detection)

def random_id_or_enum():
    if random.random() < 0.5:
        returned_id = random.choice(list(Random_16_Digit_ID)).value
    else:
        returned_id = random.randint(1000000000000000,9999999999999999)

    return returned_id