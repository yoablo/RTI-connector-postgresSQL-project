from time import time
from rti.idl import char

from rticonnector.idl_types.TacticalSensorSpecification import P_LDM_Common_T_ShortString


def str_to_char_sequence(str_input: str) -> list[char]:
    return [char(ord(ch)) for ch in str_input]


def str_list_to_short_string_sequence(str_list: list[str]) -> list[P_LDM_Common_T_ShortString]:
    return [P_LDM_Common_T_ShortString(str_to_char_sequence(string)) for string in str_list]


def get_seconds_and_nanoseconds() -> (int, int):
    time_now = time()
    seconds = int(time_now)
    nanoseconds = int((time_now - seconds) * 1_000_000_000)
    return seconds, nanoseconds
