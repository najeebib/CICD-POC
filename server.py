from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/{name}")
def name(name: str):
    return {"message": f"Hello {name}!"}


@app.get("/api/cat-fact")
def api():
    response = requests.get("https://cat-fact.herokuapp.com/facts")
    return response.json()[0]["text"]
