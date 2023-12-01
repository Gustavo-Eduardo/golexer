from fastapi import FastAPI
from pydantic import BaseModel
from goyacc import analize
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Code(BaseModel):
    code: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analizeCode")
async def analizeCode(obj: Code):
    print('analizando...')
    print('resultado: ', analize(obj.code))
    return analize(obj.code)

