from fastapi import FastAPI
from utils import get_my_ip

app = FastAPI()

@app.get("/")
async def root():

    my_ip = get_my_ip()
    return {"message": my_ip}
