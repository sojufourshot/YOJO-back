from sqlalchemy.exc import SQLAlchemyError
import httpx, asyncio, ast, re

# database setting
from database import dbconfig
from database.table.Position import Position
from database.table.Result import Result
from database.table.Keypoint import Keypoint

engine = dbconfig.Engine()


def loadPoseList(pose_type):
    session = engine.sessionMaker()
    poseList = []
    try:
        data = session.query(Position).filter(Position.position_type == pose_type).all()
        i = 1
        for d in data:
            pose = {
                'id': i,
                'title': d.position_name,
                'author': d.author,
                'content': d.description,
                'src': d.image_path
            }
            poseList.append(pose)
            i += 1
    except SQLAlchemyError as e:
        print(e)
        session.close()
        return {'success': False, 'message': 'DB Error'}
    session.close()
    return {'position': poseList}


def findPose(pose_name):
    session = engine.sessionMaker()
    try:
        data = session.query(Position).order_by(Position.image_path).all()
        i = 1
        image_name = -1
        for d in data:
            print(d.position_name)
            print(pose_name)
            if d.position_name == pose_name:
                image_name = str(i)
                break
            else:
                i += 1
    except SQLAlchemyError as e:
        print(e)
        session.close()
        return {'success': False, 'message': 'DB Error'}
    session.close()
    return image_name


def loadKey(index):
    session = engine.sessionMaker()
    try:
        data = session.query(Keypoint).filter(Keypoint.image_name == (str(index) + '.jpg')).first()

        result = {
            'width': data.width,
            'height': data.height,
            'keypoints': ast.literal_eval(data.keypoints)

        }
        print(result)
    except SQLAlchemyError as e:
        print(e)
        session.close()
        return {'success': False, 'message': 'DB Error'}
    session.close()
    return result

