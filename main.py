from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import logging

# router import
# from router import serve, model, params

logger = logging.getLogger()

app = FastAPI()
# database = db.Serving()

# router include
# app.include_router(serve.router)
# app.include_router(model.router)
# app.include_router(params.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:8000",
    "http://stacker-demo.tk"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static',StaticFiles(directory="./"),name='static')



# @app.post('/api/save/params')
# def saveParams(parameter: Parameters):
#     logger.info("save params")
#     nowDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     database.insertParams(parameter.pallet, parameter.boxSize, parameter.layer, parameter.boxNumber,
#                           parameter.barcodeLocation, parameter.modelSelection, nowDateTime)
#     return {"result": True}
#
#
# @app.get('/api/load/model')
# def loadModel():
#     logger.info("load model function")
#     dbModelList = database.selectAllModel()
#     modelList = []
#     for m in dbModelList:
#         modelList.append(m['modelname'])
#     return {'model': modelList}
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
# @app.post("/api/save/model")
# async def saveModel(filename: str = Form(), file: UploadFile = File()):
#     content = await file.read()
#     UPLOAD_DIRECTORY = "./model_data"
#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(content)
#     database.insertModel(filename)
#     return {"success": True}
