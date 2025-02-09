from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.responses import PlainTextResponse
from middleware import setup_cors


app = FastAPI()
setup_cors(app)

@app.get("/", response_class=PlainTextResponse)
def get_info():
    current_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return (
        "email:" "nosikesamuel1@gmail.com\n"
        "current_datetime:" f"{current_time}\n"
        "github_url:" "https://github.com/Samcodio/hng_stage-zero"
    )


