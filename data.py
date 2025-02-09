from fastapi import FastAPI
from datetime import datetime
import pytz
from middleware import setup_cors


app = FastAPI()
setup_cors(app)

@app.get("/")
def get_info():
    current_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "email": "nosikesamuel1@gmail.com", 
        "current_datetime": current_time, 
        "github_url": "https://github.com/Samcodio/hng_stage-zero"
        }


