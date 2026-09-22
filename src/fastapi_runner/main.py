from fastapi import FastAPI,Query
from enum import Enum
import numpy as np
from src.fastapi_runner.data_model import ProductModel
from typing import Annotated
from pydantic import AfterValidator
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


@app.post("/items/")
async def create_product(product:ProductModel):
    return product

@app.post("/items/read/")
async def read_items(q:Annotated[list[str]|None,Query(title="test_tile",description="test_description")]=None):
    default={"test_key":"test_values"}
    if q:
        default.update({"q":q})
    return default

def starts_with_s(s:str):
    if s[0]!='s':
        raise ValueError("must start with s")
    return s

@app.post("/items/valid_read/")
async def read_valid_items(id:Annotated[str|None,AfterValidator(starts_with_s)]):
    return id