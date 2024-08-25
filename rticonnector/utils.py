from rti import idl


def str_to_char_sequence(str_input):
    return [idl.char(ord(ch)) for ch in str_input]
