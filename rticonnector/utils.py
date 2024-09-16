from os import getenv
from rti.idl import char
from typing import Union

from rticonnector.idl_types.Detection import CharSequence


def str_to_char_sequence(str_input: str) -> Union[list[char], str]:
    return [ord(ch) for ch in str_input] if isinstance(str_input, str) else str_input


def char_sequence_to_str(char_sequence: CharSequence) -> str:
    return ''.join([chr(c) for c in char_sequence if c])


def string_sequence_to_str_list(string_sequence: list[CharSequence]) -> list[str]:
    return [char_sequence_to_str(string_struct.value) for string_struct in string_sequence]


def get_qos_file(qos_file_path: str) -> str:
    file_path = getenv('QOS_FILE_PATH') if qos_file_path is None else qos_file_path
    if file_path:
        return file_path
    raise ValueError('Env variable "QOS_FILE_PATH" is not set. Please provide the path to the QoS file.')
