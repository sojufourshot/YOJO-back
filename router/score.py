import datetime
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError


class Parameter(BaseModel):
    pallet: List[str]
    boxSize: List[str]
    layer: str
    boxNumber: str
    barcodeLocation: str
    modelSelection: str
    userName: str


# router include
router = APIRouter(
    prefix="/api/v1/score",
)

@router.get('/{type}/{idx}')
def sendScore(type:str,idx:int):
    scoreNum = 0
    result = {
        'score' : scoreNum
    }
    return result



# @router.get('/load/{userName}')
# def loadParams(userName: str):
#     session = engine.sessionMaker()
#     logger.info("load Params")
#     try:
#         params = session.query(Parameters).filter(Parameters.userName == userName).order_by(
#             Parameters.dataTime.desc()).first()
#         session.close()
#     except SQLAlchemyError as e:
#         print(e)
#         session.close()
#         return {'success': False, 'msg': 'DB Error'}
#
#     result = {
#         'pallet': ast.literal_eval(params.pallet),
#         'boxSize': ast.literal_eval(params.boxSize),
#         'layer': params.layer,
#         'boxNumber': params.boxNumber,
#         'barcodeLocation': params.barcodeLocation,
#         'modelSelection': params.modelSelection,
#         'serveOutput': params.serveOutput,
#         'steps': params.steps,
#     }
#     return result
