from fastapi import FastAPI

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

