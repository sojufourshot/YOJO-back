from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

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
# app.include_router(database.router)
# app.include_router(params.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:8000",
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

# app.mount('/static',StaticFiles(directory="./"),name='static')



# @app.post('/api/save/params')
# def saveParams(parameter: Parameters):
#     logger.info("save params")
#     nowDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     database.insertParams(parameter.pallet, parameter.boxSize, parameter.layer, parameter.boxNumber,
#                           parameter.barcodeLocation, parameter.modelSelection, nowDateTime)
#     return {"result": True}
#
#
# @app.get('/api/load/database')
# def loadModel():
#     logger.info("load database function")
#     dbModelList = database.selectAllModel()
#     modelList = []
#     for m in dbModelList:
#         modelList.append(m['modelname'])
#     return {'database': modelList}
#
#
# @app.get('/api/load/params')
# def loadParmas():
#     logger.info("load Params")
#     params = database.selectParams()
#     print(ast.literal_eval(params['pallet']))
#     result = {
#         'pallet': ast.literal_eval(params['pallet']),
#         'boxSize': ast.literal_eval(params['boxSize']),
#         'layer': params['layer'],
#         'boxNumber': params['boxNumber'],
#         'barcodeLocation': params['barcodeLocation'],
#         'modelSelection': params['modelSelection']
#     }
#     return result
#
#
# @app.post("/api/save/database")
# async def saveModel(filename: str = Form(), file: UploadFile = File()):
#     content = await file.read()
#     UPLOAD_DIRECTORY = "./model_data"
#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(content)
#     database.insertModel(filename)
#     return {"success": True}
