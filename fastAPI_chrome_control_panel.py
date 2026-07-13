from fastapi import FastAPI

from constants import  SystemStateConstants, DEFAULT_SYSTEM_MOD_VARIABLE, SYSTEM_MOD_VARIABLE
from redis_utils import get_redis_system_state, set_redis_system_state

app = FastAPI()

set_redis_system_state(SYSTEM_MOD_VARIABLE, DEFAULT_SYSTEM_MOD_VARIABLE)


@app.post("/toggle")
def toggle():
    if get_redis_system_state() == SystemStateConstants.ALL_DETECTIONS.value:
        set_redis_system_state(SYSTEM_MOD_VARIABLE, SystemStateConstants.CRITICAL_DETECTIONS.value)
    else:
        set_redis_system_state(SYSTEM_MOD_VARIABLE, SystemStateConstants.ALL_DETECTIONS.value)

    return get_system_state()


@app.get("/get_system_state")
def get_system_state():
    if get_redis_system_state() == SystemStateConstants.CRITICAL_DETECTIONS.value:
        return "critical detections"
    else:
        return "all detections"
