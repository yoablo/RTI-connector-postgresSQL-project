from fastapi import FastAPI

from constants import REDIS_CLIENT

app = FastAPI()


@app.post("/toggle")
def toggle():
    value = int(REDIS_CLIENT.get("system_mod_variable"))
    value = 1 - value
    REDIS_CLIENT.set("system_mod_variable", value)

    return {"system_mod_variable": value}
