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
from enum import Enum
from queue import Empty
import os
from dotenv import load_dotenv

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

        if get_from_short_string(detection.A_detectionClassification) == "NOGA":
            set_string_to_short_string(detection.A_detectionClassification, "ATR")

        elif get_from_short_string(detection.A_detectionClassification) in ("ATR", "WINDOAT"):
            set_string_to_short_string(detection.A_detectionClassification, "AT")

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

        pub.publish(detection)

def set_string_to_short_string(short_string, text):
    short_string.value.clear()
    short_string.value.extend(ord(c) for c in text)


def get_from_short_string(short_string):
    return ''.join(chr(x) for x in short_string.value)


def simulate_publish(pub, detection):
    print("Simulator thread started")

    while True:
        detection = P_Tactical_Sensor_PSM_C_Detection()
        detection.A_detectionUniqueID.A_msb = (random.choice(list(Random_16_Digit_ID)).value)
        detection.A_detectionUniqueID.A_lsb = (random.choice(list(Random_16_Digit_ID)).value)
        detection.A_timeOfDataGeneration.A_seconds = (time.time_ns() // 1_000_000_000)
        set_string_to_short_string(detection.A_detectionClassification,random.choice(list(random_classification_name)).value)

        print(f"Simulating: "f"{detection.A_detectionUniqueID.A_msb}, "f"{detection.A_detectionUniqueID.A_lsb}, "f"{get_from_short_string(detection.A_detectionClassification)}")

        pub.publish(detection)


class Random_16_Digit_ID(Enum):
    num_1 = 3001697090449141
    num_2 = 13533879590735665
    num_3 = 1691298520696870

class random_classification_name(Enum):
    name_1 = "NOGA"
    name_2 = "ATR"
    name_3 = "WINDOAT"

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
