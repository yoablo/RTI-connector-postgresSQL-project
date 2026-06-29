import queue
from queue import Empty
from threading import Thread
import time

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection
from rticonnector.topic_data import TopicEnum
from rticonnector.publisher import Publisher
from rticonnector.subscriber import Subscriber
from rticonnector.utils import char_sequence_to_string, string_to_char_sequence

from publish_simulator import simulate_publish
from constants_2 import DELAY_SECONDS, QOS_FILE, TOPIC_DETECTION, DETECTION, \
    ENGINE_STRING, DATABASE_URL
from classes_file import ClassificationName, Base, DetectionRecord

detection_queue = queue.Queue()
publish_queue = queue.Queue()

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(text(ENGINE_STRING))
    conn.commit()


def save_to_database(detection: P_Tactical_Sensor_PSM_C_Detection):
    msb = detection.A_detectionUniqueID.A_msb
    lsb = detection.A_detectionUniqueID.A_lsb
    seconds = detection.A_timeOfDataGeneration.A_seconds
    class_name = char_sequence_to_string(detection.A_detectionClassification.value)

    with Session(engine) as session:
        row_changed = False
        rows = session.query(DetectionRecord).all()

        for row in rows:
            if row.msb == msb and row.lsb == lsb:
                row.class_name = class_name
                row.seconds = seconds
                row_changed = True

        if not row_changed:
            record = DetectionRecord(msb = msb, lsb = lsb, seconds = seconds, class_name = class_name)
            session.add(record)

        session.commit()


def subscriber_message(topic_enum: TopicEnum, detection: P_Tactical_Sensor_PSM_C_Detection):
    print(f"Received: {detection.A_detectionUniqueID.A_msb}, {detection.A_detectionUniqueID.A_lsb}")
    detection_queue.put(detection)
    process_detections()


def process_detections():
    while not detection_queue.empty():
        detection = detection_queue.get()

        if char_sequence_to_string(detection.A_detectionClassification.value) == ClassificationName.NOGA.value:
            detection.A_detectionClassification.value = string_to_char_sequence(ClassificationName.ATR.value)
        elif char_sequence_to_string(detection.A_detectionClassification.value) in (
                ClassificationName.ATR.value, ClassificationName.WINDOAT.value
        ):
            detection.A_detectionClassification.value = string_to_char_sequence(ClassificationName.AT.value)

        save_to_database(detection)
        publish_queue.put(detection)


def publish(publisher: Publisher):
    print("Republisher thread started")

    while True:
        try:
            detection = publish_queue.get()
        except Empty:
            continue

        print(f"Republishing: {detection.A_detectionUniqueID.A_msb} , {detection.A_detectionUniqueID.A_lsb}")

        time.sleep(DELAY_SECONDS)
        publisher.publish(detection)


def main():
    topic = TOPIC_DETECTION
    detection = DETECTION

    subscriber_object = Subscriber(topic, subscriber_message, "", QOS_FILE)
    publisher_object = Publisher(topic, QOS_FILE)
    simulator_publisher_object = Publisher(topic, QOS_FILE)

    simulator_thread = Thread(target = simulate_publish, args = (simulator_publisher_object, detection), daemon = True)
    subscriber_thread = Thread(target = subscriber_object.run, daemon = True)
    publisher_thread = Thread(target = publish, args = (publisher_object,), daemon = True)

    simulator_thread.start()
    subscriber_thread.start()
    publisher_thread.start()

    simulator_thread.join()
    subscriber_thread.join()
    publisher_thread.join()


if __name__ == "__main__":
    main()
