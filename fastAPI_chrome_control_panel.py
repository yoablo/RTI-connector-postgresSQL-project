from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from constants import DEFAULT_SYSTEM_MOD_VARIABLE, REDIS_CLIENT

app = FastAPI()

REDIS_CLIENT.set("system_mod_variable", DEFAULT_SYSTEM_MOD_VARIABLE)


@app.get("/", response_class = HTMLResponse)
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Toggle critical mod</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:100px;">
        <h2>FastAPI's control panel</h2>

        <button onclick="toggleVariable()" style="font-size:24px; padding:20px;">
            Toggle critical mod
        </button>

        <p id="status" style="font-size:20px;">
            Current value: {int(REDIS_CLIENT.get("system_mod_variable"))}
        </p>

        <script>
            async function toggleVariable() {{
                const response = await fetch("/toggle", {{method: "POST"}});

                const data = await response.json();

                document.getElementById("status").innerHTML = "Current value: " + data.system_mod_variable;
            }}
        </script>
    </body>
    </html>
    """


@app.post("/toggle")
def toggle():
    if int(REDIS_CLIENT.get("system_mod_variable")) == 0:
        REDIS_CLIENT.set("system_mod_variable", 1)
    else:
        REDIS_CLIENT.set("system_mod_variable", 0)

    print(f"system_mod_variable = {int(REDIS_CLIENT.get("system_mod_variable"))}")
    print("")
    print("")

    return {"system_mod_variable": int(REDIS_CLIENT.get("system_mod_variable"))}
