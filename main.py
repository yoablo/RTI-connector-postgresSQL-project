import queue
import time
from threading import Thread
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from rticonnector import publisher, subscriber
from queue import Empty
import os
from dotenv import load_dotenv
from publish_simulator import simulate_publish, set_string_to_short_string, get_string_from_short_string
from constants_2 import classification_name, delay_seconds, Base, DetectionRecord, qos_file, topic1, detection1, \
    engine_string
from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection
from rticonnector.topic_data import TopicEnum

load_dotenv()

detection_queue = queue.Queue()

publish_queue = queue.Queue()

database_url = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/dds_project")

engine = create_engine(database_url)

Base.metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(text(engine_string))
    conn.commit()


def save_to_database(detection: P_Tactical_Sensor_PSM_C_Detection()):
    msb = detection.A_detectionUniqueID.A_msb
    lsb = detection.A_detectionUniqueID.A_lsb
    seconds = detection.A_timeOfDataGeneration.A_seconds
    class_name = get_string_from_short_string(detection.A_detectionClassification)

    with Session(engine) as session:
        row_changed = False

        rows = session.query(DetectionRecord).all()

        for row in rows:
            if row.msb == msb and row.lsb == lsb:
                row.class_name = class_name
                row.seconds = seconds
                row_changed = True

        if not row_changed:
            record = DetectionRecord(msb=msb, lsb=lsb, seconds=seconds, class_name=class_name)
            session.add(record)

        session.commit()


def subcriber_message(topic_enum: TopicEnum.DETECTION, detection: P_Tactical_Sensor_PSM_C_Detection()):
    print(f"Received: {detection.A_detectionUniqueID.A_msb}, {detection.A_detectionUniqueID.A_lsb}")
    detection_queue.put(detection)
    process_detections()


def process_detections():
    while not detection_queue.empty():
        detection = detection_queue.get()

        if get_string_from_short_string(detection.A_detectionClassification) == classification_name.NOGA.value:
            set_string_to_short_string(detection.A_detectionClassification, classification_name.ATR.value)

        elif get_string_from_short_string(detection.A_detectionClassification) in (classification_name.ATR.value,
                                                                                   classification_name.WINDOAT.value):
            set_string_to_short_string(detection.A_detectionClassification, classification_name.AT.value)

        save_to_database(detection)

        publish_queue.put(detection)


def publish(publisher):
    print("Republisher thread started")

    while True:
        try:
            detection = publish_queue.get()
        except Empty:
            continue

        print(f"Republishing: {detection.A_detectionUniqueID.A_msb} , {detection.A_detectionUniqueID.A_lsb}")

        time.sleep(delay_seconds)

        publisher.Publish(detection)


def main():
    topic = topic1
    detection = detection1

    subscriber1 = subscriber.Subscriber(topic, subcriber_message, "", qos_file)

    publisher1 = publisher.Publisher(topic, qos_file)

    simulator_thread = Thread(target=simulate_publish, args=(publisher1, detection), daemon=True)

    subscriber_thread = Thread(target=subscriber1.run, daemon=True)

    publisher_thread = Thread(target=publish, args=(publisher,), daemon=True)

    simulator_thread.start()
    subscriber_thread.start()
    publisher_thread.start()

    simulator_thread.join()
    subscriber_thread.join()
    publisher_thread.join()


if __name__ == "__main__":
    main()
