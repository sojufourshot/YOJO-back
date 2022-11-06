from fastapi import APIRouter, File, UploadFile, Form
# from typing import List
# from pydantic import BaseModel

import logging, os

# DB
# from database.dbconfig import
import database.crud as crud

# router include
router = APIRouter(
    prefix="/api/v1/ai",
)


@router.get('/')
def checkRoute():
    return {'message': 'ai router check OK'}

@router.get('/{idx}')
def loadKeypoint(idx:int):
    data = crud.loadKey(idx)
    return data
