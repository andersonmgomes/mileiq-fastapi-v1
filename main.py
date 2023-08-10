from fastapi import Depends, FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/")
def read_root():
    return {"Hello": "World... this is a test"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    some_database = {1: {"name": "Foo", "price": 50.2}, 2: {"name": "Bar", "price": 62}, 
                     3: {"name": "Baz", "price": 50.2}, 4: {"name": "Qux", "price": 62}}
    if item_id not in some_database:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item": some_database[item_id]}

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/custom-response/")
def custom_response():
    content = {"message": "Custom Response"}
    return JSONResponse(content=content, status_code=200)

def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/dependency/")
def read_dependency(common: dict = Depends(common_parameters)):
    return common

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token/")
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Check the user's credentials and return a token
    return 'token'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
