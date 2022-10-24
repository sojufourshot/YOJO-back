from sqlalchemy import Column, TEXT, VARCHAR, DateTime, INT
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Result(Base):
    __tablename__ = 'result'
    image_name = Column(VARCHAR(50), primary_key=True)
    position_name = Column(VARCHAR(100))
    score = Column(TEXT)
    author = Column(VARCHAR(50))
    created_at = Column(DateTime)
    image_path = Column(VARCHAR(200))

    def __init__(self, image_name, position_name, score, author,created_at,image_path):
        self.image_name = image_name
        self.position_name = position_name
        self.score = score
        self.author = author
        self.created_at=created_at
        self.image_path=image_path
