from fastapi import APIRouter, File, UploadFile, Form
import httpx, asyncio, ast, re
# from typing import List
# from pydantic import BaseModel

import logging, os

# DB
import database.crud as crud

# router include
router = APIRouter(
    prefix="/api/v1/images",
)

serverUrl = "http://localhost:8000"


# serverUrl = 'http://203.252.166.225:8000'
@router.get('/')
def checkRoute():
    return {'message': 'images router check OK'}


async def sendAI(idx1, idx2):
    async with httpx.AsyncClient() as client:
        res = await asyncio.gather(client.get(serverUrl + f'/api/v1/ai/score/{idx1}/{idx2}'))
        print(res[0].text)
        return res[0].text  # json.loads(res[0].text)


@router.post('/')
async def upload(image: UploadFile = File(), poseType: str = Form(...), poseName: str = Form()):
    print('Upload images function')
    UPLOAD_DIRECTORY = "./images"
    # UPLOAD_DIRECTORY = "./data"
    image_type = '.' + image.filename.split('.')[-1]
    # file_name = str(len(os.listdir("./images/upload/official/"))+1)+image_type
    file_name = str(len(os.listdir("/data/images/orig/")) + 1) + image_type
    if poseType == 'official':
        UPLOAD_DIRECTORY += '/upload/orig'
        # UPLOAD_DIRECTORY += '/image/orig'
    else:
        UPLOAD_DIRECTORY += '/upload/custom'
        # UPLOAD_DIRECTORY += '/image/custom'
    content = await image.read()
    # print(content)
    with open(os.path.join(UPLOAD_DIRECTORY, file_name), "wb") as fp:
        fp.write(content)

    origin_image = crud.findPose(poseName)
    print(origin_image)
    # res = await sendAI(origin_image,str(len(os.listdir("./images/upload/official/"))))
    res = await sendAI(origin_image, str(len(os.listdir("/data/images/orig/"))))

    # res = await sendAI(1,str(len(os.listdir("./data/images/upload/orig/"))))
    # {"score":35.94632015121238}
    # score = res['score']
    print(res)
    result = {
        'status': 200,
        'message': 'Upload Success'
    }
    return result


@router.get('/{pose_type}')
def loadImage(pose_type: int):
    result = crud.loadPoseList(pose_type)
    return result

# @router.post('/')
# async def enrollNewPosition():


# @router.post('/')
# async def uploadImages(images: List[UploadFile] = File()):
#     print('Upload images function')
#     UPLOAD_DIRECTORY = "./images"
#     print()
#     for file in images:
#         content = await file.read()
#         with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
#             fp.write(content)
#
#
#
#     result = {
#         'status': 200,
#         'message': 'Upload Success'
#     }
#     return result


# @router.get('/{type}')
# def sendScore(type: str):
#     idx = 0
#     data = [['path', idx], ['path', idx]]
#     result = {
#         'imageList': data
#     }
#     return result


# @router.get('/{type}/{idx}')
# def sendScore(type: str, idx: int):
#     idx = 0
#     data = ['./images/pose1.jpeg', idx]
#     result = {
#         'result': data
#     }
#     return result
