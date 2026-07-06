from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from threading import Lock, Thread
import time


# SHARED CONTROL STATE

class ControlState:
    def __init__(self):
        self.lock = Lock()
        self.filter = None
        self.paused = False


state = ControlState()

# FASTAPI APP

app = FastAPI()

# HTML UI (Chrome buttons)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DDS Control Panel</title>
</head>
<body>

<h2>DDS Control Panel</h2>

<button onclick="setFilter('NOGA')">NOGA</button>
<button onclick="setFilter('ATR')">ATR</button>
<button onclick="setFilter('AT')">AT</button>

<br><br>

<button onclick="pause()">PAUSE</button>
<button onclick="resume()">RESUME</button>

<script>
function setFilter(value) {
    fetch("/set-filter", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({value: value})
    });
}

function pause() {
    fetch("/pause", {method: "POST"});
}

function resume() {
    fetch("/resume", {method: "POST"});
}
</script>

</body>
</html>
"""


@app.get("/", response_class = HTMLResponse)
def ui():
    return HTML_PAGE


# REQUEST MODEL

class FilterRequest(BaseModel):
    value: str


# CONTROL ENDPOINTS

@app.post("/set-filter")
def set_filter(req: FilterRequest):
    with state.lock:
        state.filter = req.value
    print("Filter set:", req.value)
    return {"ok": True}


@app.post("/pause")
def pause():
    with state.lock:
        state.paused = True
    print("Paused")
    return {"paused": True}


@app.post("/resume")
def resume():
    with state.lock:
        state.paused = False
    print("Resumed")
    return {"paused": False}


# SIMULATED DDS LOOP
# (replace with your real subscriber logic)

def fake_dds_loop():
    i = 0
    while True:
        time.sleep(1)

        with state.lock:
            if state.paused:
                print("DDS paused...")
                continue

            current_filter = state.filter

        print(f"DDS message {i} | filter={current_filter}")
        i += 1


# RUN EVERYTHING

if __name__ == "__main__":
    import uvicorn

    # Start DDS simulation in background
    Thread(target = fake_dds_loop, daemon = True).start()

    # Start FastAPI server
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
