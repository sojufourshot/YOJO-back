from fastapi import APIRouter, File, UploadFile, Form
# from typing import List
# from pydantic import BaseModel

import logging, os

# router include
router = APIRouter(
    prefix="/api/v1/images",
)


@router.post('/')
async def test(image: UploadFile = File(), poseType: str = Form(...)):
    print('Upload images function')
    UPLOAD_DIRECTORY = "./official_images"
    # print(file)
    print(poseType)
    print()
    content = await image.read()
    with open(os.path.join(UPLOAD_DIRECTORY, image.filename), "wb") as fp:
        fp.write(content)
    result = {
        'status': 200,
        'message': 'Upload Success'
    }
    return result


# @router.post('/')
# async def uploadImages(images: List[UploadFile] = File()):
#     print('Upload images function')
#     UPLOAD_DIRECTORY = "./official_images"
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


@router.get('/')
def checkRoute():
    return {'message': 'images router check OK'}

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
#     data = ['./official_images/pose1.jpeg', idx]
#     result = {
#         'result': data
#     }
#     return result
