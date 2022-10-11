from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from utils import get_my_public_ip

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):

    my_ip = get_my_public_ip()
    return templates.TemplateResponse(
        'index.html',
        {"request": request, "message": my_ip}
    )
