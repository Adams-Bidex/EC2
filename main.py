from fastapi import FastAPI
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException, status, WebSocket
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from Calculator import bmi


app= FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def getInfo():
    return {'data':'Fast API IS Running on AWS EC2'}

@app.get('/bmi')
async def getbmi():
    data=bmi(19.8)
    return {'data':data}


