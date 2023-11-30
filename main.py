from fastapi import FastAPI
from pydantic import BaseModel
from goyacc import analize

app = FastAPI()

class Code(BaseModel):
    code: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analizeCode")
async def analizeCode(code: Code):
    return analize(code)

