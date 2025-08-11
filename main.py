from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel
from enum import Enum

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

#Using enums
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

#Path parameters
@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: 
        return {"model name": model_name, "message": "Deep learing ftw"}
    if model_name.value == "lenet": 
        return {"model name": model_name, "message": "lenet is good"}

    return {"model name": model_name, "message": "Machine learning is great"}


#Put using request body data
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

#Post
@app.post("/")
def root(item: Item):
    name = item.name
    return {"message" : f"It's {name}"}
 
