from queue import Queue, Empty
from threading import Thread
from time import sleep
from pickle import dumps, loads

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from rticonnector.idl_types.Tactical_Sensor_PSM import P_Tactical_Sensor_PSM_C_Detection
from rticonnector.topic_data import TopicEnum
from rticonnector.publisher import Publisher
from rticonnector.subscriber import Subscriber
from rticonnector.utils import char_sequence_to_string, string_to_char_sequence

from publish_simulator import simulate_publish
from constants import DELAY_SECONDS, QOS_FILE, ENGINE_STRING, DATABASE_URL, ClassificationName, REDIS_CLIENT, \
    DETECTION_SOURCEID_PLATFORMID, DETECTION_SOURCEID_MODULEID, DETECTION_SOURCEID_SYSTEMID, FASPTAPI_SERVER_HOST, \
    FASPTAPI_SERVER_PORT, WHAT_SYSTEM_MOD_VARIABLE_FILTERS
from sql_classes import Base, DetectionRecord
from fastAPI_chrome_control_panel import app as chrome_control_panel_app
from uvicorn import run as uvicorn_run

publish_queue = Queue()
redis_client = REDIS_CLIENT

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(text(ENGINE_STRING))
    conn.commit()


def save_to_database(detection: P_Tactical_Sensor_PSM_C_Detection, is_published: bool):
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
            record = DetectionRecord(msb = msb, lsb = lsb, seconds = seconds, class_name = class_name,
                                     is_published = is_published)
            session.add(record)

        session.commit()


def subscriber_message(topic_enum: TopicEnum, detection: P_Tactical_Sensor_PSM_C_Detection):
    print(
        f"Received: {detection.A_detectionUniqueID.A_msb}, {detection.A_detectionUniqueID.A_lsb},{char_sequence_to_string(detection.A_detectionClassification.value)}")
    redis_client.rpush("latest_detection", dumps(detection))
    process_detections()


def publisher_filter(detection: P_Tactical_Sensor_PSM_C_Detection):
    return char_sequence_to_string(
        detection.A_detectionClassification.value) == ClassificationName.WINDCOAT.value or char_sequence_to_string(
        detection.A_detectionClassification.value) == ClassificationName.AT.value


def process_detections():
    _, raw_redis_pickled = redis_client.blpop("latest_detection")
    is_published = False

    if raw_redis_pickled is not None:
        detection = loads(raw_redis_pickled)

        if char_sequence_to_string(detection.A_detectionClassification.value) == ClassificationName.NOGA.value:
            detection.A_detectionClassification.value = string_to_char_sequence(ClassificationName.ATR.value)
        elif char_sequence_to_string(detection.A_detectionClassification.value) in (
                ClassificationName.ATR.value, ClassificationName.WINDCOAT.value
        ):
            detection.A_detectionClassification.value = string_to_char_sequence(ClassificationName.AT.value)

        if int(redis_client.get("system_mod_variable")) != WHAT_SYSTEM_MOD_VARIABLE_FILTERS or publisher_filter(detection):
            detection.A_sourceID.A_platformId = DETECTION_SOURCEID_PLATFORMID
            detection.A_sourceID.A_systemId = DETECTION_SOURCEID_MODULEID
            detection.A_sourceID.A_moduleId = DETECTION_SOURCEID_SYSTEMID
            print(
                f"!!!!! changed source ID to: {detection.A_sourceID.A_platformId}.{detection.A_sourceID.A_systemId}.{detection.A_sourceID.A_moduleId}")

            publish_queue.put(detection)
            is_published = True
        else:
            print(
                f"!!!!! no change: {detection.A_sourceID.A_platformId}.{detection.A_sourceID.A_systemId}.{detection.A_sourceID.A_moduleId}")

        save_to_database(detection, is_published)


def publish(publisher: Publisher):
    print("Republisher thread started")

    while True:
        try:
            detection = publish_queue.get()
        except Empty:
            continue

        print(
            f"Republishing: {detection.A_detectionUniqueID.A_msb} , {detection.A_detectionUniqueID.A_lsb}, {detection.A_sourceID}")

        sleep(DELAY_SECONDS)
        publisher.publish(detection)


def filter_char_sequence_with_string(detection_parameter_name: str, word: str):
    return " AND ".join(f"{detection_parameter_name}[{i}] = '{char}'" for i, char in enumerate(word))


def main():
    topic = TopicEnum.DETECTION
    detection = P_Tactical_Sensor_PSM_C_Detection()

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


def start_fasptAPI_control_panel():
    uvicorn_run(chrome_control_panel_app, host = FASPTAPI_SERVER_HOST,
                port = FASPTAPI_SERVER_PORT)


if __name__ == "__main__":
    Thread(target = start_fasptAPI_control_panel, daemon = True).start()
    main()
