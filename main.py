from fastapi import FastAPI, Request
import psutil
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
async def read_root():
    return "This is root path from MyAPI"


@app.get("/info/")
async def read_info(request:Request) :
    return templates.TemplateResponse("infoMain.html", {"request":request})

@app.get("/info/getInfo/")
async def get_info() :
    # CPU 정보 얻기
    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    # 메모리 정보 얻기
    virtual_memory = psutil.virtual_memory()

    total_memory = virtual_memory.total // (1024 * 1024)
    available_memory = virtual_memory.available // (1024 * 1024)
    used_memory = total_memory - available_memory

    totalInfo = {"cpu_percent":cpu_percent,"cpu_count":cpu_count, "total_memory":total_memory, "available_memory":available_memory, "used_memory":used_memory}

    return totalInfo