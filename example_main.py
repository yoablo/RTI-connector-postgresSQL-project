import queue
import random
import time
from threading import Thread

from sqlalchemy import create_engine, BigInteger, Integer, text
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped, mapped_column

from rticonnector import publisher
from rticonnector import subscriber
from rticonnector import topic_data
from rticonnector.idl_types.Tactical_Sensor_PSM import (P_Tactical_Sensor_PSM_C_Detection)
from enum import Enum
from queue import Empty

detection_queue = queue.Queue()
republish_queue = queue.Queue()

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/dds_project")


class Base(DeclarativeBase):
    pass


class DetectionRecord(Base):
    __tablename__ = "detections"

    table_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    msb: Mapped[int] = mapped_column(BigInteger)
    lsb: Mapped[int] = mapped_column(BigInteger)

    seconds: Mapped[int] = mapped_column(BigInteger)


Base.metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE detections RESTART IDENTITY"))
    conn.commit()


def save_to_database(detection):  # nanoseconds

    msb = detection.A_detectionUniqueID.A_msb
    lsb = detection.A_detectionUniqueID.A_lsb
    seconds = detection.A_timeOfDataGeneration.A_seconds

    with Session(engine) as session:
        row_changed = False

        rows = session.query(DetectionRecord).all()

        for row in rows:
            if row.msb == msb and row.lsb == lsb:
                # Change only this row
                row.seconds = seconds
                row_changed = True

        if not row_changed:
            record = DetectionRecord(msb=msb, lsb=lsb, seconds=seconds)  # seconds=seconds
            session.add(record)

        session.commit()


# def sub_message(topic_enum, detection):
#     print(f"Received: " f"{detection.A_detectionUniqueID.A_msb}, " f"{detection.A_detectionUniqueID.A_lsb}")
#     detection_queue.put(detection)

def sub_message(topic_enum, detection):
    while True:
        print(f"Received: "f"{detection.A_detectionUniqueID.A_msb}, "f"{detection.A_detectionUniqueID.A_lsb}")

        save_to_database(detection)

        republish_queue.put(detection)


# def process_detections():
#     print("Processing thread started")
#
#     while True:
#         try:
#             detection = detection_queue.get(timeout=0.5)
#         except Empty:
#             continue
#
#         # detection.A_timeOfDataGeneration.A_seconds = (time.time_ns() // 1_000_000_000)
#
#         save_to_database(detection)
#
#         republish_queue.put(detection)


def republish(pub):
    print("Republisher thread started")

    while True:
        try:
            detection = republish_queue.get(timeout=0.5)
        except Empty:
            continue

        print(f"Republishing: " f"{detection.A_detectionUniqueID.A_msb}, "f"{detection.A_detectionUniqueID.A_lsb}")

        pub.publish(detection)


def simulate(pub, detection):
    print("Simulator thread started")

    while True:
        detection = P_Tactical_Sensor_PSM_C_Detection()
        detection.A_detectionUniqueID.A_msb = (random.choice(list(Random16DigitID)).value)
        detection.A_detectionUniqueID.A_lsb = (random.choice(list(Random16DigitID)).value)
        detection.A_timeOfDataGeneration.A_seconds = (time.time_ns() // 1_000_000_000)

        print(f"Simulating: "f"{detection.A_detectionUniqueID.A_msb}, "f"{detection.A_detectionUniqueID.A_lsb}")

        pub.publish(detection)

        time.sleep(2)


class Random16DigitID(Enum):
    num_1 = 3001697090449141
    num_2 = 1353387959073566
    num_3 = 1691298520696870
    # num_4 = 5808496090508926
    # num_5 = 7368284097418089


def main():
    topic = topic_data.TopicEnum.DETECTION
    detection = P_Tactical_Sensor_PSM_C_Detection()

    sub = subscriber.Subscriber(topic, sub_message, "", "rticonnector/Configuration/BarakQosProfile.xml")

    pub = publisher.Publisher(topic, "rticonnector/Configuration/BarakQosProfile.xml")

    simulator_thread = Thread(target=simulate, args=(pub, detection), daemon=True)

    subscriber_thread = Thread(target=sub.run, daemon=True)

    processing_thread = Thread(target=process_detections, daemon=True)

    republisher_thread = Thread(target=republish, args=(pub,), daemon=True)

    simulator_thread.start()
    # time.sleep(3)
    subscriber_thread.start()
    processing_thread.start()
    republisher_thread.start()

    simulator_thread.join()
    subscriber_thread.join()
    processing_thread.join()
    republisher_thread.join()


if __name__ == "__main__":
    main()
