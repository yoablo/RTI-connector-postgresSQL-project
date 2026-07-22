from constants import SYSTEM_MOD_VARIABLE, REDIS_CLIENT

def get_redis_system_state():
    return int(REDIS_CLIENT.get(SYSTEM_MOD_VARIABLE))

def set_redis_system_state(keyword: str,value):
    REDIS_CLIENT.set(keyword, value)