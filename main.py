from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging

# router import
from router import image
from router import ai
from router import cam

logger = logging.getLogger()

app = FastAPI()
# database = database.Serving()

# router include
app.include_router(image.router)
app.include_router(ai.router)
app.include_router(cam.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:8000",
    "https://localhost",
    "https://localhost:3000",
    "https://localhost:5500",
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'message': 'hello FastAPI!'}

