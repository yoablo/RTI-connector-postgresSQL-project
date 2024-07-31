
import rti.idl as idl


@idl.struct
class ProfilesExample:
    profile_name: str = ""
    x: idl.int32 = 0


@idl.struct
class ProfilesExample2:
    profile_name: str = ""
    x: idl.int32 = 0
