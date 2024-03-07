from fastapi import FastAPI, Request
from typing import Union
from pydantic import BaseModel
import psutil
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()

class Item(BaseModel):
    name : str
    description : Union[str,None] = None
    price : float

@app.get("/")
async def read_root():
    return "This is root path from MyAPI"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,  None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id }")
def delete_item(item_id: int):
    return {"deleted": item_id}

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