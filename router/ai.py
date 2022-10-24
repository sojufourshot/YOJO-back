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



@router.get('/{pose_type}')
def loadImage(pose_type: int):
    result = crud.loadPoseList(pose_type)
    return result


@router.get('/detail/{pose_name}')
def loadChoosePose(pose_name: str):
    result = crud.loadPoseDetail(pose_name)
    return result
