from fastapi import APIRouter, File, UploadFile, Form


# DB
import database.crud as crud

# router include
router = APIRouter(
    prefix="/api/v1/cam",
)

serverUrl = "http://localhost:8000"
# serverUrl = 'http://203.252.166.225:8000'

@router.get('/')
def checkRoute():
    return {'message': 'cam router check OK'}


@router.get('/{idx}')
def loadKeypoint(idx:int):
    data = crud.loadKey(idx)
    return data

