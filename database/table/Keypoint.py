from sqlalchemy import Column, TEXT, VARCHAR, DateTime, INT
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Keypoint(Base):
    __tablename__ = 'keypoint'
    image_name = Column(VARCHAR(50), primary_key=True)
    width  = Column(INT)
    height = Column(INT)
    keypoints = Column(TEXT)

    def __init__(self, image_name, width, height, keypoints):
        self.image_name = image_name
        self.width = width
        self.height = height
        self.keypoints = keypoints
