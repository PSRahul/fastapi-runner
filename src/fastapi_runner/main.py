from fastapi import FastAPI
from enum import Enum
import numpy as np


class ModelList(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello!"}

@app.get("/items/{item_id}")
async def read_item(item_id:int, extras:str,short:bool=False):
    if short:
        return "item_id, short set on"
    return {"item_id":item_id,"extras":extras}

@app.get("/models/{model_name}")
async def get_model_name(model_name: ModelList):
    if model_name==ModelList.alexnet:
        return {"model_name":"ALEXNET"}
    elif model_name.value==ModelList.lenet.value:
        return {"model_name":"LENET"}
    else:
        return {"model_name":"RESNET"}

@app.get("/files/read/{file_path:path}")
async def read_file(file_path:str):
    return f"Reading file Path - {file_path}"

@app.get("/arange")
async def arange_list( end:int,start:int=45):
    return np.arange(start,end).tolist()

