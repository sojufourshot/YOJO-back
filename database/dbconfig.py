from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

app = {
    'name': 'mysql+pymysql',
    'user': 'root',
    'password': '1234!',
    'host': 'localhost',
    'dbconn': 'yojo',
    'port': '3306',
}

conn_string = f'{app["name"]}://{app["user"]}:{app["password"]}@{app["host"]}:{app["port"]}/{app["dbconn"]}'


class Engine:

    def __init__(self):
        self.engine = create_engine(conn_string, pool_recycle=500)

    def sessionMaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn
