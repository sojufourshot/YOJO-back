from sqlalchemy import Column, TEXT, VARCHAR, DateTime,INT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Position(Base):
    __tablename__='position'
    position_name = Column(VARCHAR(100),primary_key=True)
    position_type = Column(INT)
    image_path = Column(VARCHAR(200))
    description = Column(TEXT)
    author = Column(VARCHAR(50))

    def __init__(self,position_name,position_type,image_path,description,author):
        self.position_name = position_name
        self.position_type = position_type
        self.image_path=image_path
        self.description=description
        self.author=author