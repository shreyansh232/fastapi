from fastapi import FastAPI
from pydantic import BaseModel

#Define model Item 
class Item(BaseModel):
    name: str

#Instatiate app
app = FastAPI();

#Handle get requests
@app.get("/")
def root():
    return {"message:" : "Hello World"}

#Takes in query parameter name
@app.get("/hello")
def hello(name: str = "Shreyansh"):
    return {"message" : f"Hello {name}"}


@app.post("/")
def root(item: Item):
    name = item.name
    return {"message" : f"It's {name}"}
 
