from fastapi import FastAPI
from pydantic import BaseModel
from goyacc import parser
from fastapi.middleware.cors import CORSMiddleware

# Funcion para analizar el codigo desde la API
def analize(code: str):
  try:
    result = parser.parse(code)
    return result
  except Exception as e:
    return str(e)
        

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
    print(obj.code)
    print('analizando...')
    result = analize(obj.code)
    # print('resultado: ', analize(obj.code))
    return result

