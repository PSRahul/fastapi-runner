from fastapi import FastAPI
from enum import Enum

class ModelList(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello!"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}

@app.get("/models/{model_name}")
async def get_model_name(model_name: ModelList):
    if model_name==ModelList.alexnet:
        return {"model_name":"ALEXNET"}
    elif model_name.value==ModelList.lenet.value:
        return {"model_name":"LENET"}
    else:
        return {"model_name":"RESNET"}