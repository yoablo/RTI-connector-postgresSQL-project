from os import getenv

def string_to_char_sequence(s: str):
    return list(s.encode("utf-8"))


def char_sequence_to_string(seq):
    return bytes(seq).decode("utf-8")


def get_qos_file(qos_file_path: str) -> str:
    file_path = getenv('QOS_FILE_PATH') if qos_file_path is None else qos_file_path
    if file_path:
        return file_path
    raise ValueError('Env variable "QOS_FILE_PATH" is not set. Please provide the path to the QoS file.')
