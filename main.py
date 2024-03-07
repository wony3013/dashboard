import psutil
from fastapi import FastAPI, APIRouter
from http import HTTPStatus

from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI()

cpu_percent = None


@app.get("/")
async def cpu_info():
    return {"message": "hello"}

