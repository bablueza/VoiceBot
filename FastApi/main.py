from typing import Optional
from fastapi import FastAPI, Form

from src import service
from param import items

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(name:Optional[str] = None):
    return {"Hello": name}

#x-www-form-urlencoded
@app.post("/")
def login(name: str = Form(...), age: int = Form(...)):
    return {"Hello": name +':'+str(age) +' year old.',}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/json")
def post_item(user:items.Item):
    return {
        "Hello": user.name +':'+str(user.age) +' year old.',
    }

app.include_router(service.router)