from fastapi import APIRouter, File, UploadFile, Form
import httpx, asyncio
import os

# DB
import database.crud as crud

# router include
router = APIRouter(
    prefix="/api/v1/images",
)

# serverUrl = "http://localhost:8000"
serverUrl = 'http://203.252.166.225:8000'


@router.get('/')
def checkRoute():
    return {'message': 'images router check OK'}


async def sendAI(idx1, idx2):
    async with httpx.AsyncClient() as client:
        res = await asyncio.gather(client.get(serverUrl + f'/api/v1/ai/score/{idx1}/{idx2}'))
        print(res[0].text)
        return res[0].text


@router.post('/')
async def upload(image: UploadFile = File(), poseType: str = Form(...), poseName: str = Form()):
    print('Upload images function')
    # UPLOAD_DIRECTORY = "/data/images"
    UPLOAD_DIRECTORY = "./images"
    image_type = '.' + image.filename.split('.')[-1]
    file_name = str(len(os.listdir(UPLOAD_DIRECTORY + "/upload/orig/")) + 1) + image_type
    if poseType == 'orig':
        UPLOAD_DIRECTORY += '/upload/orig'
    else:
        UPLOAD_DIRECTORY += '/upload/custom'
    content = await image.read()
    with open(os.path.join(UPLOAD_DIRECTORY, file_name), "wb") as fp:
        fp.write(content)

    origin_image = crud.findPose(poseName)
    print(origin_image)
    print(str(len(os.listdir(UPLOAD_DIRECTORY))))
    res = await sendAI(origin_image, str(len(os.listdir(UPLOAD_DIRECTORY))))
    # res = await sendAI(1,2)
    # UPLOAD_DIRECTORY = './images/upload/orig'
    crud.saveUpload(file_name, poseName, eval(res)['score'], '', UPLOAD_DIRECTORY + file_name)

    result = {
        'status': 200,
        'message': 'Upload Success'
    }
    return result


@router.post('/cam')
async def uploadCam(image: UploadFile = File(), poseType: str = Form(...), poseName: str = Form()):
    print('Upload images function')
    # UPLOAD_DIRECTORY = "/data/images"
    UPLOAD_DIRECTORY = "./images"
    image_type = '.' + image.filename.split('.')[-1]
    file_name = str(len(os.listdir(UPLOAD_DIRECTORY + "/upload/orig/")) + 1) + image_type
    if poseType == 'orig':
        UPLOAD_DIRECTORY += '/upload/orig'
    else:
        UPLOAD_DIRECTORY += '/upload/custom'
    content = await image.read()
    with open(os.path.join(UPLOAD_DIRECTORY, file_name), "wb") as fp:
        fp.write(content)

    origin_image = crud.findPose(poseName)
    print(origin_image)
    print(str(len(os.listdir(UPLOAD_DIRECTORY))))
    res = await sendAI(origin_image, str(len(os.listdir(UPLOAD_DIRECTORY))))
    UPLOAD_DIRECTORY = './images/result/'
    crud.saveUpload(file_name, poseName, eval(res)['score'], '', UPLOAD_DIRECTORY + eval(res)['filename'])
    result = {
        'status': 200,
        'message': 'Upload Success'
    }
    return result


@router.get('/{pose_type}')
def loadImage(pose_type: int):
    result = crud.loadPoseList(pose_type)
    return result


@router.get('/{pose_name}')
def loadResult(pose_name: str):
    reult = crud.loadResultList(pose_name)
    return reult
