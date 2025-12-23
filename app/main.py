from fastapi import FastAPI

app = FastAPI(title="FastAPI Fundamentals")

@app.get("/")
def root():
    return {"message": "FastAPI Fundamentals running"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}

@app.post("/items")
def create_item(item: dict):
    return {"item_created": item}

@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {
        "item_id": item_id,
        "status": "updated"
    }


@app.delete("/items/1")
def delete_item():
    return {"status": "deleted"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "message": "Item fetched successfully"
    }


