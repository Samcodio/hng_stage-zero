from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.responses import PlainTextResponse
from middleware import setup_cors


app = FastAPI()
setup_cors(app)

@app.get("/", response_class=PlainTextResponse)
def get_info():
    return (
        f"email: nosikesamuel1@gmail.com\n"
        f"current_datetime: {datetime.now(pytz.utc).isoformat()}\n"
        f"github_url: https://github.com/Samcodio/hng_stage-zero"
    )


