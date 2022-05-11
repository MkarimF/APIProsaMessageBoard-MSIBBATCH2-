from fastapi import FastAPI
from requests import post

app=FastAPI()

@app.get('/')
def index():
        return None