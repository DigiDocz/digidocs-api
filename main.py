from fastapi import FastAPI
from app.features.extractor import route


app = FastAPI()

app.include_router(route.router)


@app.get('/')
def read_root():
  return {"message": "Hello World"}