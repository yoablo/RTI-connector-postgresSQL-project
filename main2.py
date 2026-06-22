import queue
import random
import time
from threading import Thread

from sqlalchemy import create_engine, BigInteger, Integer, text, String
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped, mapped_column

from rticonnector import publisher
from rticonnector import subscriber
from rticonnector import topic_data
from rticonnector.idl_types.Tactical_Sensor_PSM import (P_Tactical_Sensor_PSM_C_Detection)
from queue import Empty
import os
from dotenv import load_dotenv
from constants_2 import classification_name , Random_16_Digit_ID
from publish_simulator import simulate_publish , set_string_to_short_string ,get_from_short_string

load_dotenv()

detection_queue = queue.Queue()
republish_queue = queue.Queue()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)


class Base(DeclarativeBase):
    pass


class DetectionRecord(Base):
    __tablename__ = "detections"

    table_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    msb: Mapped[int] = mapped_column(BigInteger)
    lsb: Mapped[int] = mapped_column(BigInteger)

    seconds: Mapped[int] = mapped_column(BigInteger)
    class_name: Mapped[str] = mapped_column(String)


Base.metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE detections RESTART IDENTITY"))
    conn.commit()


def save_to_database(detection):

    msb = detection.A_detectionUniqueID.A_msb
    lsb = detection.A_detectionUniqueID.A_lsb
    seconds = detection.A_timeOfDataGeneration.A_seconds
    class_name = get_from_short_string(detection.A_detectionClassification)

    with Session(engine) as session:
        row_changed = False

        rows = session.query(DetectionRecord).all()

        for row in rows:
            if row.msb == msb and row.lsb == lsb:
                row.class_name = class_name
                row.seconds = seconds
                row_changed = True

        if not row_changed:
            record = DetectionRecord(msb=msb, lsb=lsb, seconds=seconds,class_name=class_name)
            session.add(record)

        session.commit()


def sub_message(topic_enum, detection):
    print(f"Received: " f"{detection.A_detectionUniqueID.A_msb}, " f"{detection.A_detectionUniqueID.A_lsb}")
    detection_queue.put(detection)
    process_detections()


def process_detections():
    while not detection_queue.empty():
        detection = detection_queue.get()

        if get_from_short_string(detection.A_detectionClassification) == classification_name.NOGA.value:
            set_string_to_short_string(detection.A_detectionClassification, classification_name.ATR.value)

        elif get_from_short_string(detection.A_detectionClassification) in (classification_name.ATR.value, classification_name.WINDOAT.value):
            set_string_to_short_string(detection.A_detectionClassification, classification_name.AT.value)

        save_to_database(detection)

        republish_queue.put(detection)


def republish(pub):
    print("Republisher thread started")

    while True:
        try:
            detection = republish_queue.get(timeout=0.5)
        except Empty:
            continue

        print(f"Republishing: " f"{detection.A_detectionUniqueID.A_msb}, "f"{detection.A_detectionUniqueID.A_lsb}")

        time.sleep(1)
        pub.publish(detection)



def random_id_or_enum():
    if random.random() < 0.3:
        returned_id = random.choice(list(Random_16_Digit_ID)).value
    else:
        returned_id = random.randint(1000000000000000,9999999999999999)

    return returned_id

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

def main():
    topic = topic_data.TopicEnum.DETECTION
    detection = P_Tactical_Sensor_PSM_C_Detection()

    sub = subscriber.Subscriber(topic, sub_message, "", "rticonnector/Configuration/BarakQosProfile.xml")

    pub = publisher.Publisher(topic, "rticonnector/Configuration/BarakQosProfile.xml")

    simulator_thread = Thread(target=simulate_publish, args=(pub, detection), daemon=True)

    subscriber_thread = Thread(target=sub.run, daemon=True)

    republisher_thread = Thread(target=republish, args=(pub,), daemon=True)

    simulator_thread.start()
    subscriber_thread.start()
    republisher_thread.start()

    simulator_thread.join()
    subscriber_thread.join()
    republisher_thread.join()


if __name__ == "__main__":
    main()