from fastapi import FastAPI

from constants import REDIS_CLIENT , FastAPIConstants , DEFAULT_SYSTEM_MOD_VARIABLE

app = FastAPI()

REDIS_CLIENT.set("system_mod_variable",DEFAULT_SYSTEM_MOD_VARIABLE)


@app.post("/toggle")
def toggle():
    if int(REDIS_CLIENT.get("system_mod_variable")) == FastAPIConstants.ALL_DETECTIONS.value:
        REDIS_CLIENT.set("system_mod_variable", FastAPIConstants.CRITICAL_DETECTIONS.value)
        system_state = "critical detections"
    else:
        REDIS_CLIENT.set("system_mod_variable", FastAPIConstants.ALL_DETECTIONS.value)
        system_state = "all detections"
    return system_state
