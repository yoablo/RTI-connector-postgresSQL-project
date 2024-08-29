from os import getenv


def get_qos_file(qos_file_path: str) -> str:
    if qos_file_path:  # Use the provided file path if available
        return qos_file_path
    qos_file_path = getenv('QOS_FILE_PATH')
    if qos_file_path:  # try the environment variable if the file path is not provided
        return qos_file_path
    raise ValueError('Env variable "QOS_FILE_PATH" is not set. Please provide the path to the QoS file.')
