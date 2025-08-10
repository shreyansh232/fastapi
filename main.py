from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

#Define model Item 
class Item(BaseModel):
    name: str

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

#Instatiate app
app = FastAPI();

#Handle get requests
@app.get("/")
def root():
    return {"message:" : "Hello World"}

@app.get("/items/{item}")
async def items(item: str):
    return {"item" : item}

#Takes in query parameter name
@app.get("/hello")
def hello(name: str = "Shreyansh"):
    return {"message" : f"Hello {name}"}

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: 
        return {"model name": model_name, "message": "Deep learing ftw"}
    if model_name.value == "lenet": 
        return {"model name": model_name, "message": "lenet is good"}

    return {"model name": model_name, "message": "Machine learning is great"}




@app.post("/")
def root(item: Item):
    name = item.name
    return {"message" : f"It's {name}"}
 
