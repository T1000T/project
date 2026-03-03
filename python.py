from fastapi import FastAPI
import uvicorn

# Initialize the app
app = FastAPI()

# Define a route that responds to a GET request
@app.get("/")
def read_root():
    return {"message": "Hello! Your API is working."}

# Define a route that takes a parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

