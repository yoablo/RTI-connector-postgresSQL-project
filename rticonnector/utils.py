from os import getenv
from rti.idl import char

from rticonnector.idl_types.TacticalSensorSpecification import P_LDM_Common_T_ShortString


def str_to_char_sequence(str_input: str) -> list[char]:
    return [char(ord(ch)) for ch in str_input]


def str_list_to_short_string_sequence(str_list: list[str]) -> list[P_LDM_Common_T_ShortString]:
    return [P_LDM_Common_T_ShortString(str_to_char_sequence(string)) for string in str_list]


def get_qos_file(qos_file_path: str) -> str:
    if qos_file_path:  # Use the provided file path if available
        return qos_file_path
    qos_file_path = getenv('QOS_FILE_PATH')
    if qos_file_path:  # try the environment variable if the file path is not provided
        return qos_file_path
    raise ValueError('Env variable "QOS_FILE_PATH" is not set. Please provide the path to the QoS file.')
    